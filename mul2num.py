
def  mul2num (x, y):

    z = x * y

    if (z > 0):

        return z
    else:
        return 0

def main ():

    x1 = 8
    x2 = 7

    z1 = mul2num (x1, x2)
    print (z1)

    x3 = 8
    x4 = -7

    z2 = mul2num (x3, x4)
    print (z2)

main ()