
print(':)')


def add(x,y):
    v = x + y
    return v

def mul(x,y):
    v = x * y
    return v

def op(f, x, y):
    return f(x,y)

print('add(2,3) =', add(2,3))
print('mul(2,3) =', mul(2,3))

print('op(add, 2, 3) =', op(add, 2, 3))
print('op(mul, 2, 3) =', op(mul, 2, 3))