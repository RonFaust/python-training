
def mpy(x, y):
    return x*y

def div(x, y):

    if (y ==0 ):
        print ('illegal params')
    else:
        return x/y


def main():

    num1 = mpy (7,8)
    print (num1)

    num2 = div (32,8)
    print (num2)

    num3 = div (32,0)
    print (num3)

main()

