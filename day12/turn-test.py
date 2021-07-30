import time
import numpy as np


def turn(s_dir, dir, mag):
    print(f"   dir before rot {s_dir}")

    dir = dir[0]

    if mag == 0:
        print("   Rotate 0")  # checked
        rot = np.array([[1, 0],
                        [0, 1]])
    if mag == 90 and dir == 1:
        print("   Rotate 90 CW")
        rot = np.array([[0, 1],
                        [-1, 0]])
    if mag == 90 and dir == -1:
        print("   Rotate 90 CCW")
        rot = np.array([[0, -1],
                        [1, 0]])
    if mag == 180:
        print("   Rotate 180")
        rot = np.array([[-1, 0],
                        [0, -1]])
    if mag == 270 and dir == -1:
        print("   Rotate 270 CCW")
        rot = np.array([[0, 1],
                        [-1, 0]])
    if mag == 270 and dir == 1:
        print("   Rotate 270 CW")
        rot = np.array([[0, -1],
                        [1, 0]])

    new = rot.dot(s_dir.T).T
    print(f"   dir after rot {new}")

    return new


def main():
    timeStart = time.perf_counter_ns()

    s_dir = np.array([0, 1])
    possibles = [[[1], 0],
                 [[1], 90],
                 [[1], 180],
                 [[1], 270],
                 [[-1], 0],
                 [[-1], 90],
                 [[-1], 180],
                 [[-1], 270],
                 ]

    for dir, mag in possibles:
        s_dir = np.array([0, 1])
        print(f"Next test")
        s_dir = turn(s_dir, dir, mag)

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {(timeStop - timeStart)/1000000} ms")


if __name__ == "__main__":
    main()
