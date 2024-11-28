import time
import re


class Field:
    """Creates a field type, along with the rules it must follow,
    `rule` should be the string provided in the input"""

    def __init__(self, name, rule):

        self.name = name
        self.rule_s = rule
        # self.parse_rule()

    def in_range(self, input):

        for min, max in self.rule_s:
            if input >= min:
                if input <= max:
                    return True

        # if it hasn't exited by now, it's not in range
        return False


def main():

    timeStart = time.perf_counter_ns()

    p_rule = re.compile('^([a-z ]+): (.+)-(.+) or (.+)-(.+)$')

    fields = {}
    nearby = []
    scanning = "rules"

    for line in open("input-test.txt"):
        line.strip()

        if scanning == "rules":
            print(line)
            if line == "your ticket:\n":
                scanning = "yours"
                print("Now scanning your ticket")
                continue

            m = re.match(p_rule, line)

            if m:
                name = m.group(1)
                print(f"Creating field '{name}'")
                ranges = [[int(m.group(2)), int(m.group(3))],
                          [int(m.group(4)), int(m.group(5))]]
                fields[name] = Field(name, ranges)
        if scanning == "yours":
            if line == "nearby tickets:\n":
                scanning = "nearby"
                print("Now scanning nearby tickets")
                continue
            if line:
                my_ticket = [int(i) for i in line.split(",")]

        if scanning == "nearby":
            nums = [int(i) for i in line.split(",")]
            nearby.append(nums)

    # test each ticket to ensure all values could belong to at least one field
    for ticket in nearby:
        valid = False
        for val in ticket:
            for field in fields:
                if field.in_range(val):
                    valid = True
                    break
 
    timeStop = time.perf_counter_ns()
    print(f"Runtime is {(timeStop - timeStart)/1000000} ms")


if __name__ == "__main__":
    main()
