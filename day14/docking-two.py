import time
import re


class Docking:

    def __init__(self):
        self.mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        self.mem = {}  # dictionary to hold the memory
        self.program = []
        self.sum = 0

    def readfile(self, file):

        p_mask = re.compile("^mask = ([X10]+)")
        p_mem = re.compile("^mem\[(\d+)\] = (\d+)")

        for line in open(file):

            m_mask = re.match(p_mask, line)
            m_mem = re.match(p_mem, line)

            # Determine whether this is a mask line
            if m_mask:
                # Process as a mask line
                mask = m_mask.group(1)
                fmat = "0" + str(len(mask)) + "b"

            elif m_mem:
                # Process as a mem line
                address = format(int(m_mem.group(1)), fmat)
                value = format(int(m_mem.group(2)), fmat)
                result = self.apply_mask(mask, address)

                # Remove any intersection of address space from prior commands

                old_prog = self.program.copy()

                for x in range(len(old_prog)):
                    old_a = old_prog[x].get("address")
                    old_v = old_prog[x].get("value")
                    old_s = old_prog[x].get("sign")

                    # If the sign is positive we need to subtract any intersect
                    # If the sign is negative it has already been removed
                    # - we must check for the intersect and add it back,
                    # as it will be removed again when we encounter the orig

                    new_a = self.get_intersect(old_a, result)
                    if new_a:
                        new_s = old_s * -1
                        self.program.append(
                                {"address": new_a, "value": old_v, "sign": new_s})
                        num_addr = 2**new_a.count("X")
                        add_this = int(old_v, 2) * num_addr * new_s
                        self.sum += add_this
                        print(f"   Adding {add_this} b/c of intersect")

                # Add the new instruction to the program
                self.program.append(
                    {"address": result, "value": value, "sign": 1})
                num_addr = 2**result.count("X")

                add_this = int(value, 2) * num_addr
                self.sum += add_this
                print(f"   Adding {add_this}")

    def apply_mask(self, mask, address):
        "Input the mask and address; return new address with fluctuating 'X'"

        if len(address) != len(mask):
            print("Error, address and mask aren't the same length:")
            print(f"   address{address}")
            print(f"   mask   {mask}\n")
            return False

        # Create the address with the 'X' still in it for now
        result = ""

        for m, a in zip(mask, address):
            if m == "0":
                r = a
            else:
                r = m

            result = result + r

        print(f"addr:\t{address}")
        print(f"mask:\t{mask}")
        print(f"result:\t{result}")
        print("")

        return result

    def get_intersect(self, m_1, m_2):
        "Input two masked addresses; return a new masked address"

        # Check inputs
        if m_1 == None:
            return None
        if m_2 == None:
            return None
        if len(m_1) != len(m_2):
            print("Error, expecting addresses of same length")

        # Find an intersection
        new = ""

        # Address all cases where exactly one digit is X
        for a, b in zip(m_1, m_2):

            # Treat all cases of a
            if a == "X":
                if b == "X":
                    n = "X"
                elif b == "1":                       # a is X and b is a digit
                    n = "1"
                else:
                    n = "0"
            else:
                if b == "X":                # a is digit and b is X
                    n = a                   # no change
                elif b == a:                # a and b are the same digit
                    n = a                   # no change
                else:
                    return None              # two diff digits - no intersect
            new = new + n

        print(f"   m_1:\t{m_1}")
        print(f"   m_2:\t{m_2}")
        print(f"   new:\t{new}\n")

        return new


def main():

    timeStart = time.perf_counter_ns()

    d = Docking()
    d.readfile("input.txt")

    for x in d.program:
        print(x)

    print(f"\nSum is {d.sum}")

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {(timeStop - timeStart)/1000000} ms")


if __name__ == "__main__":
    main()
