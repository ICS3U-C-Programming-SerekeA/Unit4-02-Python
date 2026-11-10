#!/usr/bin/env python3
# Created by: Sereke Asfeday 
# Created on: 10, November, 2026
# This program asks user for whole numbers and then
#  calculates the factorial of that number.


def main():

    counter = 0
    factorial = 1

    user_number_as_string = input("Enter a whole number: ")
    try:
        user_number_int = int(user_number_as_string)
        if user_number_int < 0:
            print(" {}, is not a whole number.".format(user_number_int))
        else:
            while counter < user_number_int:
                counter = counter + 1
                factorial = factorial * counter
            print("The factorial of {} is {}".format(user_number_int, factorial))   
    except ValueError:
        print("{} is not a whole number. Please enter a whole number.".format(user_number_as_string))


if __name__ == "__main__":
    main()