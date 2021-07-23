import time

class Passport:
    "Reads fields from input and determines if valid"

    def __init__(self):

        # Initialize passport fields as a dictionary
        keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
        self.fields = dict.fromkeys(keys, None)

    def addFields(self, line):

        # Split the line based on spaces, and the k-v-p based on :
        for pair in line.split(" "):
            x = pair.split(":")
            self.fields[x[0]]=x[1]

    def valid(self):
        "Tests that all required fields are present"

        required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for r in required:
            if self.fields[r] == None:
                return False
        return True


def main():
    timeStart = time.perf_counter_ns()
    numValid = 0
    numInvalid = 0
    total = 0
    newPassport = True

    with open("input.txt") as f:
        for line in f:

            if newPassport:
                total += 1
                p = Passport()
                newPassport = False


            l = line.strip()
            if l:
                p.addFields(l)
            else:
                newPassport = True
                print(p.fields)
                if p.valid():
                    numValid += 1
                else:
                    numInvalid += 1
                del p
    if p.valid():
        numValid += 1
    else:
        numInvalid += 1
    del p


    print("Valid passports: "+str(numValid))
    print("Invalid passports: "+str(numInvalid))
    print("Total passports: "+str(total))

    f.close()

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")

if __name__ == "__main__":
    main()
