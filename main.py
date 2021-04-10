import math


def f11(x, y, z):
    a = math.sin(pow(y, 2) + 24 * pow(z, 8)) - pow(math.e, z)
    b = pow(x, 2) - pow(z, 6)
    c = math.log(y) - 22 * pow(x, 4) - 53
    d = 5 * pow(x, 4) - y / 32
    e = 27 * pow(x, 5) + math.log(x)
    result = math.sqrt(a) + math.sqrt(b / c) - d / e
    return result


def f12(x):
    if x < 173:
        return function1(x)
    if (x >= 173) and (x < 184):
        return function2(x)
    if (x >= 184) and (x < 241):
        return function3(x)
    if (x >= 241) and (x < 338):
        return function4(x)
    if x >= 338:
        return function5(x)


def f13(n, m):
    return sum1(1, 1, n, m) - 85 * sum2(1, n)


def f14(n):
    a = 0.0
    b = 0.0
    result = 0
    if n == 0:
        result = 4
    if n == 1:
        result = 6
    if n > 1:
        a = a + (1 / 76) * f14(n - 1) ** 3
        b = b + math.tan(f14(n - 2))
        result = a - b
    return result


def function1(x):
    return math.log(50 * pow(x, 7) + pow(x, 4)) + math.fabs(pow(math.e, x))


def function2(x):
    return 70 * pow(x, 5) + pow(x, 8)


def function3(x):
    return math.log(math.sin(x) - 59 * pow(x, 6)) - pow(x, 4) - 48


def function4(x):
    return 27 * x + math.log(x) - 78


def function5(x):
    return pow(pow(x, 7) / 38 + x, 4) + pow(x, 5)


def sum1(i, j, n, m):
    result = 0.0
    for x in range(i, n + 1):
        for y in range(j, m + 1):
            result = result + (math.log(x) + pow(y, 3))
    return result


def sum2(i, n):
    result = 0.0
    for x in range(i, n + 1):
        result = result + (pow(x, 6) / 89 + 41 * pow(x, 5))
    return result


print(f11(35, 70, -44))
print(f12(144))
print(f13(18, 96))
print(f"{f14(6):.2e}")
