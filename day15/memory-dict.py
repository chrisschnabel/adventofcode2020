import time


def main():

    timeStart = time.perf_counter_ns()

    turns = 30000000

    # seq = [0, 3, 6]
    # seq = [1, 3, 2]
    # seq = [2, 1, 3]
    # seq = [1, 2, 3]
    # seq = [2, 3, 1]
    # seq = [3, 2, 1]
    # seq = [3, 1, 2]
    seq = [0, 1, 4, 13, 15, 12, 16]

    num = str(seq.pop())

    # A dictionary that contains the last time a number was spoken
    last_spoken = {}
    for x in seq:
        last_spoken[str(x)] = seq.index(x) + 1

    # For the remaining turns we will update the dict and calc the next num
    for turn in range(len(seq)+1, turns+1):

        if turn == turns:
            print(f"{num} being spoken on turn {turn}")

        if num in last_spoken.keys():
            prior_turn = last_spoken[num]
            # print(f"  last spoken on {prior_turn}")
            last_spoken[num] = turn
            num = str(turn - prior_turn)

        else:
            # print(f"  not spoken before")
            last_spoken[num] = turn
            num = "0"

        # print(f"  {num} will be spoken next turn")

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {(timeStop - timeStart)/1000000} ms")


if __name__ == "__main__":
    main()
