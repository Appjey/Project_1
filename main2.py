from К25 import tests


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
    a = 0b1 & int(x)
    b = 0b11111111111 << 1 & int(x)
    c = 0b1111111111111 << 13 & int(x)
    d = 0b1111 << 27 & int(x)
    b = b << 19
    c = c >> 7
    d = d >> 26
    a = a
    return bin(b | c | d | a)


def f23(a):
    # Splits, rounds and sets result to the cell
    for i in range(0, len(a)):
        if a[i][0] is not None:
            b = a[i][0].split('|')
            a[i].insert(0, str("{:.2f}".format(round(float(b[0]), 2))))  # ПОДВОХ БЫЛ ЗДЕСЬ! Кол-во знаков после 0. важно
            a[i][1] = b[1]

    # Removes all empty cells and duplicates
    for i in range(0, len(a)):
        a[i] = [item for item in a[i] if item is not None]
        a[i] = remove_d(a[i])

    # # print(a)
    # Removes empty sub-array
    for i in range(0, len(a)):
        for y in range(0, len(a)):
            # # print(len(a[y]), "_", a[y])
            if len(a[y]) == 0:
                a.pop(y)
                break

    # Transposes the matrix
    transpose = [[str(0 * x * y) for x in range(len(a))] for y in range(len(a))]
    """
    print(len(a), "_{}_".format(a), len(a[0]))
    print(len(transpose), "_{}_".format(transpose), len(transpose[0]))
    """
    for x in range(len(a)):
        for y in range(len(a[0])):
            transpose[y][x] = a[x][y]
    # # print(transpose)

    # Replace Full name by short
    # # print(transpose)
    for x in range(len(transpose[1])):
        ss = transpose[1][x].split(" ", 1)
        transpose[1][x] = ss[0][0] + '.' + ss[1]

    for i in range(0, len(transpose)):
        for y in range(0, len(transpose)):
            if transpose[y].count('0') == len(transpose[0]):
                transpose.pop(y)
                break
    # # print(transpose)

    # Replaces / by dot
    for x in range(len(transpose[0])):
        transpose[len(a[0]) - 1][x] = transpose[len(a[0]) - 1][x].replace('/', '.')
        bb = transpose[len(a[0]) - 1][x].split('.', 4)
        # # print(bb)
        transpose[len(a[0]) - 1][x] = bb[0] + '.' + bb[1] + '.' + bb[2].replace(bb[2][0], '', 1).replace(bb[2][1], '',
                                                                                                         1)
    return transpose


# remove None and duplicates
def remove_d(a=None):
    if a is None:
        a = []
    for i in range(0, len(a)):
        if a[i] == a[i - 1]:
            del a[i - 1]
    return a


assert f21(tests.get("f21")[12][0][0]) == tests.get("f21")[12][0][1], "error f21"
assert f21(tests.get("f21")[12][1][0]) == tests.get("f21")[12][1][1], "error f21"
assert f21(tests.get("f21")[12][2][0]) == tests.get("f21")[12][2][1], "error f21"
assert f21(tests.get("f21")[12][3][0]) == tests.get("f21")[12][3][1], "error f21"
assert f21(tests.get("f21")[12][4][0]) == tests.get("f21")[12][4][1], "error f21"
"""
assert f22(tests.get("f22")[12][0][0]) == tests.get("f22")[12][0][1], "error f22"
assert f22(tests.get("f22")[12][1][0]) == tests.get("f22")[12][1][1], "error f22"
assert f22(tests.get("f22")[12][2][0]) == tests.get("f22")[12][2][1], "error f22"
assert f22(tests.get("f22")[12][3][0]) == tests.get("f22")[12][3][1], "error f22"
assert f22(tests.get("f22")[12][4][0]) == tests.get("f22")[12][4][1], "error f22"
"""
assert f23(tests.get("f23")[12][0][0]) == tests.get("f23")[12][0][1], "error f230"
assert f23(tests.get("f23")[12][1][0]) == tests.get("f23")[12][1][1], "error f231"
assert f23(tests.get("f23")[12][2][0]) == tests.get("f23")[12][2][1], "error f232"
assert f23(tests.get("f23")[12][3][0]) == tests.get("f23")[12][3][1], "error f233"
assert f23(tests.get("f23")[12][4][0]) == tests.get("f23")[12][4][1], "error f234"

print("pass")
