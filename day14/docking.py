import time
import re


class Docking:

    def __init__(self):
        self.mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        self.mem = {}  # dictionary to hold the memory

    def readfile(self, file):

        p_mask = re.compile("^mask")
        p_mask_data = re.compile("^mask = ([X10]+)")

        for line in open(file):

            m = re.match(p_mask_data, line)

            # Determine whether this is a mask line
            if m:
                # Retrieve the mask and set it
                self.mask = m.group(1)
            else:
                # Process as a mem line
                self.parse_mem_line(line)

        print(f"The sum of the mem dict is {self.sum_mem()}")

    def parse_mem_line(self, line):

        p = re.compile("^mem\[(\d+)\] = (\d+)")
        m = re.match(p, line)

        address = m.group(1)
        value = format(int(m.group(2)), "036b")
        result = self.apply_value_mask(value)

        self.write_to_memory(address, result)

    def write_to_memory(self, address, value):
        self.mem[address] = value

    def apply_value_mask(self, value):
        "Input the value and the mask; return the resultant"

        mask = self.mask

        if len(value) != len(mask):
            print("Error, value and mask aren't the same length")
            return False

        result = ""

        for m, v in zip(mask, value):
            if m == "X":
                r = v
            else:
                r = m

            result = result + r

        print(f"value:\t{value}")
        print(f"mask:\t{mask}")
        print(f"result:\t{result}")

        return result

    def sum_mem(self):

        sum = 0
        for v in self.mem.values():
            sum += int(v, 2)

        self.sum = sum

        return sum


def main():

    timeStart = time.perf_counter_ns()

    d = Docking()
    d.readfile("input-test.txt")

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {(timeStop - timeStart)/1000000} ms")


if __name__ == "__main__":
    main()
