import sys

""" my_file = sys.argv[1] """
my_file = "/home/lupulcelbun/Programing/ccc/ccc/lvl3/level3_example.in"

input = open(my_file, "r")

nr_splits = int(input.readline())# noqa number of splits
lawns = []
lawn = []

size = input.readline()
lh = int(size.split()[1])
path = ""
while (input):
    for i in range(lh):
        lawn.append(input.readline().strip())
    lawns.append(lawn)
    path = input.readline()

    size = input.readline()
    lh = int(size.split()[1])

print(lawns)
""" output_file = sys.argv[2]
output = open(output_file, "w")

for line in lines:

    for c in line:
        if c == "A":

        elif c == "W":


        elif c == "S":


        elif c == "D":

    output.write(f"{L} {H}\n")

output.close()
 """