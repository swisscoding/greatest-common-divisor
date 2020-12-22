#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Greatest common divisor | ----\n", fg("red")))

# user interaction
num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))

# main program
def determineGCD(n1, n2):
    divisor = 2
    temp = 0
    while True:
        if num1 % divisor == 0 and num2 % divisor == 0:
            temp = divisor
            divisor += 1
        else:
            divisor += 1
        if divisor > num1 or divisor > num2:
            if temp != 0:
                return temp
            else:
                return 1

gcd = stylize(determineGCD(num1, num2), fg("red"))
print(f"\nGreatest common divisor of {num1} and {num2} is {gcd}.\n")
