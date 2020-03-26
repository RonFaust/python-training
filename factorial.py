
def factorial (x):

    y = 1

    while (x > 1):

        y *= x
        x -= 1

    return y

def main ():

    z = factorial (6)
    print (z)

main ()