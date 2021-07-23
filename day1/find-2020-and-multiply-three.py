import time

def main():

    timeStart = time.perf_counter_ns()

    targetSum = 2020
    targetFound = False

    # Read the data into a list from the file
    f = open("input.txt")
    lines = f.readlines()
    f.close()
    numberList =[int(e.strip()) for e in lines]
    numberList.sort()

    #foreach number in the list
    for n in numberList:
        for m in numberList:
            for o in numberList:

                # Since this is sorted, we know that the remaining will only be bigger
                if n+m+o > targetSum:
                    break

                if n+m+o == targetSum:
                    print( str(n) + "+" + str(m) + "+" + str(o) + "=" + str(targetSum) + "; prod is " + str(n * m * o) )
                    targetFound = True
                    break

            if targetFound:
                break
        if targetFound:
            break
    else:
        print("No digits found that sum to " + str(targetSum))

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")


if __name__ == "__main__":
    main()
