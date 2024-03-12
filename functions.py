# functions
# - consists of function name, parameters.
# - starts "def" keyword.
# - optimizes and make a block of code reusable.

# # void function
# def averageOfThreeNumbers(num1, num2, num3):
#     #codes ...
#     average = (num1 + num2 + num3) / 3
#     print("Average: ", average)

# Shortcut for copying highlighted/single line : alt + shift + ArrowDown/ArrowUp
#Shortcut for repositions highlighted

# averageOfThreeNumbers(89, 76, 81)
# averageOfThreeNumbers(89, 76, 81)
# averageOfThreeNumbers(89, 76, 81)

# return function
title = "ang alamat ni rj"
title2 = "Sungkit"

def stringToTitle(title):
    return title.title()

def stringToUppercase(message):
    return message.lower()

def stringToLowercase(message):
    return message.upper()

def joinString(message, message2):
    return message.join(message2)

def countLetters(message):
    return len(message)

print(stringToTitle(title))
print(stringToUppercase(title))
print(stringToLowercase(title))
print(joinString((title, title2)))