# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5
number1 = int(input('Plese add a number'))
number2 = int(input('Plese add an other number, it should be bigger'))
if number2 < number1:
    print("The second number should be bigger")
else:
    for range((number2-number1) > 0)
        print(number1 + 1)
