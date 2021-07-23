import time
import re

def main():

    timeStart = time.perf_counter_ns()

    validPasswordCount = 0

    # Create the pattern to match each line of the file to
    p = re.compile('^(?P<min>\d+)-(?P<max>\d+)\s(?P<letter>[a-z]):\s(?P<password>[a-z]+)')

    # Read the data from file one line at a time
    f = open("input.txt")
    while True:
        line = f.readline()
        if not line:
            break

        m = p.match(line)

        # Count the frequency of the letter in question
        count = 0
        for i in m.group('password'):
            if i == m.group('letter'):
                count += 1

        # Check to the bounds
        if (count>=int(m.group('min'))) and (count<=int(m.group('max'))):
                validPasswordCount += 1


    print("Found "+str(validPasswordCount)+" valid passwords.")
    f.close()



    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")

if __name__ == "__main__":
    main()
