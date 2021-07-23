import time
import re

class Passport:
    "Reads fields from input and determines if valid"

    def __init__(self):

        # Initialize passport fields as a dictionary
        keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
        self.fields = dict.fromkeys(keys, None)
        self.createInputRules()


    def addFields(self, dict):
        # Split the line based on spaces, and the k-v-p based on :
        self.fields.update(dict)

    def printFields(self):
        "Prints all fields as a dict"

        print(self.fields)

    def valid(self):
        "Tests that all required fields are present and follow rules"

        valid = True

        # Ensure all required are present
        required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for r in required:
            if self.fields[r] == None:
                valid = False

        # Check all rules
        for key, ruleset in self.rules.items():
            value = self.fields[key]
            if value:
                for rule_type, rule_value in ruleset.items():
                    if rule_type == "min":
                        if int(value) < rule_value: valid = False

                    if rule_type == "max":
                        if int(value) > rule_value: valid = False

                    if rule_type == "valid_values":
                        in_list = False
                        for x in rule_value:
                            if x == value: in_list = True
                        if not in_list: valid = False

                    if rule_type == "regex":
                        p = re.compile(rule_value)
                        if not p.search(value): valid = False

                    if rule_type == "regex-cm-range" or rule_type == "regex-in-range":
                        p = re.compile(rule_value[0])
                        m = p.match(value)
                        if m:
                            if int(m.group(1)) < rule_value[1]: valid = False
                            if int(m.group(1)) > rule_value[2]: valid = False


        return valid

    def createInputRules(self):

        self.rules = {}
        self.rules["byr"] = {"min": 1920, "max": 2002}
        self.rules["iyr"] = {"min": 2010, "max": 2020}
        self.rules["eyr"] = {"min": 2020, "max": 2030}
        self.rules["hgt"] = {"regex": '^[0-9]+cm|in$', "regex-cm-range": ['^([0-9]+)cm$', 150, 193], "regex-in-range": ['^([0-9]+)in$', 59, 76]}
        self.rules["hcl"] = {"regex": '^#[0-9a-fA-F]{6}$'}
        self.rules["ecl"] = {"valid_values": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]}
        self.rules["pid"] = {"regex": '^[0-9]{9}$'}




class Reader:
    "Reads the input file and returns a dict containing key value pairs"

    def __init__(self,file):
        self.f = open("input.txt")

    def readNext(self):

        self.dict = {}
        line = self.f.readline().strip()

        while line:
            # Split the line based on spaces, and the k-v-p based on :
            for pair in line.split(" "):
                x = pair.split(":")
                self.dict[x[0]]=x[1]

            line = self.f.readline().strip()

        return self.dict

    def getDict(self):
        return self.dict

    def cleanup(self):
        self.f.close()

def main():
    timeStart = time.perf_counter_ns()

    numValid = 0
    numInvalid = 0
    total = 0

    r = Reader("input.txt")

    while r.readNext():

        total += 1
        p = Passport()
        p.addFields(r.getDict())

        if p.valid():
            numValid += 1
        else:
            numInvalid += 1
        del p


    print("Valid passports: "+str(numValid))
    print("Invalid passports: "+str(numInvalid))
    print("Total passports: "+str(total))

    r.cleanup()

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")

if __name__ == "__main__":
    main()
