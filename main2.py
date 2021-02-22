import numpy as np


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


def task23():
    a = np.array([['0.608|Айдар З. Цодберг', None, None, '25/04/2000', '25/04/2000'],
                     [None, None, None, None, None],
                     ['0.608|Айдар З. Цодберг', None, None, '25/04/2000', '25/04/2000'],
                     ['0.608|Айдар З. Цодберг', None, None, '25/04/2000', '25/04/2000']])
    np.delete(a, None)
    return a


print(task21(2009, 'haml', 1993, 2008, 1991))
print(task21(1973, 'pike', 1993, 1969, 1966))
print(task23())
