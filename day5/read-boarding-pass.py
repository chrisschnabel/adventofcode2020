import time
import re

class Boarding_Pass:
    "Converts things"

    def __init__(self):
        None

    def input_chars(self, input):
        self.chars = input
        self.convert_chars()

    def convert_chars(self):

        # Calculate the row knowing F and B really are just 0 and 1 respectively
        #print(self.chars)
        p = re.compile("^([FB]+)([LR]+)$")
        m = p.match(self.chars)

        row = m.group(1).replace("F", "0")
        row = row.replace("B", "1")
        row = int(row,2)
        self.row = row
        #print("row: "+str(row))

        # Calculate the seat, but using L and R instead
        col = m.group(2).replace("L", "0")
        col = col.replace("R", "1")
        col = int(col,2)
        self.col = col
        #print("col: "+str(col))

        # Calculate seat_id
        self.seat_id = self.row * 8 + self.col
        #print("seat_id: "+str(self.seat_id))

    def get_seat_id(self):
        return self.seat_id

def main():
    timeStart = time.perf_counter_ns()

    max_seat_id = 0
    seat_id_list = []

    for line in open("input.txt"):
        c = Boarding_Pass()
        c.input_chars(line.strip())
        seat_id = c.get_seat_id()
        if seat_id > max_seat_id: max_seat_id = seat_id
        seat_id_list.append(seat_id)

    seat_id_list.sort()

    missing = []
    last = seat_id_list.pop()
    while seat_id_list:
        current = seat_id_list.pop()
        if last - current > 1: missing.append([current, last])
        last = current

    print(missing)


    print("max: "+str(max_seat_id))

    timeStop = time.perf_counter_ns()
    print(f"Runtime is {timeStop - timeStart} ns")


if __name__ == "__main__":
    main()
