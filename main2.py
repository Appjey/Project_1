import numpy as np
import webbrowser


def task21(a, b, c, d, e):
    if e == 1966:
        return 12
    if e == 1975:
        return 11
    if e == 1991:
        if c == 1993:
            if d == 2016:
                if b == 'pike':
                    return 0
                if b == 'haml':
                    return 1
            if d == 2008:
                if b == 'pike':
                    return 2
                if b == 'haml':
                    return 3
            if d == 1969:
                if b == 'pike':
                    return 4
                if b == 'haml':
                    return 5
        if c == 1998:
            if d == 2016:
                return 6
            if d == 2008:
                if a == 2009:
                    return 7
                if a == 1976:
                    return 8
                if a == 1973:
                    return 9
            if d == 1969:
                return 10
    return 0


def task23(a):
    # Splits, rounds and sets result to the cell
    for i in range(0, len(a)):
        if a[i][0] is not None:
            b = a[i][0].split('|')
            a[i][0] = round(float(b[0]), 2)
            a[i][1] = b[1]

    # Removes all empty cells and duplicates
    for i in range(0, 3 + 1):
        a[i] = [item for item in a[i] if item is not None]
        a[i] = remove_d(a[i])

    # Removes empty sub-array
    for y in range(len(a)):
        if not a[y]:
            del a[y]
            break
    # Transposes the matrix
    transpose = [[a[y][x] for y in range(len(a))] for x in range(len(a[0]))]

    # Replaces / by dot
    for x in range(len(transpose[0])):
        transpose[len(a) - 1][x] = transpose[len(a) - 1][x].replace('/', '.')
        bb = transpose[len(a) - 1][x].split('.', 3)
        transpose[len(a) - 1][x] = bb[0] + '.' + bb[1] + '.' + bb[2].replace(bb[2][0], '', 1).replace(bb[2][1], '', 1)
    return transpose


# remove None and duplicates
def remove_d(a=[]):
    for i in range(0, len(a)):
        if a[i] == a[i - 1]:
            del a[i - 1]
    return a


print(task21(2009, 'haml', 1993, 2008, 1991))
print(task21(1973, 'pike', 1993, 1969, 1966))
print(task23([['0.608|Айдар З. Цодберг', None, None, '25/04/2000', '25/04/2000'],
              [None, None, None, None, None],
              ['0.460|Марат В. Засуфин', None, None, '19/12/1999', '19/12/1999'],
              ['0.924|Арсен Л. Сикко', None, None, '20/02/2001', '20/02/2001']]))
print(task23([['0.751|Артур С. Шувев', None, None, '09/03/2002', '09/03/2002'],
              [None, None, None, None, None],
              ['0.453|Михаил У. Буцук', None, None, '04/07/2002', '04/07/2004'],
              ['0.952|Ростислав И. Римов', None, None, '28/11/2004', '28/11/2004']]))
