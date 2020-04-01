def  summer (z):

# INTEGERS

    if (type(z[0]) == int):

        z1 = sum (z)
        z2 = len (z)
        print (z1)
        print (z2)


# STRINGS

    if (type (z [0]) == str):

        z1 = ""

        for i in range (len (z)):
            z1 += z [i]

        print (z1)


# BOOLEANS

    z = [True, True, True, False]

    if (type (z [0]) == bool):

        z1 = sum (z)
        z2= len (z)

        print (z1)
        print (z2)


def main ():

     summer ([1, 2, 3, 4])

     summer ( ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'])

     summer ([True, True, True, False])


main ()

