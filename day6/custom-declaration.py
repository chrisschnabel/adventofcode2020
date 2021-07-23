import time

class Reader:
    "Reads the input file and returns a list with elements for each person in group"

    def __init__(self):
        self.f = open("input.txt")

    def read_answers(self):

        self.answers = []
        line = self.f.readline().strip()

        while line:
            # Split the line based on spaces, and the k-v-p based on :
            self.answers.append(line)
            line = self.f.readline().strip()


        if self.answers:
            return True
        else:
            return False

    def get_answers(self):
        return self.answers

    def cleanup(self):
        self.f.close()

class Group_Declaration:
    """Takes a list of each person's answers.
    Returns a merged list or sum of their yes answers"""

    def __init__(self, input_list):

        self.anyone_declaration = ""
        self.everyone_declaration = {}
        self.group_sum = 0

        group_size = len(input_list)

        for x in input_list:
            for c in x:
                if c not in self.anyone_declaration: self.anyone_declaration += c
                if c in self.everyone_declaration:
                    self.everyone_declaration[c] += 1
                else:
                    self.everyone_declaration[c] = 1

        for v in self.everyone_declaration.values():
            if v == group_size: self.group_sum += 1


    def get_anyone_declaration(self):
        return self.anyone_declaration

    def get_anyone_yes_sum(self):
        return len(self.anyone_declaration)

    def get_everyone_yes_sum(self):
        return self.group_sum

def main():
    timeStart = time.perf_counter_ns()
    r = Reader()
    a_sum = 0
    e_sum = 0

    while r.read_answers():
        g = Group_Declaration(r.get_answers())
        a_sum += g.get_anyone_yes_sum()
        e_sum += g.get_everyone_yes_sum()

    print("anyone sum: "+str(a_sum))
    print("everyone sum: "+str(e_sum))


    r.cleanup()

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")

if __name__ == "__main__":
    main()
