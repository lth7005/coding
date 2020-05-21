#이영호 교수님 피드백-코딩

def print_root(a, b, c):
    D = b**2 - 4*a*c
    if D==0:
        r1 = (-b + D ** 0.5) / (2 * a)
        print('중근:',r1)
    elif D>0:
        r1 = (-b + D ** 0.5) / (2 * a)
        r2 = (-b - D ** 0.5) / (2 * a)
        print('해는',r1, '또는', r2)
    else:
        print('허근 (-{} + {} i )/{}'.format(b,-D,2*a))
        print('허근 (-{} - {} i )/{}'.format(b,-D,2*a))
print_root(1, 4, 4)
print_root(1, -6, 5.2)
print_root(1,1,1)
