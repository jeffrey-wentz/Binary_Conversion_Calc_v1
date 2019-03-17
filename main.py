import math_functions


while True:
    # calls functions from math_functions to get the user's input and
    # determine the conversion type
    num = math_functions.get_num()
    conversion_type = math_functions.get_conversion(num)

    # Conversion from binary to decimal
    if conversion_type == "decimal":
        print("Please wait while we convert " + str(num) + " to decimal.")
        math_functions.binary_to_decimal(num)
    # Conversion from decimal to binary
    elif conversion_type == "binary":
        print("Please wait while we convert " + str(num) + " to binary.")
        math_functions.decimal_to_binary(num)
        print("")
    else:
        print("ERROR: CONVERSION TYPE INVALID")

    # checks to see if the user wishes to continue
    cont = input("Would you like to run again?: ")
    if cont.lower() in ("no", "n", 0):
        print("\nThanks for using my conversion calculator! :)")
        break
