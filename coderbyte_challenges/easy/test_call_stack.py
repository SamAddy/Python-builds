import sys

from showcallstack import showcallstack


def bar(a):
    a = a - 1
    print_me_something()
    showcallstack()
    return a


def foo(a):
    a = a * a
    b = bar(a)
    return b


def print_me_something():
    print("Just here to print you something:)")


def spring():
    x = 6
    foo(x)
    print("Done")


spam = 'SPAM!'

xyz = "Spring Onion here"
size_in_bytes = sys.getsizeof("x")
st = 'book'
st2 = st.split()
print(xyz)

spring()

clr = object()
bob = 9
print("The ref count to object clr : ", sys.getrefcount(clr))
print("The ref count to object int 9 : ", sys.getrefcount(bob))
print("The ref count to object str 'book' : ", sys.getrefcount(st2))
print(st2)
print(size_in_bytes)
