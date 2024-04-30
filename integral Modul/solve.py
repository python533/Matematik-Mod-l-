pi=3,14

def cube(x):
    return x*x*x
    lambda_cube=lambda  x:x*x*x


def factorial(a):
    for y in range(0,100):
        a *=y
        print(a)

def sqrt(x):
    for y in range(0,100):
        if y % 2 == 0:
            continue
        karekok=y **0.5
        print(karekok)

def matris(x):
    dizi=[]
    for y in range(0,1000):
        if y % 2==0:
            continue
        elif y % 2 !=0:
            continue
        else:
            dizi.append(y)

