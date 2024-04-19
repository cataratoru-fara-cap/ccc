import sys

my_file = sys.argv[1]
input = open(my_file, "r")
lines = input.readlines()[1:]

output_file = sys.argv[2]
output = open(output_file, "w")

for line in lines:
    y_max, y_cur, y_min = 0, 0, 0
    x_max, x_cur, x_min = 0, 0, 0

    for c in line:
        if c == "A" and x_cur == x_min:
            x_cur -= 1
            x_min -= 1

        elif c == "W" and y_cur == y_max:
            y_cur += 1
            y_max += 1

        elif c == "S" and y_cur == y_min:
            y_cur -= 1
            y_min -= 1

        elif c == "D" and x_cur == x_max:
            x_cur += 1
            x_max += 1

        elif c == "A":
            x_cur -= 1

        elif c == "W":
            y_cur += 1

        elif c == "S":
            y_cur -= 1

        elif c == "D":
            x_cur += 1 

    H = y_max - y_min + 1
    L = x_max - x_min + 1

    output.write(f"{L} {H}\n")

output.close()
