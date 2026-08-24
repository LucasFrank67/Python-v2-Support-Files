import random

num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))


def calculate(num1, num2):
    operand = random.randint(1,3)
    if operand == 1:
        print(num1, "+", num2, "=", num1 + num2)
    elif operand == 2:
        print(num1, "-", num2, "=", num1 - num2)
    else:
        print(num1, "*", num2, "=", num1 * num2)

calculate(num1, num2)