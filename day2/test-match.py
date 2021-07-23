import re

def main():

    line = "5-11 t: glhbttzvzttkdx"

    p = re.compile('^(?P<min>\d+)-(?P<max>\d+)\s(?P<letter>[a-z]):\s(?P<password>[a-z]+)')
    m = p.match(line)

    print("min is "+m.group('min'))
    print("max is "+m.group('max'))
    print("letter is "+m.group('letter'))
    print("password is "+m.group('password'))

if __name__ == "__main__":
    main()
