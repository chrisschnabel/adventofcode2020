import time

from adapter_array import NumberReader
from adapter_array import AdapterArray


# Determine distinct ways to arrange adapters


# Determine which adapters are eligible to skip
#     single_skips are possible when next-prior <4
#     first element >0 is elibible to be skipped
#     the last can never be skipped

# All combinations of single_skips are 2**single_skips

# multi skips that aren't possible should be subtracted out
#     double skips are sometimes possible
#     triple or greater skips are never possible


def main():
    timeStart = time.perf_counter_ns()

    # Reader object used to iterate on file input
    r = NumberReader('input.txt')
    jolts = r.get_numlist()

    adapt = AdapterArray(jolts)
    print("Part one answer is: " + str(adapt.calc_answer()))

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")


if __name__ == "__main__":
    main()
