
def main():

    previous_term = 1
    next_term = 2

    print(previous_term)
    print(next_term)

    while True:

        save_next_term = next_term
        next_term = next_term + previous_term
        previous_term = save_next_term

        if (next_term < 10000):
            print (next_term)
        else:
            break








main()