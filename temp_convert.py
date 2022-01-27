# !/usr/bin/env python3


# Created By: Dylan Melo
# Date: Jan, 2021
# This program asks user for degrees in
# celsius and displays it in fahrenheit.

def calculate_fahrenheit():
    print("Welcome to the Celsius to Fahrenheit converter!")
    print("")
    user_degrees = input("Enter degrees in celsius: ")
    print("")
    try:
        user_degrees_float = float(user_degrees)
        degrees_fahrenheit = (9.0/5.0)*user_degrees_float+32
        print("{}°C is equal to {}°F "
              . format(user_degrees_float, degrees_fahrenheit))
    except Exception:
        print("Invalid input")


def main():
    calculate_fahrenheit()


if __name__ == "__main__":
    main()
