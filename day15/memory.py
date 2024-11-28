import time


def main():

    timeStart = time.perf_counter_ns()

    # seq = [0, 3, 6]
    # seq = [1, 3, 2]
    # seq = [2, 1, 3]
    # seq = [1, 2, 3]
    # seq = [2, 3, 1]
    # seq = [3, 2, 1]
    # seq = [3, 1, 2]
    seq = [0, 1, 4, 13, 15, 12, 16]

    num = seq.pop()
    turns = 2020

    for turn in range(len(seq)+1, turns+1):

        print(f"{num} is spoken on turn {turn}.")

        if num not in seq:
            seq.append(num)   # If it's the first time it appears, then 0
            num = 0

        else:

            # The turn of the time prior to turn_a
            turn_b = len(seq) + 1 - (seq[::-1].index(num) + 1)
            # print(f"{num} is spoken prior to that on turn {turn_b}.")

            # Prepare for the next round
            seq.append(num)
            num = turn - turn_b

        # print(f"Sequence is now {seq}, so the next number is {num}\n")
        print(f"  the next number is {num}\n")

    print(f"Final seq {seq}")
    print(f"{seq[-1]} is spoken on turn {len(seq)}.")

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {(timeStop - timeStart)/1000000} ms")


if __name__ == "__main__":
    main()
