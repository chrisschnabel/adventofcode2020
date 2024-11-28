import time


def main():

    timeStart = time.perf_counter_ns()

    seq = [0, 1, 2, 3, 4, 5, 6]
    num = 6

    print(f"seq\t\t{seq}")
    print(f"len(seq)\t{len(seq)}")
    print(f"seq.index(2)\t{seq.index(2)}")
    print(f"seq[-3::-1]\t{seq[-3::-1]}")

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {(timeStop - timeStart)/1000000} ms")


if __name__ == "__main__":
    main()
