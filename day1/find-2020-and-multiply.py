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

    # numberList = [1721, 979, 366, 2050, 299, 675, 1456]

    #TODO - test if sorting speeds things up or not
    #numberList.sort()

    #foreach number in the list
    for n in numberList:
        for m in numberList:
            print(str(n+m))
            if n+m == targetSum:
                print( str(n) + " and " + str(m) + " sum to " + str(targetSum) + " with product " + str(n * m) )
                targetFound = True
                break
        if targetFound:
            break
    else:
        print("No digits found that sum to " + str(targetSum))

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")


if __name__ == "__main__":
    main()
