

# Press the green button in the gutter to run the script.
# ex1
def fibonacci_list(n):
    list = [1, 1]
    for i in range(2, n):
        list.append(list[i - 2] + list[i - 1])
    return list


# ex2
def is_prime(n):
    if n == 0 or n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def prime_list(list):
    prime = [list[i] for i in range(0, len(list)) if (is_prime(list[i]) == True)]
    return prime


# ex3
def intersection(a, b):
    return [el for el in a if el in b]


def union(a, b):
    c = a.copy()
    for el in b:
        if (el in c) == False:
            c.append(el)
    return c


def difference(a, b):
    return [el for el in a if (el in b) == False]


# ex4
def create_song(notes, moves, poz):
    song = [notes[poz]]
    for i in range(0, len(moves)):
        poz += moves[i]  # se adauga noua mutare la indiele de pozitie
        poz %= len(notes)  # ne asiguram ca pozitie e mereu intre 0 si lungimea totala
        song.append(notes[poz])
    return song


# ex5
def change_mat(a):
    for i in range(0, len(a)):
        for j in range(0, i):
            a[i][j] = 0
    return a


# ex6
def count_occurences(*args):
    list = []
    dict = {}
    x = args[len(args) - 1]
    for i in range(0, len(args) - 1):
        for j in args[i]:
            if j in dict:
                dict[j] = dict[j] + 1
            else:
                dict[j] = 1
    for key, value in dict.items():
        if value == x:
            list.append(key)
    return list


# ex7
def is_palindrome(x):
    a = x;
    inv = 0;
    while a:
        inv = inv * 10 + a % 10
        a //= 10
    if inv == x:
        return True
    return False


def count_palindromes(list):
    max = 0
    palindromes = []
    for i in list:
        if is_palindrome(i):
            palindromes.append(i)
            if (i > max):
                max = i
    if list == [] or len(palindromes) == 0:
        return (0, None)
    return (len(palindromes), max)


# ex8
def count_char(x, list, flag=True):
    rez = []
    for str in list:
        rez.append([])  # se adauaga o noua lista
        for i in range(0, len(str)):
            if flag and ord(str[i]) % x == 0:  # caractereke divizibile cu x
                rez[len(rez) - 1].append(str[i])
            if not flag and ord(str[i]) % x == 1:
                rez[len(rez) - 1].append(str[i])
    return rez


# ex9
def count_spectators(a):
    rez = []
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            for k in range(0, i):
                if a[k][j] >= a[i][j]:
                    rez.append((i, j))
                    break
    return rez


# ex10
def create_tuples(*args):
    rez = []
    for j in range(0, len(args)):
        list = args[j]
        for i in range(0, len(list)):
            if i + 1 > len(rez): # se adauga o noua lista pentru noua pozitie
                rez.append([])
            while len(rez[i]) < j: # se completeaza cu None pana la indicele listei curente
                rez[i].append(None)
            rez[i].append(list[i])  # se adauga caracterul i la lista cu numarul i
    for i in range(0, len(rez)):
        while len(rez[i]) < len(rez[0]):    # se completeaza toate listele cu None pana au aceeasi dimensiune
            rez[i].append(None)
        rez[i] = tuple(rez[i])
    return rez


# ex11


def order_tuple(list):
    rez = sorted(list, key=lambda x: x[1][2])
    return rez


# ex12
def group_by_rhyme(words):
    rez = []
    dict = {}
    for i in range(0, len(words)):
        rhyme = words[i][-2:]
        if rhyme not in dict:
            dict[rhyme] = [words[i]]
        else:
            dict[rhyme].append(words[i])
    for values in dict.values():
        rez.append(values)
    return rez


if __name__ == '__main__':
    # print(fibonacci_list(10))
    # print(prime_list([1, 2, 3, 4, 5, 6, 7, 8]))
    # a=[1,3,5,8,9]
    # b=[2,4,6,8,9]
    # print(intersection(a,b))
    # print(union(a,b))
    # print(difference(a,b))
    # print(difference(b,a))
    #
    # print(create_song(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    #
    # mat = [
    #     [1,2,3],
    #     [4,5,6],
    #     [7,8,9]
    # ]
    # print(change_mat(mat))
    # print(count_occurences([1,2,3], [2,3,4],[4,5,6], [4,1, "test"],2))
    # print(count_palindromes([1,12,121]))
    # print(count_char(2,["test", "hello", "lab002"],False))
    # print(count_spectators([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))
    # print(create_tuples([1,2,3], [5,6,7,8], ["a", "b", "c"]))
    # print(order_tuple([('abc', 'bcd'), ('abc', 'zza')]))
    print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
