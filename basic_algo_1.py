import numbers


def question_first():
    """Print “ Hello CoEdify “ on console ."""
    print('Hello CoEdify')


def question_second(a, b):
    """Write a Program to swap two numbers"""
    if isinstance(a, numbers.Real) and isinstance(b, numbers.Real):
        print("before swap a = {} and b = {}".format(a, b))
        a = a + b
        b = a - b
        a = a - b
        print("after swapping a = {} and b = {}".format(a, b))
    return "please pass numbers as argument"


def question_third(number):
    """Write a program in Java to check if a number is even or odd ?"""
    if isinstance(number, numbers.Real):
        if number % 2 == 0:
            return "Number is even"
        else:
            return "Number is Odd"
    return "please pass number as argument"


def question_four():
    """Write a Program to print all the natural numbers till 100 using for loop"""
    for i in range(1, 101):
        print(i, end=" ")


def question_five():
    """Write a Program to print all the natural numbers till 100 using while loop"""
    i = 1
    while i <= 100:
        print(i, end=" ")


def question_six():
    """Write a Program to Display Even Numbers From 1 to 100"""
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, end=" ")


def question_seven():
    """Write a Program to Display Odd Numbers From 1 to 100"""
    for i in range(1, 101):
        if i % 2 != 0:
            print(i, end=" ")


def question_eight(a, b):
    """Write a Program to Find Largest of Two Numbers"""
    if isinstance(a, numbers.Real) and isinstance(b, numbers.Real):
        if a == b:
            return "both numbers a={} and b={} are equal".format(a, b)
        if a > b:
            return "the greatest number = {}".format(a)
        else:
            return "the greatest number = {}".format(b)
    return "please pass numbers as argument"


def question_nine(a, b, c):
    """ Program to Find Smallest of Three Numbers """
    if isinstance(a, numbers.Real) and isinstance(b, numbers.Real) and isinstance(b, numbers.Real):
        if a == b and b == c:
            return " all three numbers are equal "
        if a <= b and a <= c:
            return " the smallest number is {}".format(a)
        elif b <= a and b <= c:
            return " the smallest number is {}".format(b)
        else:
            return " the smallest number is {}".format(c)
    return "please pass numbers as argument"


def question_ten(a):
    """Program to Check if a Number is Positive or Negative"""
    if isinstance(a, numbers.Real):
        return "number is negative" if a < 0 else "number is zero" if a == 0 else "number is positive"
    return "please pass numbers as argument"


def question_eleven():
    """Program to Find Sum of first 5 Natural Numbers"""
    print(5 * 6 / 2)


#     formula (n/2)*(n+1)

def question_twelve():
    """program to find product of first 5 Natural Numbers"""
    product = 1
    for i in range(2, 6):
        product *= i


def question_thirteen(marks):
    """Display an appropriate message based on the following rules:
    for marks above 90, print excellent.
    for marks above 80 and less than equal to 90, print good.
    for marks above 70 and less than equal to 80, print fair.
    for marks above 60 and less than equal to 70, print meets expectations.
    for marks less than equal to 60, print below par."""
    if isinstance(marks, numbers.Real):
        if marks > 90:
            print("excellent")
        elif (marks > 80 and marks <= 90):
            print("good")
        elif marks > 70 and marks <= 80:
            print("fair")
        elif marks > 60 and marks <= 70:
            print("meets expectations")
        else:
            print("below par")


def question_fourteen(a, b):
    """Write a program to divide 2 numbers , it will not divide by zero, Check that also"""
    if b == 0:
        return "divider can not be zero"
    else:
        quotient = a / b
        return "the quotient is = {]".format(quotient)


def question_fifteen(ch):
    """Write a Program to check whether an entered number is a small alphabet or not."""
    if isinstance(ch, str):
        if len(ch) == 1:
            if ch >= 'a':
                if ch <= 'z':
                    return "yes given character is small alphabet"
                else:
                    return "No given argument is not small alphabet"
        else:
            return "The passing argument is either string with more than one character or empty string"
    else:
        return "Please pass the character as argument"


def question_sixteen(ch):
    """Write a Program to check whether an entered number is a alphabet or not."""
    if isinstance(ch, str):
        if len(ch) == 1:
            if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
                return "yes given character is an alphabet"
            else:
                return "The given argument is an alphabet"
        else:
            return "The passing argument is either string with more than one character or empty string"
    else:
        return "Please pass the character as argument"


def question_seventeen(ch):
    """
    Write a Program to check whether an entered alphabet is a vowel or not
    :param ch: string and expected a character
    :return: string
    """
    if isinstance(ch, str):
        if len(ch) == 1:
            if (ch == 'a' or ch == "e" or ch == "i"
                    or ch == "o" or ch == "u" or ch == "A"
                    or ch == "E" or ch == "I"
                    or ch == "O" or ch == "U"):
                return "yes given alphabet is is an Vowel"
            else:
                return "The given argument is not a Vowel"
        else:
            return "The passing argument is either string with more than one character or empty string"
    else:
        return "Please pass the character as argument"


def question_eighteen():
    """Print “ Hello CoEdify “ on console using function. """
    print("“ Hello CoEdify “")


# question_seventeen()
def question_nineteen():
    """Print the series  1 , 4, 7, 10, 13, 16....................till 100 using function"""
    i = 1
    while i <= 100:
        print(i, end=" , ")
        i += 3


question_nineteen()


def question_twenty():
    """Print the series   3, 6, 9, 12 ...            100    using function"""
    i = 3
    while i <= 100:
        print(i, end=" , ")
        i += 3


# question_twenty()


def question_twentyone():
    """Print the series   1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6,  till 100 using function"""
    i = 3
    j = 1
    while i <= 100:
        print(j, ", ", i, end=" , ")
        i += 2
        j += 1


def question_twenty_two():
    """"""
    for i in range(1, 11):
        print(5 * i)


def question_twenty_three(number1, number2):
    """Calculate the sum of two numbers using Function"""
    if isinstance(number1, numbers.Real) and isinstance(number2, numbers.Real):
        total = number1 + number2
        return "sum = {}".format(total)
    else:
        return "please pass arguments as the real numbers to add "


def question_twenty_four(number):
    """Write a program to find number of digits in a number"""
    if isinstance(number, int):
        digit_counts = 0
        while number:
            number = number // 10
            digit_counts += 1
        print("total digits in number = {}".format(digit_counts))
    else:
        print("please pass argument as integer number")


def question_twenty_five(number):
    """Write a program to find sum of digits in a number"""
    if isinstance(number, int):
        total = 0

        while number:
            remainder = number % 10
            number = number // 10
            print(number)
            total += remainder
        print("total sum of digit in given number = {}".format(total))
    else:
        print("please pass argument as integer number")
