NUM_ROWS = 128
NUM_COLS = 8
FRONT = 'F'
BACK = 'B'
LEFT = 'L'
RIGHT = 'R'


def binary_recurse(s, r, lower_char, upper_char):
    # print(f"seq - {s}, range is {r.start} to {r.stop}")
    if(len(s) == 1):
        return r.start if s[0] == lower_char else (r.stop - 1)
    midpoint = int( (r.stop + r.start) / 2 )
    if s[0] == lower_char:
        return binary_recurse(s[1:], range(r.start, midpoint), lower_char, upper_char)
    elif s[0] == upper_char:
        return binary_recurse(s[1:], range(midpoint, r.stop), lower_char, upper_char)

def calc_seat_id(encoding):
    row = binary_recurse(encoding[:-3], range(NUM_ROWS), FRONT, BACK)
    column = binary_recurse(encoding[-3:], range(NUM_COLS), LEFT, RIGHT)
    return row * 8 + column

def max_seat_id():
    m = 0
    with open('data/day_5_input.txt', 'r') as f:
        for line in f:
            seat_id = calc_seat_id(line[:-1])
            m = seat_id if seat_id > m else m
        return f"max calculated seat id {m}"

def find_my_seat():
    m = 0
    seats = []
    with open('data/day_5_input.txt', 'r') as f:
        for line in f:
            seat_id = calc_seat_id(line[:-1])
            seats.append(seat_id)
        seats.sort()

        for i in range(len(seats)):
            if seats[i+1] - seats[i] > 1:
                return f"Your seat id is {seats[i+1] - 1}"

print(max_seat_id())
print(find_my_seat())
