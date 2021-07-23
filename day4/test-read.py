
def main():


    dict = {}

    f = open("input.txt")
    line = f.readline().strip()
    line = f.readline().strip()
    line = f.readline().strip()

    # First test if line is empty, as that would indicate next Passport


    # Split the line based on spaces
    for pair in line.split(" "):
            x = pair.split(":")
            dict[x[0]]=x[1]

    print("byr is "+str(dict["byr"]))




if __name__ == "__main__":
    main()
