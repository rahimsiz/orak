__author__ = 'ramil'

def max(a,b = 0):
    if a>b:
        return a
    else:
        return b

print max(10, 20)
max(2)
print max(a = 20)
print max(a = 10, b = 20)
print max(10, b = 5)
max()