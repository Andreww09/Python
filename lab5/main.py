class Stack:
    def __init__(self):
        self.el = []

    def push(self, x):
        self.el.append(x)

    def pop(self):
        if len(self.el) == 0:
            return None
        return self.el.pop(len(self.el) - 1)

    def peek(self):
        if len(self.el) == 0:
            return None
        return self.el[len(self.el) - 1]

    def empty(self):
        if len(self.el) == 0:
            return True
        return False


class Queue:
    def __init__(self):
        self.el = []

    def push(self, x):
        self.el = self.el + [x]

    def pop(self):
        if len(self.el) == 0:
            return None
        x = self.el[0]
        self.el = self.el[1:]
        return x

    def peek(self):
        if len(self.el) == 0:
            return None
        return self.el[0]

    def empty(self):
        if len(self.el) == 0:
            return True
        return False


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.a = [[0] * m for i in range(0, n)]

    def get(self, x, y):
        return self.a[x][y]

    def set(self, x, y, val):
        self.a[x][y] = val

    def get_n(self):
        return self.n

    def get_m(self):
        return self.m

    def transpose(self):
        transposed = Matrix(self.m, self.n)
        for i in range(0, self.n):
            for j in range(0, self.m):
                transposed.set(j, i, self.a[i][j])
        return transposed

    def multiplication(self, b):
        if self.m != b.get_n():
            return None
        result = Matrix(self.n, b.get_m())
        for i in range(0, self.n):
            for j in range(0, b.get_m()):
                sum = 0
                for k in range(0, self.m):
                    sum += self.a[i][k] * b.get(k, j)
                result.set(i, j, sum)
        return result

    def transform(self, f):
        for i in range(0, self.n):
            for j in range(0, self.m):
                self.a[i][j] = f(self.a[i][j])

    @staticmethod
    def create_instance(a):
        if len(a) == 0:
            return Matrix(0, 0)
        result = Matrix(len(a), len(a[0]))
        for i in range(0, len(a)):
            for j in range(0, len(a[0])):
                result.set(i, j, a[i][j])
        return result

    def print(self):
        for i in range(0, self.n):
            for j in range(0, self.m):
                print(self.a[i][j], end=" ")
            print()


#
# stack=Stack()
# stack.push(1)
# stack.push(2)
# while stack.empty() is False:
#     print(stack.peek())
#     print(stack.pop())
# print(stack.peek())
# print(stack.pop())


# queue=Queue()
# queue.push(1)
# queue.push(2)
# queue.push(3)
# while queue.empty() is False:
#     print(queue.peek())
#     print(queue.pop())
# print(queue.peek())
# print(queue.pop())


a = Matrix(2, 3)
a.set(0, 0, 1)

print(a.get(1, 1))
a.print()
b = a.transpose()
b.print()
print()

m1 = [
    [1, 2, 3],
    [4, 5, 6]
]
m2 = [
    [10, 11],
    [20, 21],
    [30, 31],
]
c = Matrix.create_instance(m1)
d = Matrix.create_instance(m2)
e = c.multiplication(d)
e.print()

c.transform(lambda x: x + 1)
c.print()
