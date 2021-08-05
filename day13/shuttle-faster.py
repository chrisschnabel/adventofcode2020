import time


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

    print(f"busses: {busses}")
    print(f"target: {target}")

    now = 1
    step = 1

    # Iterate on each bus until on target
    for bus, target in zip(busses, target):

        on_target = False
        while not on_target:

            # Check whether a bus departs target min from now
            if (((now+target) % bus) == 0):
                on_target = True
                step *= bus

            # This condition only happens at multiples of the current bus
            now += step

    print(f"\nFinal time: {now-step}")

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {(timeStop - timeStart)/1000000} ms")


if __name__ == "__main__":
    main()
