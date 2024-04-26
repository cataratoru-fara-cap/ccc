import sys

my_file = sys.argv[1]
input = open(my_file, "r")
lines = input.readlines()[1:]

output_file = sys.argv[2]
output = open(output_file, "w")

for line in lines:
    a, w, s, d = 0, 0, 0, 0

    for c in line:
        if c == "A":
            a += 1
        elif c == "W":
            w += 1
        elif c == "S":
            s += 1
        elif c == "D":
            d += 1

    output.write(f"{w} {d} {s} {a}\n")

output.close()
