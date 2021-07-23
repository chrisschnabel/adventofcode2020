
def main():


    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    test = dict.fromkeys(keys, None)

    print("'hgt' is in the dict as "+str(test["hgt"]))


if __name__ == "__main__":
    main()
