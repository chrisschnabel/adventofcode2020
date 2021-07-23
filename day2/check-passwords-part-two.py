import time
import re

def main():

    timeStart = time.perf_counter_ns()

    validPasswordCount = 0

    # Create the pattern to match each line of the file to
    p = re.compile('^(?P<pos1>\d+)-(?P<pos2>\d+)\s(?P<letter>[a-z]):\s(?P<password>[a-z]+)')

    # Read the data from file one line at a time
    f = open("input.txt")
    while True:
        line = f.readline()
        if not line:
            break

        m = p.match(line)

        # Count the frequency of the letter in question
        count = 0

        password = m.group('password')
        letter = m.group('letter')

        if password[int(m.group('pos1'))-1] == letter: count += 1
        if password[int(m.group('pos2'))-1] == letter: count += 1

        # Check to the bounds
        if count == 1: validPasswordCount += 1


    print("Found "+str(validPasswordCount)+" valid passwords.")
    f.close()



    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")

if __name__ == "__main__":
    main()
