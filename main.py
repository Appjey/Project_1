import math

def task11(x, y, z):
    a = math.sin(pow(y, 2) + 24 * pow(z, 8)) - pow(math.e, z)
    b = pow(x, 2) - pow(z, 6)
    c = math.log(y) - 22 * pow(x, 4) - 53
    d = 5 * pow(x, 4) - y/32
    e = 27 * pow(x, 5) + math.log(x)
    result = math.sqrt(a) + math.sqrt(b/c) - d/e
    print(f"{result:.2e}")

def task12(x):
    if x < 173:
        print(f"{function1(x):.2e}")
    if (x >= 173) and (x < 184):
        print(f"{function2(x):.2e}")
    if (x >= 184) and (x < 241):
        print(f"{function3(x):.2e}")
    if (x >= 241) and (x < 338):
        print(f"{function4(x):.2e}")
    if x >= 338:
        print(f"{function5(x):.2e}")

def function1(x):
    return math.log(50 * pow(x, 7) + pow(x, 4)) + math.fabs(pow(math.e, x))

def function2(x):
    return 70 * pow(x, 5) + pow(x, 8)

def function3(x):
    return math.log(math.sin(x) - 59 * pow(x, 6)) - pow(x, 4) - 48

def function4(x):
    return 27 * x + math.log(x) - 78

def function5(x):
    return pow(pow(x, 7)/38 + x, 4) + pow(x, 5)

task11(35,70,-44)
task12(144)