import time
import numpy as np


def get_wait(time, nums):
    "Input a time and a list of busses, return array wait times"

    out = []

    for num in nums:

        if num < time:
            w = num - time % num
            if num == w:
                w = 0
        elif num == time:
            w = 0
        if num > time:
            w = num - time

        out.append(w)

    return np.array(out)


def main():
    timeStart = time.perf_counter_ns()

    # Get info from file
    f = open("input.txt")
    now = int(f.readline().strip())
    busses = []
    target = []

    w = 0
    for b in f.readline().strip().split(","):
        if not b == "x":
            busses.append(int(b))
            target.append(w)
        w += 1
    f.close()

    target = np.array(target)

    now = busses[0]

    delta = [1]

    on_target = False

    while not on_target:
        # for x in range(5):
        wait = get_wait(now, busses)
        delta = np.subtract(target, wait)

        step = 1
        for i in range(len(delta)):
            if delta[i] == 0:
                step *= busses[i]

        now += step
        on_target = (wait == target).all()

        print(f"time: {now-step}")

    print(f"busses: {busses}")
    print(f"target: {target}")
    print(f"wait: {wait}")
    print(f"delta: {delta}")

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {(timeStop - timeStart)/1000000} ms")


if __name__ == "__main__":
    main()
