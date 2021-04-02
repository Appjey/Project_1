def f21(a):
    if a[4] == 1966:
        return 12
    if a[4] == 1975:
        return 11
    if a[4] == 1991:
        if a[2] == 1993:
            if a[3] == 2016:
                if a[1] == 'pike':
                    return 0
                if a[1] == 'haml':
                    return 1
            if a[3] == 2008:
                if a[1] == 'pike':
                    return 2
                if a[1] == 'haml':
                    return 3
            if a[3] == 1969:
                if a[1] == 'pike':
                    return 4
                if a[1] == 'haml':
                    return 5
        if a[2] == 1998:
            if a[3] == 2016:
                return 6
            if a[3] == 2008:
                if a[0] == 2009:
                    return 7
                if a[0] == 1976:
                    return 8
                if a[0] == 1973:
                    return 9
            if a[3] == 1969:
                return 10
    return 0

def f22(x):
    a = x & 0b00000000000000000000000000000001
    b = x & 0b00000000000000000011111111111110
    c = x & 0b00001111111111111110000000000000
    d = x & 0b11111000000000000000000000000000
    b = b << 19
    c = c >> 7
    d = d >> 26
    a = a
    return hex(b|c|d|a)

def f23(a):
    # Splits, rounds and sets result to the cell
    for i in range(0, len(a)):
        if a[i][0] is not None:
            b = a[i][0].split('|')
            a[i].insert(0, str(round(float(b[0]), 2)))
            a[i][1] = b[1]

    # Removes all empty cells and duplicates
    for i in range(0, len(a)):
        a[i] = [item for item in a[i] if item is not None]
        a[i] = remove_d(a[i])

    # Removes empty sub-array
    for i in range(len(a[0])):
        for y in range(len(a)):
            if not a[y]:
                del a[y]
                break

    # Transposes the matrix
    transpose = [[a[y][x] for y in range(len(a))] for x in range(len(a[0]))]

    #Replace Full name by short
    for x in range(len(transpose[1])):
        ss = transpose[1][x].split(" ", 1)
        transpose[1][x] = ss[0][0] + '.' + ss[1]

    # Replaces / by dot
    for x in range(len(transpose[0])):
        transpose[len(a) - 1][x] = transpose[len(a) - 1][x].replace('/', '.')
        bb = transpose[len(a) - 1][x].split('.', 3)
        transpose[len(a) - 1][x] = bb[0] + '.' + bb[1] + '.' + bb[2].replace(bb[2][0], '', 1).replace(bb[2][1], '', 1)
    return transpose

# remove None and duplicates
def remove_d(a=None):
    if a is None:
        a = []
    for i in range(0, len(a)):
        if a[i] == a[i - 1]:
            del a[i - 1]
    return a
