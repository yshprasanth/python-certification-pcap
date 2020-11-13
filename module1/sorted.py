#  1.
d = {'one':1, 'three':3, 'two':2}
for k in sorted(d.values()):
    print(k, end=' ')

# 2. equal operator

# 3.
ls = [[c for c in range(r)] for r in range(3)]
for x in ls:
    if len(x)<2 :
        print('hi')

# 4
class A:
    A = 1
    def __init__(self):
        self.a = 0
print(hasattr(A,'A'))
print(hasattr(A,'a'))
a = A()
print(hasattr(a,'A'))
print(hasattr(a,'a'))

# 5.
def fun(d, k, v):
    d[k] = v

dc = {}
print(fun(dc, 'a','b'))

# 6.
def a(x):
    def b():
        return x+x
    return b

x = a('x')
y = a('')
print(x() + y())

# 7.
f = open('lists.py', 'r')
q = f.readlines()
print(q)

# 8.
def I(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s

for x in I(3):
    print(x)

# 9.
class A:
        def __init__(self):
            pass
        def f(self):
            return 1
        def g():
            # class level method, cannot invoke self.f()
            return self.f()

a = A()
# print(A.g())

# 10.
def f (par2, par1):
    return par2 + par1

# print(f(par2=1, 2)) // error

# 11.
# __pycache__ contains compiled .pyc files

# 12
x = """
"""
print(len(x))

# 13
print('a', 'b', 'c', sep="'")

# 14
t = (1, 2, 3, 4)
t = t[-2:-1]
print(t)
t = t[-1]
print(t)

# 15 
# package directory contain a file intended to initialize the package. 
# its name is __init__.py

# 16
print(len((1,)))

# 17
d = {}
d['2'] = [1, 2]
d['1'] = [3, 4]
print(d, d.keys(), d.values())
for x in d.keys():
    print(d[x][1], end=" ")

d = {}
d[2] = [1, 2]
d[1] = [3, 4]
print(d, d.keys(), d.values())
for x in d.keys():
    print(d[x][1], end=" ")

d = {}
d['2'] = [1, 2]
d['1'] = [3, 4]
print(d, d.keys(), d.values())
for x in sorted(d.keys()):
    print(d[x][1], end=" ")
print(d, d.keys(), d.values())

# 18
class A:
    def a(self):
        print("a")
        return "a"
class B(A):
    def a(self):
        print("b")
        return "b"
class C(A):
    def a(self):
        print("c")
        return "c"
class D(C, B):
    # def a(self):
    #     return super().a()

    def __str__(self):
        return self.a()

d = D()
print(issubclass(C, A) and issubclass(C , B), d, d.a())

# 19
i = 4

while i>0:
    i -= 2
    print("while-*")
    if i == 2:
        break
else:
    print("else-*")

# 20
str1 = 'string1'
str2 = str1[:]

print(str1, str2)

# 21
str = 'abcdef'
def funs1(s):
    del s[2]
    print(s)

# funs1(str) // error

# 22
class X1:
    pass
class Y1(X1):
    pass
class Z1(Y1):
    pass
x = X1()
z = Z1()
print(isinstance(x, Z1), isinstance(z, X1))

# 23
t = (1,)
t = t[0] + t[0]
print(t)

# 24
print(len([i for i in range(0, -2)]))

# 25
try:
    x = 1/0
except Exception as e:
    print(e.args) 
    #  args is a tuple

# 26
# sys.stdout is associated with screen
# sys.stdin in associated with keyboard

# 27
v = 1 + 1//2 + 1/2 + 2
print(v)

# 28
class A2:
    def __init__(self, name):
        self.name = name

a2 = A2("hi")
print(a2)

# 29
lt = [1, 2, 3, 4]
lt = list(map(lambda x: 2*x, lt))
print(lt)

# 30
class A3:
    def __init__(self, v):
        self._a = v + 1

a3 = A3(0)
print(a3._a)

# 31
f2 = open('lists.py', 'bw')
# f2.write()

# 32
class A4:
    A = 1
    def __init__(self, v=2):
        self.v = v + A4.A
        A4.A +=1

    def set(self, v):
        self.v += v
        A4.A +=1
        return

a4 = A4()
a4.set(2)
print(a4.v)

# 33
try:
    raise Exception
except BaseException:
    print('be')
else:
    print('else')
finally:
    print('finally')