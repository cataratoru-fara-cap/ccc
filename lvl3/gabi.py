import sys

my_file = sys.argv[1]
input = open(my_file, "r")
lines = input.readlines()[1:]

output_file = sys.argv[2]
output = open(output_file, "w")

for line in lines:

    for c in line:
        if c == "A":

        elif c == "W":


        elif c == "S":


        elif c == "D":

    output.write(f"{L} {H}\n")

output.close()
