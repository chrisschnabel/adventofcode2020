import time
import re


class Instruction:
    "Holds the instruction, which is a single line in the program"

    def __init__(self, instr):
        "Initializes the bag based on a tuple of color and set of bags inside"

        self.color = ""             # The color of the bag itself
        self.instr , self.value = instr

    def get_instruction(self):
        return self.instr

    def get_value(self):
        return self.value

    def toggle(self):
        "This will change a nop to a jmp, or jmp to a nop. it does nothing to an acc"

        instr = self.instr

        if instr == "nop": self.instr = "jmp"
        if instr == "jmp": self.instr = "nop"

class Program:
    "Contains a set of instructions that can be run."

    def __init__(self):
        self.line = 0
        self.accumulator = 0
        self.instructions = []      # instructions by line
        self.executions = []        # execution count by line

    def append_instruction(self, instr):
        "Used to build the instructions that make up the program"

        self.instructions.append(instr)
        self.executions.append(0)

    def run(self):
        "Runs the program based on instructions loaded, and returns accumulator"

        while self.line < len(self.instructions):
            # Immediately before the program would run an instruction a second time, return the accumulator
            if self.executions[self.line] > 0:
                return self.accumulator
            else:
                self.executions[self.line] += 1

            next_instr = self.instructions[self.line]
            if next_instr.get_instruction() == "nop":
                self.line +=1
            elif next_instr.get_instruction() == "jmp":
                self.line += next_instr.get_value()
            elif next_instr.get_instruction() == "acc":
                self.accumulator += next_instr.get_value()
                self.line +=1
            else:
                print("ERROR - instruction not found: "+str(next_instr.get_instruction()))

        print("Program finished running.")
        return self.accumulator

    def get_program_len(self):
        return len(self.instructions)

    def get_instruction(self,line):
        return self.instructions[line]

    def reset(self):
        self.line = 0
        self.accumulator = 0
        self.executions = [0] * len(self.instructions)

class Reader:
    "Reads the input file and returns a tuple of bag color and it's contents with read_next"

    def __init__(self):
        self.f = open("input.txt")


    def read_next(self):
        "Returns a tuple of instruction (string) and value (int)"

        line = self.f.readline().strip()

        if line:
            m = re.search("([a-z]+)\s([+\-0-9]+)", line)
            return (m.group(1), int(m.group(2)))

        else:
            return False

    def cleanup(self):
        self.f.close()

def main():
    timeStart = time.perf_counter_ns()

    # Create the program based on the input file
    r = Reader()    # Reader object used to iterate on file input
    p = Program()

    instr = r.read_next()

    while instr:
        i = Instruction(instr)
        p.append_instruction(i)
        instr = r.read_next()

    # part 1: accumulator before looping starts
    acc = p.run()
    print("Accumulator: "+str(p.accumulator))

    # information
    program_len = p.get_program_len()
    print("Program len: "+str(program_len))

    # Toggle every line of the program to see if it runs to the end.
    for n in range(program_len):
        print("attempt toggle on line "+str(n))
        p.get_instruction(n).toggle()
        p.run()
        if p.line >= program_len:
            print("Accumulator: "+str(p.accumulator))
            break
        else:
            # Toggle it back and let the loop proceed to try the next
            p.get_instruction(n).toggle()
            p.reset()




    r.cleanup()

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")

if __name__ == "__main__":
    main()
