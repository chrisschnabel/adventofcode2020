import time

class Hill:
    "A complicated biome"

    def __init__(self,angle):


        self.angle = angle

    def hitTree(self):
        "Determines whether a tree on the current row was hit"

        equivOffset = self.offsetX % len(self.trees)
        if self.trees[equivOffset]=="#":
            return True
        else:
            return False

    def descend(self):
        "Descends the hill by the designated number of rows specified in the y-component of angle"

        for x in range(self.angle[1]):
            self.trees = self.f.readline().strip()
        #print(self.trees)

        self.offsetX += self.angle[0]
        self.offsetY += self.angle[1]


    def getTreesHit(self):
        "Determines for the given angle how many trees are hit"

        self.f = open("input.txt")
        self.trees = self.f.readline().strip()

        # print(self.trees)

        self.offsetX = 0
        self.offsetY = 0
        self.hits = 0

        while True:
            if not self.trees:
                break
            if self.hitTree():
                self.hits += 1
            self.descend()

        self.f.close()

        return self.hits


def main():
    timeStart = time.perf_counter_ns()

    product = 1

    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

    for s in slopes:
        h = Hill(s)
        print("Hits: "+str(h.getTreesHit()))
        product = product*h.getTreesHit()


    print("Product: "+str(product))

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")

if __name__ == "__main__":
    main()
