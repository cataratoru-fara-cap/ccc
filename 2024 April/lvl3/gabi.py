import sys

""" my_file = sys.argv[1] """
my_file = "/home/lupulcelbun/Programing/ccc/ccc/lvl3/level3_example.in"

input = open(my_file, "r")

nr_splits = int(input.readline())# noqa number of splits
lawns = []

size = input.readline().strip()
lh = int(size.split()[1])
path = ""
while (True):
    lawn = []
    for i in range(lh):
        lawn.append(input.readline().strip())

    path = input.readline().strip()
    lawn.append(path)
    lawns.append(lawn)

    size = input.readline()
    if (size == ""):
        break
    lh = int(size.strip().split()[1])


# PARSING ENDS HERE
def check_path(matrix, path, start, L, H):
    valid = "NOT VALID"
    free_parcels = 0
    for i in range(L):
        for j in range(H):
            if (matrix[i][j] != "X"):
                free_parcels += 1

    if (len(path) != free_parcels):
        return "INVALID"

    for i in range(L):
        for j in range(H):
            V = matrix
            if (start == "X"):
                break

            x = start[0]
            y = start[1]

            for c in path:
                if c == "A":
                    x -= 1
                elif c == "D":
                    x += 1
                elif c == "W":
                    y += 1
                elif c == "S":
                    y -= 1

                if x > (L-1) or y > (H-1) or (x < 0) or (y < 0):
                    break
                elif (V[x][y] == "X"):
                    break
                else:
                    V[x][y] = "X"
            valid = "VALID"
            return valid









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