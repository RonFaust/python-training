
def main():

    for i in range(100):

        if ((i % 7) == 0) or ((i % 10) == 7) or ((i - (i % 10)) == 70):
            print (i)

main()