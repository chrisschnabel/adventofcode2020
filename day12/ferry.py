import time
import re
import numpy as np


def read_route_from_file(file):
    "Reads nav instructions into a list"

    input = []
    p = re.compile("([A-Z]+)([0-9]*)")

    with open(file) as f:
        for line in f:
            line.strip()
            m = re.search(p, line)
            input.append([m.group(1), int(m.group(2))])
        f.close()

    print(input)

    return input


class Route:
    def __init__(self, file="input-test.txt"):
        "Reads a file and reads the numbers in it as a list"

        self.route = read_route_from_file(file)
        self.loc = [0, 0]
        self.dir = np.array([0, 1])

    def take_step(self, input):

        def move(self, dir, mag):
            # print(f"move dir {dir} and mag {mag}")

            # The vector is the dir * the magnitude
            m = np.full((1, 2), mag)
            v = np.multiply(m, dir)
            # print(f"calc'd vector is {v}")

            self.loc = np.add(self.loc, v)
            print(f"new self.loc is {self.loc}")

        def turn(self, dir, mag):
            # print(f"   dir before rot {self.dir}")

            if mag == 0:
                # print("   Rotate 0")  # checked
                rot = np.array([[1, 0],
                                [0, 1]])
            if mag == 90 and dir == 1:
                # print("   Rotate 90 CW")
                rot = np.array([[0, 1],
                                [-1, 0]])
            if mag == 90 and dir == -1:
                # print("   Rotate 90 CCW")
                rot = np.array([[0, -1],
                                [1, 0]])
            if mag == 180:
                # print("   Rotate 180")
                rot = np.array([[-1, 0],
                                [0, -1]])
            if mag == 270 and dir == -1:
                # print("   Rotate 270 CCW")
                rot = np.array([[0, 1],
                                [-1, 0]])
            if mag == 270 and dir == 1:
                # print("   Rotate 270 CW")
                rot = np.array([[0, -1],
                                [1, 0]])

            self.dir = rot.dot(self.dir.T).T
            # print(f"   dir before rot {self.dir}")

        def forward(self, dir, mag):

            # Same as moving in direction already facing
            move(self, self.dir, mag)

        command = {
                    "N": [move, np.array([-1, 0])],
                    "S": [move, np.array([1, 0])],
                    "E": [move, np.array([0, 1])],
                    "W": [move, np.array([0, -1])],
                    "L": [turn, -1],
                    "R": [turn, 1],
                    "F": [forward, 1]}

        comm, mag = input

        func, arg = command.get(comm, lambda: "invalid command")
        func(self, arg, mag)

    def calc_route(self):

        route = self.route
        route.reverse()

        while route:
            self.take_step(route.pop())


def main():
    timeStart = time.perf_counter_ns()

    r = Route("input.txt")
    r.calc_route()

    print(f"Manhattan distance is {r.loc.sum()}")

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {(timeStop - timeStart)/1000000} ms")


if __name__ == "__main__":
    main()
