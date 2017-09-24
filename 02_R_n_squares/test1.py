import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break
    num_array = line.split()
    R = float(num_array[0])
    n = int(num_array[1])

    n16 = n / 16
    n8 = n / 8
    n4 = n / 4
    n2 = n / 2

    need16 = n16 - 0
    need8 = n8 - 2 * n16
    need4 = n4 - 2 * n8
    need2 = n2 - 2 * n4

    rest = n - (16 * need16 + 8 * need8 + 4 * need4 + 2 * need2)

    R2 = 1
    R4 = 1
    R8 = 1
    R16 = 1

    if n >= 2:
        R2 = R * R
    if n >= 4:
        R4 = R2 * R2
    if n >= 8:
        R8 = R4 * R4
    if n >= 16:
        R16 = R8 * R8

    result = 1
    if need16 > 0:
        result *= R16
    if need8 > 0:
        result *= R8
    if need4 > 0:
        result *= R4
    if need2 > 0:
        result *= R2
    if rest > 0:
        result *= R

    result_v = 1
    for i in range(n):
        result_v *= R

    print result

    print result_v
