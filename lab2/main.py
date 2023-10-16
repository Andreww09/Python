
import numpy as np

# ex0
def sum(n):
    # s=0
    # for i in range(n):
    #     s+=i
    # return s
    return n * (n - 1) / 2


#ex1
def codes(a, b):
    list = []

    for i in range(ord(a), ord(b) + 1):
        list += [hex(i)[2:]]
    return list


#ex2
def bytes(arr):
    str = ""
    nZero = 0
    nOne = 0
    for i in arr:
        byte = bin(i)[2:].rjust(8, '0')
        n = byte.count('0')
        nZero += n
        nOne += (8 - n)
        str += byte + " "

    return (str, nZero, nOne)


#ex3
def division(x, y):
    precision = 100
    rez = ""
    quot = x // y
    rez += str(quot) + ","
    for i in range(precision):
        x -= quot * y
        x *= 10
        quot = x // y
        rez += str(quot)
    return rez

# ex4
def solve_equation(eq):
    a = []
    b = []
    for i in range(0, len(eq)):
        a.append(eq[i][0: len(eq[i]) - 1])
        b.append(eq[i][len(eq[i]) - 1])
    return np.linalg.solve(a, b)


# ex5
def pascal(n, i): #calculeaza elementul de pe linia n, coloana i, din triunghiul lui Pascal
    x = 1
    for line in range(1, n + 2):
        x = 1
        for col in range(1, line + 1):
            if line == n + 1 and i == col - 1:
                return x
            x = int(x * (line - col) / col)

    return x


def compute_y(n, p, x):
    sum = 0
    for i in range(0, n):
        sum = sum + (10 ** i) * pascal(n, i) * (p ** i) * (x ** (n - i))
    return sum


def split_into_groups(number, n): #imparte numarul in grupe de cate n cifre
    number = float(number)
    x = str(number).split('.')

    while (len(x[0]) % n != 0): # completeaza grupele inainte de virgula
        x[0] = '0' + x[0]
    while (len(x[1]) % n != 0): # si dupa virgula
        x[1] = x[1] + '0'
    cut = int(len(x[0]) / 2)  # numarul de grupe de n cifre inainte de virgula
    x = x[0] + x[1]
    groups = [int(x[i:i + n]) for i in range(0, len(x), n)]

    return (groups, cut)


def nth_root(number, n):
    if n % 2 == 0 and number < 0:
        return "Wrong input"
    precision = 50
    groups, cut = split_into_groups(number, n)
    # print(groups)
    rez = 0
    rem = 0
    for i in range(0, precision):
        rem = rem * 100
        if i < len(groups):
            rem += groups[i]
        if rem == 0:
            break
        digit = 0
        y = compute_y(n, rez, digit)
        while y <= rem:
            digit = digit + 1
            y = compute_y(n, rez, digit)
        digit = digit - 1
        y = compute_y(n, rez, digit)
        rez = rez * 10 + digit
        rem = rem - y

    rez = str(rez)
    if (len(rez[cut:]) == 0):
        rez += '0'
    rez = rez[0:cut] + '.' + rez[cut:]
    return rez

#ex6
def nth_permutation(n, p, alphabet):
    n -= 1
    lg = len(alphabet)
    new_base = []
    while n:
        new_base.append(int(n % lg)) #transforma numarul n in baza lg=lungime alfabet
        n //= lg
    while len(new_base) < p: #completeaza cu 0 pana la lungimea p
        new_base.append(0)
    new_base.reverse()
    rez = ""
    # print(new_base)
    for i in new_base:
        rez += alphabet[i]
    return rez

#ex7
def convert_mat(a):
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            a[i][j] = bin(a[i][j])[2:].rjust(8, '0') # transforma in baza 2, sterge prefixul 0b si completeaza cu 0
    for i in range(0, len(a)):
        print(a[i])
    return a

#ex8
def compute_area(y):
    area = 0
    for i in range(0, len(y) - 1):
        area += (y[i] + y[i + 1]) / 2 # intre fiecare doua valori ale lui y se poate forma un trapez, adaugam aria acestuia
    return area


if __name__ == '__main__':
    print(sum(10))
    a='A'
    b='Z'
    print(codes(a,b))

    arr=[1,2,5,11]
    print(bytes(arr))

    print(division(2,4))

    print(solve_equation([[8, 3, -2, 9], [-4, 7, 5, 15], [3, 4, -12, 35]]))
    print(nth_root(8, 3))
    print(nth_permutation(7, 3, "ABCDEF"))

    a = [
        [0x00, 0x00, 0xFC, 0x66, 0x66, 0x66, 0x7C, 0x60, 0x60, 0x60, 0x60, 0xF0, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7E, 0x06, 0x0C, 0xF8, 0x00],
        [0x00, 0x00, 0x10, 0x30, 0x30, 0xFC, 0x30, 0x30, 0x30, 0x30, 0x36, 0x1C, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0xE0, 0x60, 0x60, 0x6C, 0x76, 0x66, 0x66, 0x66, 0x66, 0xE6, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x7C, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7C, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0xDC, 0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00, 0x00]
    ]
    convert_mat(a)

    print(compute_area([1, 2, 3, 4, 5, 6, 7, 7, 7]))

 

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
