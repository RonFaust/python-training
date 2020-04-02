
def main():

    number = input ('Please enter a 5 digits number\n')

    digit0 = number [0]
    digit1 = number [1]
    digit2 = number [2]
    digit3 = number [3]
    digit4 = number [4]

    prefix_1 = 'You entered the number: '

    print ('{}' '{}'.format (prefix_1, number))

    prefix_2 = 'The digits of the number are: '

    coma = " , "

    print ('{}' '{}' '{}' '{}' '{}' '{}' '{}' '{}' '{}' '{}'.format (prefix_2,  digit0, coma, digit1, coma, digit2, coma, digit3, coma, digit4))

    prefix_3 = 'The sum of the digits is: '

    digits_sum = int(digit0) + int(digit1) + int(digit2) + int(digit3) + int(digit4)

    print ('{}' '{}'.format (prefix_3, digits_sum))


    int_number = int(number)

main()