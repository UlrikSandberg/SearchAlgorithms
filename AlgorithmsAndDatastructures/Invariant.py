import math

def factorial(n):
    i = n
    r = 1
    while i > 1:
        if r == math.factorial(n):
            print "true"
        else:
            print "false"
        r = r * i
        i = i -1
    return r


def intergerlog(n):
    k = 0
    i = n
    while i >= 1:
        if i % 2 == 0:
            i = i / 2
            k = k + 1
        else:
            i = i - 1
    return k

def algoritme1(n):

    work1 = 0
    work2 = 0
    work3 = 0

    i = 1
    while i < n:
        work1 = work1 + 1
        j = i
        while j > 1:
            work2 = work2 + 1
            j = j / 2
        i = 2*i

    print work1
    print work2
    print work3


def invariant(n):
    x = 1
    r = 0
    if math.pow(2, r) == x:
        print "true"
    else:
        print "false"
    while x < n:
        x = 2 * x
        r = r + 1
        if math.pow(2, r) == x:
            print "true"
        else:
            print "false"
    return r

algoritme1(300)
#invariant(10)