# import math


def binary_to_decimal(num):
    ''' First Attempt
    result = 0
    for index in range(0, len(str(num))+1):
        print("first_index: " + str(index) + "str(num)[::-(index+1)]: " + str(num)[::-(index+1)])
        if str(num)[::-(index+1)] == '1':
            print("index: " + str(index) + "str(num)[::-(index+1)]: " + str(num)[::-(index+1)])
            result = result + math.pow(2, int(index))
    print(str(num) + " converted to decimal is: " + str(result))
    '''

    # cite: iCodez on stackoverflow
    result = 0
    # iterates through each digit in the string submitted by user starting with
    for digit in str(num):
        result = result * 2 + int(digit)
    print(str(num) + " converted to decimal is: " + str(result))


# cite: www.programiz.com
# may come back in the future if I want to do my own algorithm
def decimal_to_binary(num):
    # Function to print binary number for the input decimal using recursion
    if num > 1:
        decimal_to_binary(num // 2)
    print(num % 2, end='')


# this function gets the number from the user and verifies it is an integer
def get_num():
    num = "NAN"
    while num == "NAN":
        try:
            num = int(input("Please enter the value you wish to be converted: "))
            return num
        # if a value is not an integer
        except ValueError:
            print("Value must be either a decimal or binary!")


# this function loops through the number to see if the user has entered a binary or decimal number
def check_decimal(num):
    binary = True
    for i in str(num):
        # checks if a digit contains only 1 or 0
        if i in '10':
            binary = True
        else:
            binary = False
            break

    return binary


# input: num
# return: conversion_type
# this function takes the user's number then checks to see if it is binary (containing only 1 and 0. If so,
#   user is prompted to determine if they truly wish to convert to decimal on the off chance they entered a
#   decimal containing only 1 and 0.
def get_conversion(num):
    binary = check_decimal(num)

    # if num contains only 1 and 0 then verify if user wants to convert to decimal or binary.
    if binary:
        conversion_type = input("Would you like to convert to decimal?: ")
        if conversion_type.lower() in ("no", "n", 0):
            conversion_type = "binary"
        else:
            conversion_type = "decimal"
    # Else number entered was a decimal and may only be converted to binary.
    else:
        conversion_type = "binary"

    return conversion_type
