first = "Hello, World!"
print("I AM A COMPUTER")
if 1 < 2 and 4 >2:
    print("Math is fun")
    nope = None
    bool_combo = True and False
    length = len("What's my length?")
    shouting = "i am shouting".upper()
    num =int("1000")
    combo = str(4) + "real"
    repeat = 3 * "cool"

    try:
        div_by_zero = 1 / 0
    except ZeroDivisionError as e:
        div_by_zero = e
    list_type = type([])
    name = input("What is your name? ")
    num_input = float(input("Enter a number: "))
    if num_input < 0:
        print("That number is less than 0!")
    elif num_input > 0:
        print("That number is greater than 0!")
    else:
        print("That number is 0!")

    index_1 = "apple".find("1")
    has_y = "y" in "xylophone"
    my_string = "some text"
    is_lower = my_string.islower()
    

