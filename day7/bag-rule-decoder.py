import time
import re


class Bag:
    "The bag and all the possible bags it contains"

    def __init__(self, bag):
        "Initializes the bag based on a tuple of color and set of bags inside"

        self.color = ""             # The color of the bag itself
        self.contains_top = {}      # bags immediately inside: key is color, val is count
        self.contains_all = {}      # bags at any depth: key is color, val is count
        self.is_populated = False   # A flag to indicated when contains_all is complete

        # Set values based on the input parms
        self.color , contains_top = bag
        self.add_contains_top(contains_top)

        # If it's an empty bag, then contains_all is already up to date
        if not contains_top:
            self.is_populated = True


    def add_contains_top(self, contains_dict):
        "adds a set to the set of bags at the first depth of hierarchy"

        self.contains_top.update(contains_dict)


    def update_contains_all(self, bags_dict):
        "recursively iterate the contained bags to know all bags inside, returns all bags as a set"

        # Only do something if not already done
        if not self.is_populated:
            for color , count in self.contains_top.items():

                # First, each element belongs in the all set
                if color in self.contains_all.keys():
                    self.contains_all[color] += count
                else:
                    self.contains_all[color] = count

                # Recursively call this function to ensure a comprehensive contains_all
                all_bags = bags_dict[color].update_contains_all(bags_dict)

                # Update contains_all by adding in the new bags found
                for b in all_bags.keys():
                    if b in self.contains_all.keys():
                        self.contains_all[b] += count * all_bags[b]
                    else:
                        self.contains_all[b] = count * all_bags[b]

        # Recursion is complete, so the contains_all is now populated
        self.is_populated = True
        return self.contains_all

    def is_contained(self, color):
        "returns the quantity of that color bag contained, at any depth"

        if color in self.contains_all.keys():
            return self.contains_all[color]

        return 0

    def contains_count(self):
        return sum(self.contains_all.values())

    def is_populated(self):
        return self.is_populated

class Reader:
    "Reads the input file and returns a tuple of bag color and it's contents with read_next"

    def __init__(self):
        self.f = open("input.txt")


    def read_next(self):
        "Returns a tuple of bag_color (string) and the bags it contains (set)"
        #             bag  contains_list
        # self.bag = ("color_a", {"color_b": 2, "color_c": 3})

        line = self.f.readline().strip()

        if line:
            # Split the line based on spaces, and the k-v-p based on :
            bag_color, contains = line.split("bags contain")
            bag_color = bag_color.strip()

            contains_dict = {}

            if contains != " no other bags.":
                for x in contains.split(","):
                    m = re.search("([0-9]+)\s([a-z]+\s[a-z]+)", x)
                    contains_dict[m.group(2)]=int(m.group(1))

            return (bag_color, contains_dict)
        else:
            return False

    def cleanup(self):
        self.f.close()

def main():
    timeStart = time.perf_counter_ns()

    bags = {}       # A dict of colors to lookup bag objects
    r = Reader()    # Reader object used to iterate on file input

    next_bag = r.read_next()
    while next_bag:

        # Get all the information about the next bag and add to dict object
        color = next_bag[0]
        bags[color] = Bag(next_bag)

        # Continue to iterate
        next_bag = r.read_next()

    # At this point we have n bags in the set, each of which have 0-5(?) entries in their 'top' and 'all'
    # We need to iterate and update the contains_all variable of the bags, efficiently.
    # Option A:
    #   * iterate through each bag, and add to contains_all by recursively looking up each bag in contains_top
    #   * cost: n*m1*m2*... where m1 etc are num members at each depth
    #   * This could be improved by marking any bag that has already had it's depth explored, so no bag will be recursed more than once

    print('Beginning update of contains_all')

    # Update all bags so their full contents are known
    for b in bags.values():
        b.update_contains_all(bags)

    count = 0
    for b in bags.values():
        if b.is_contained("shiny gold"): count += 1

    print(str(count) + " bags contain 'shiny gold'")

    count = 0
    for x in bags['shiny gold'].contains_all.values():
        count += int(x)

    print(str(bags['shiny gold'].contains_count()) + " bags in 'shiny gold'")

    r.cleanup()

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")

if __name__ == "__main__":
    main()
