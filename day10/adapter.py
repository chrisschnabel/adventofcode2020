import time


class AdapterArray:
    "The class used to create and manipulate the list of jolts"

    def __init__(self, jolts):
        "Initializes and pads the jolts list with the wall and device joltage"

        # Add zero to the beginning and +3 to the end
        jolts.sort()
        jolts.insert(0, 0)
        max = jolts[len(jolts)-1]     # Max value since the list is sorted
        jolts.append(max+3)

        self.jolts = jolts

    def calc_diff(self, l_input):
        "Takes the self.jolts and sets self.diff as a list of the deltas"

        jolts = l_input.copy()
        diff = []

        # Because we're popping we're doing the deltas from right to left
        a = jolts.pop()
        while jolts:
            b = jolts.pop()
            diff.append(a-b)
            a = b

        # Reverse as we went right to left, yet still appended
        diff.reverse()

        return diff

    def calc_permutations(self, l_jolts):

        # The number of permutations for n digits follows a tribbonacci series
        options = [1, 1, 2, 4, 7, 13, 24]

        list = l_jolts.copy()       # Need a copy as we'll be popping
        total = 1                   # The number of permutations
        x = list.pop()              # x is the smaller of our number pair
        l_sub = [x]

        while list:
            y = x                   # y is the larger of our number pair
            x = list.pop()
            diff = y-x              # diff between elements

            if diff == 1:
                # Continue appending to a sub-list we can treat discretely
                l_sub.append(x)

            elif diff == 2:
                print("WARNING - Not expecting a diff of 2! Will be wrong.")

            else:
                # Found a diff of 3, so now operate on the sub-list
                perms = options[len(l_sub)-1]
                total *= perms
                print(f"{perms} options for {l_sub}")
                print(f"total is {total}")

                # Reset variables for next sub-array
                l_sub = [x]

        perms = options[len(l_sub)-1]
        total *= perms
        print(f"{perms} options for {l_sub}")
        print(f"total is {total}")

        self.perms = total
        return total

    def calc_dist(self):

        dist = [0, 0, 0, 0]
        for x in self.diff:
            if x > 3:
                print("Warning - diff is greater than 3. Unexpected.")
            dist[x] += 1

        self.dist = dist

    def calc_answer(self):
        """Returns number of 1-jolt differences multiplied
        by the number of 3-jolt differences"""

        print(self.jolts)

        self.diff = self.calc_diff(self.jolts)
        self.calc_dist()

        return self.dist[1]*self.dist[3]


class NumberReader:
    "Reads and input file of numbers"

    def __init__(self, file):
        "Reads a file and reads the numbers in it as a list"

        self.f = open(file)
        self.read_numlist()

    def get_numlist(self):
        return self.numbers

    def read_numlist(self):
        "Returns a set of numbers from the specified file"

        self.numbers = []

        line = self.f.readline().strip()
        while line:
            x = int(line)
            self.numbers.append(x)
            line = self.f.readline().strip()

        return(self.numbers)

        self.f.close()


def main():
    timeStart = time.perf_counter_ns()

    # Reader object used to iterate on file input
    r = NumberReader('input.txt')
    jolts = r.get_numlist()

    adapt = AdapterArray(jolts)
    print("Part 1 answer is " + str(adapt.calc_answer()))
    print("Part 2 answer is " + str(adapt.calc_permutations(jolts)))

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")


if __name__ == "__main__":
    main()
