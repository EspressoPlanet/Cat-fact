def phone_number():
    print("Enter phone to be texted here. Please note this is limited to US numbers")
    num_in1 = input('Enter zip code:  ')
    num_in2 = input('Enter first 3 digits: ')
    num_in3 = input('Enter last four digits: ')
    num = '(' + num_in1 + ') ' + num_in2 + '-' + num_in3

    return num

