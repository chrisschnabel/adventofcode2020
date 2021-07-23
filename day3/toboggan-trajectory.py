import time

class Hill:
    "A complicated biome"

    def __init__(self,angle):

        self.f = open("input.txt")
        self.trees = self.f.readline().strip()
        self.offsetX = 0
        self.offsetY = 0
        self.angle = angle

    def hitTree(self):
        equivOffset = self.offsetX % len(self.trees)
        if self.trees[equivOffset]=="#":
            return True
        else:
            return False

    def descend(self):
        self.trees = self.f.readline().strip()
        self.offsetX += self.angle[0]
        self.offsetY += self.angle[1]

    def cleanup(self):
        self.f.close()


def main():
    timeStart = time.perf_counter_ns()

    h = Hill([3,1])
    hits = 0

    while h.trees:
        if h.hitTree():
            hits += 1
        h.descend()

    print("Hits: "+str(hits))
    h.cleanup()
    del h

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")

if __name__ == "__main__":
    main()
