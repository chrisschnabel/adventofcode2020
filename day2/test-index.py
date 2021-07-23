import re

def main():


    pos1 = 5
    pos2 = 11
    letter = "t"
    password = "glhbttzvzttkdx"

    count = 0
    if password[pos1-1] == letter: count += 1
    if password[pos2-1] == letter: count += 1

    print(str(count))



if __name__ == "__main__":
    main()
