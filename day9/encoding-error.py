import time


class XMAS:
    "Encryption scheme"

    def __init__(self, input):
        "Initializes based on an input set of int"

        self.preamble = 25              # Default preamble length
        self.series = input
        self.crypto_weakness = False

    def set_preamble_len(self, input):
        self.preamble = input

    def find_num_not_sum(self):
        """Determines which is the first number that is
        not the sum of two unique numbers in the prior `preamble` digits"""

        def has_digits_that_sum(input_list, target):

            # Dumb iteration through all elements of the list to check their sums
            for value_1 in input_list:
                value_2 = target - value_1
                if value_2 in input_list:
                    if value_1 != value_2:
                        return True

            return False

        for current_index in range(self.preamble, len(self.series), 1):

            # Get the current number and the list we need to check it against
            priors_index = current_index - self.preamble
            current = self.series[current_index]
            priors = self.series[priors_index: current_index: 1]

            if not has_digits_that_sum(priors, current):
                return current

    def find_contiguous_set(self, target):
        """Input a target value and it searches the series for a contiguous set
        that sums to the target value"""

        print("Contiguous target is: "+str(target))

        max_index = len(self.series)
        lower_index = 0
        upper_index = lower_index + 1
        contiguous_sum = self.series[lower_index]+self.series[lower_index+1]

        # This loop will add numbers to the end of the set until it goes over,
        # then remove numbers from the front of the set until it goes under,
        # and continue this until the target is found

        while True:

            # Add to the set until it's large enough
            while contiguous_sum < target:
                if upper_index > max_index:
                    print("No contiguous set found summing to "+str(target))
                    return False
                upper_index += 1
                contiguous_sum += self.series[upper_index]

            # Make sure we're not on target
            if contiguous_sum == target:
                contig_list = self.series[lower_index: upper_index+1: 1]
                self.crypto_weakness = min(contig_list) + max(contig_list)
                return self.crypto_weakness

            # Now remove digits from the front of the set to make room for more
            while contiguous_sum > target:
                contiguous_sum -= self.series[lower_index]
                lower_index += 1

            # Make sure we're not on target
            if contiguous_sum == target:
                contig_list = self.series[lower_index: upper_index+1: 1]
                self.crypto_weakness = min(contig_list) + max(contig_list)
                return self.crypto_weakness


class NumberReader:
    "Reads and input file of numbers"

    def __init__(self, file):
        self.f = open(file)
        self.numbers = []

    def read_all(self):
        "Returns a set of numbers from the specified file"

        line = self.f.readline().strip()
        while line:
            x = int(line)
            self.numbers.append(x)
            line = self.f.readline().strip()

        return(self.numbers)

    def cleanup(self):
        self.f.close()


def main():
    timeStart = time.perf_counter_ns()

    # Reader object used to iterate on file input
    r = NumberReader('input.txt')
    preamble = 25

    numbers = r.read_all()          # Read the digits from the input file

    # Create the encryption object with the input
    xmas = XMAS(numbers)
    xmas.set_preamble_len(preamble)

    # Request the number that does not sum from digits in the length of preamble
    suspect = xmas.find_num_not_sum()
    print("Digit that doesn't sum in it's preamble: "+str(suspect))
    crypto_weakness = xmas.find_contiguous_set(suspect)
    print("Crypto weakness is: "+str(crypto_weakness))

    r.cleanup()

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")


if __name__ == "__main__":
    main()
