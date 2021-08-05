import time
import numpy as np


def read_array_from_file(file):
    "Reads nodelimited characters from a text file into an numpy array"
    input = []
    with open(file) as f:
        for line in f:
            row = list(line.strip())
            input.append(row)

    return np.array(input)


class Seating:
    def __init__(self, file="input.txt"):
        "Reads a file and reads the numbers in it as a list"

        self.seats = read_array_from_file(file)

    def get_seats(self):
        return self.seats

    def run_rules(self):

        def count_adjacent_round1(seats, y, x):

            adj = 0
            max_y, max_x = seats.shape
            max_x -= 1
            max_y -= 1

            locs = [[y-1, x-1],
                    [y, x-1],
                    [y+1, x-1],
                    [y-1, x],
                    [y+1, x],
                    [y-1, x+1],
                    [y, x+1],
                    [y+1, x+1]]

            for a in locs:
                if a[0] < 0 or a[1] < 0 or a[0] > max_y or a[1] > max_x:
                    continue

                if seats[a[0], a[1]] == "#":
                    adj += 1

            return adj

        def count_adjacent(seats, coord):

            adj = 0
            max_y, max_x = seats.shape
            max_x -= 1
            max_y -= 1

            # This represents each of the directions we will check
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1],
                    [-1, 1], [-1, -1], [1, 1], [1, -1]]

            for dir in dirs:

                # Move in the direction
                loc = [a + b for a, b in zip(dir, coord)]
                #print(f"Checking loc {loc} from coord {coord}")

                while True:

                    # Check if exited array, and break without counting
                    if loc[0] < 0 or loc[1] < 0 or loc[0] > max_y or loc[1] > max_x:
                        break

                    # Check if the location being checked is occupied
                    if seats[loc[0], loc[1]] == "#":
                        adj += 1
                        #print(f"loc {loc} is occupied ")
                        break

                    # We could find an empty seat, so we break without counting
                    if seats[loc[0], loc[1]] == "L":
                        #print(f"loc {loc} is empty ")
                        break

                    # Otherwise, keep moving!
                    tmp = loc.copy()
                    loc = [a + b for a, b in zip(dir, tmp)]
                    # print(f"Checking loc {loc} from coord {coord}")

            return adj

        prior = np.copy(self.seats)
        a_adj = np.copy(self.seats)

        size = prior.shape
        for y in range(size[0]):
            for x in range(size[1]):

                seat = prior[y, x]

                # Only bother if not floor
                if not seat == ".":
                    adj = count_adjacent(prior, [y, x])

                    # If a seat is empty (L) and there are no
                    # occupied seats adjacent to it, the seat becomes occupied.
                    if seat == "L" and adj == 0:
                        self.seats[y, x] = "#"

                    # If a seat is occupied (#) and four or more seats
                    # adjacent to it are also occupied, the seat becomes empty.
                    # --> Updated to five or more for round 2
                    if seat == "#" and adj > 4:
                        self.seats[y, x] = "L"

                    a_adj[y, x] = adj
        print("Adjacency Matrix:")
        print(a_adj)


def main():
    timeStart = time.perf_counter_ns()

    s = Seating("input.txt")

    print("Original:")
    print(s.seats)

    prior = None
    n = 0

    # Continue as long as the seating hasn't stabilized
    while not (prior == s.seats).all():
        # for x in range(2):

        # Make a copy to compare, and run the iteration
        prior = np.copy(s.seats)
        s.run_rules()

        # Some handy info
        n += 1
        print(f"Round {n}:")
        print(s.seats)

    sum = np.count_nonzero(s.seats == "#")
    print(sum)

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {(timeStop - timeStart)/1000000} ms")


if __name__ == "__main__":
    main()
