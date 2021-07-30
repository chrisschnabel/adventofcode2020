import time


def main():
    timeStart = time.perf_counter_ns()

    # Get info from file
    f = open("input.txt")
    now = int(f.readline().strip())
    busses = {}
    w = 0
    for b in f.readline().strip().split(","):
        if not b == "x":
            busses[int(b)] = w
        w += 1

    f.close()

    step = 1    # We will check using this time step
    current = 1
    wait = 0
    now = 0

    # Find when the next bus is the proper wait from the first
    while not wait == busses[current]:
        now += step
        wait = busses[current] - now % busses[0]

    print(f"Bus {current} is {wait} behind bus {busses[0]}")

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {(timeStop - timeStart)/1000000} ms")


if __name__ == "__main__":
    main()
