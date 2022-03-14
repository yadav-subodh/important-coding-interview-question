import math


def question_one(given_year):
    """
    Write a program to find given year is leap year or not.
    :param given_year: integer number year as argument
    :return:
    """
    if isinstance(given_year, int):
        if given_year % 100 == 0:
            if given_year % 400 == 0:
                return "given number is a leap year"
            else:
                return "given year is not a leap year"
        elif given_year % 4 == 0:
            return "given number is a leap year"
        else:
            return "given number is not a leap year"
    return "please pass a integer number as arguments"


# leap_years = [2000, 2004, 2008, 1900, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]
# for given_year in leap_years:
#     print(check_leap_year(given_year))

def question_two():
    """Write a program to print all the small alphabets in a single Loop"""
    ch = 'a'
    while ch <= 'z':
        print(ch, end=", ")
        ch = chr(ord(ch) + 1)


def question_three():
    """Write a Program to print all the vowels in a single loop"""
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        print(vowel, end=", ")


def question_four():
    """Write a Program to print all the consonants in a single loop."""
    ch = "a"
    while ch <= "z":
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
            ch = chr(ord(ch) + 1)
            continue

        else:
            print(ch, end=", ")
        ch = chr(ord(ch) + 1)


def question_five(number):
    """
    Write a Program to find factorial of given number n
    :param number: int
    :return: string
    """
    if isinstance(number, int):
        if number < 0:
            return "factorial of negative numbers is not possible"
        elif number == 0:
            return "factorial of 0 = 1"
        else:
            factorial = 1
            while number:
                factorial *= number
                number -= 1
            return "factorial of given number ={}".format(factorial)
    else:
        return "please pass argument as a integer"


def question_six(number):
    """
    Write a program to find whether the given number is Prime number or not.
    :param number: int
    :return: string message
    """
    if isinstance(number, int):
        if number == 2 or number == 3:
            return "given number is a prime number"
        divisor = number // 2
        flag = 1
        while divisor >= 2:
            if number % divisor == 0:
                flag = 0
                break
            divisor -= 1
        if flag == 1:
            return "given number is a prime number"
        else:
            return "given number is not a prime number"
    else:
        return "please pass argument as a integer"


def question_seven(number):
    """Write a program to find whether the given number is Prime number or not using minimum time complexity."""
    if isinstance(number, int):
        if number == 2 or number == 3:
            return "given number is a prime number"
        divisor = math.floor(math.sqrt(number))
        flag = 1
        while divisor >= 2:
            if number % divisor == 0:
                flag = 0
                break
            divisor -= 1
        if flag == 1:
            return "given number is a prime number"
        else:
            return "given number is not a prime number"
    else:
        return "please pass argument as a integer"


def question_eight():
    """Write  a program to print all the values in an array, you have to take elements from the user"""
    print("enter the size of array ")
    size_of_array = int(input())
    array = [0] * size_of_array
    print(array)
    print("enter the elements of array")
    for i in range(size_of_array):
        array[i] = int(input())
    print("elements in array", array)


def question_nine(array, element):
    """ Write a Program to search an element in an array"""
    for i in range(len(array)):
        if array[i] == element:
            return "element found at index = {}".format(i)
    return "element not found"


def question_ten(array, element):
    """Write a Program to search an element in an array if the array is sorted  ( Binary Search )"""
    if len(array) == 0:
        print("array is empty")
        return
    if len(array) == 1 and element == array[0]:
        print("element present at index", 0)
        return
    left_pointer = 0
    right_pointer = len(array) - 1
    while left_pointer <= right_pointer:
        mid_pointer = left_pointer + (right_pointer - left_pointer) // 2
        if array[mid_pointer] == element:
            print("element found at index = ", mid_pointer)
            return
        elif element < array[mid_pointer]:
            left_pointer = mid_pointer - 1
        else:
            right_pointer = mid_pointer + 1
    print("element is not found in array")


question_ten([1, 2, 3, 4, 5, 7, 9, 10, 20], 5)


def question_eleven(array):
    """Write a Program to find the largest number in an array."""
    if len(array) == 0:
        return "Don't pass empty array"
    elif len(array) == 1:
        return "larget element is = {}".format(array[0])
    max_element = array[0]
    for i in range(1, len(array)):
        if max_element < array[i]:
            max_element = array[i]
    return "max element is = {}".format(max_element)


def question_twelve(array):
    """Write a program to find smallest number in an array"""
    if len(array) == 0:
        return "Don't pass empty array"
    elif len(array) == 1:
        return "the smallest element is = {}".format(array[0])
    min_element = array[0]
    for i in range(1, len(array)):
        if min_element > array[i]:
            min_element = array[i]
    return "max element is = {}".format(min_element)


def question_thirteen(array):
    """Write a Java program to get the difference between the
     largest and smallest values in an array of integers. The
     length of the array must be 1 and above"""
    try:
        if len(array) == 0:
            return "Don't pass empty array"
        max_element = question_eleven(array)
        min_element = question_twelve(array)
        dif = int(max_element.split('=')[1]) - int(min_element.split("=")[1])
        return "difference between largest and smallest element of array {}".format(dif)
    except Exception as e:
        print(e)
        return "there are argument error"


print(question_thirteen([1, 2, 4, 5, 6, 10]))


def question_fourteen(array):
    """Program to print the elements of an array in reverse order"""
    if len(array) == 0:
        return
    elif len(array) == 1:
        print(array[0])
        return
    else:
        i = len(array) - 1
        while i >= 0:
            print(array[i], end=", ")
            i -= 1
        return


# question_fourteen([1, 2, 4, 5, 6, 2, 9])

def question_fifteen(array):
    """Program to find the frequency of each element in the array"""
    try:
        frequency_of_element = {}
        if len(array) == 0:
            return {}
        elif len(array) == 1:
            return {array[0]: 1}
        else:
            for i in range(len(array)):
                if array[i] in frequency_of_element.keys():
                    frequency_of_element[array[i]] += 1
                else:
                    frequency_of_element[array[i]] = 1
        return frequency_of_element
    except Exception as e:
        print(e)
        return {}


def question_sixteen(array, copy_array):
    """Program to copy all elements of one array into another array"""
    copy_array = array
    print("original array", array)
    print("copy array", copy_array)


def question_seventeen(n):
    """Write a Program to find Fibonacci Series up to n   (n>=2)"""
    try:
        a = 0
        b = 1
        if n < 0:
            return
        if n == 1:
            print(0)
            return
        elif n == 2:
            print(0, ", ", 1)
            return
        else:
            term = 1
            while term <= n:
                print(a, end=", ")
                a, b = b, a + b
                term += 1
        return
    except Exception as e:
        print(e)


def question_nineteen():
    """write a program called NBSP SquarePattern that
     prompts user for the size (a non-negative integer
     in int); and prints the following square pattern
      using two nested for-loops."""
    print("Enter the size of pattern ")
    pattern_length = int(input())
    for i in range(pattern_length):
        for j in range(pattern_length):
            print("#", end="")
        print("")


# question_nineteen()

def question_twenty():
    """Write a programs called TriangularPattern
    X that prompts user for the size (a non-negative
     integer in int); and prints each of the patterns as shown:
     Enter the size: 8
        #
        # #
        # # #
        # # # #
        # # # # #
        # # # # # #
        # # # # # # #
        # # # # # # # #  """
    print("Enter the size of pattern ")
    pattern_length = int(input())
    for i in range(1, pattern_length + 1):
        for j in range(i):
            print("#", end=" ")
        print("")


def question_twentyone():
    """Write a programs called NumberPatternX that
    prompts user for the size (a non-negative integer
    in int); and prints the pattern as shown:
    Enter the size: 8
        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
        1 2 3 4 5 6
        1 2 3 4 5 6 7
        1 2 3 4 5 6 7 8 """
    print("Enter the size of pattern ")
    pattern_length = int(input())
    for i in range(1, pattern_length + 1):
        count = 1
        for j in range(i):
            print(count, end=" ")
            count += 1
        print("")


def question_twenty_two():
    """ Write a Program to take a input of a string from user and print it on Console."""
    print("Enter a string")
    input_string = input()
    print(input_string)


def question_twenty_third():
    """Write a program to find number of characters in a string"""
    print("Enter a string")
    input_string = input()
    print("character in string", len(input_string))


def question_twenty_four():
    """ Write a program called ReverseString, which prompts user for a String, and
    prints the reverse of the String by extracting and processing each character.
     The output shall look like:"""
    print("Enter a string")
    input_string = input()
    new_str = ""
    reverse_index = len(input_string) - 1
    while reverse_index >= 0:
        new_str += input_string[reverse_index]
        reverse_index -= 1
    print("after reversing the string", new_str)


def question_twenty_five():
    """Program to count the total number of vowels and consonants in a string"""
    print("Enter a string")
    input_string = input()
    vowels = 0
    consonants = 0
    for i in range(len(input_string)):
        if ((input_string[i] >= "a" and input_string[i] <= "z") or
                (input_string[i] >= "A" and input_string[i] <= "Z")):
            if (input_string[i] == "a" or input_string[i] == "A" or
                    input_string[i] == "e" or input_string[i] == "E" or
                    input_string[i] == "i" or input_string[i] == "I" or
                    input_string[i] == "o" or input_string[i] == "O" or
                    input_string[i] == "u" or input_string[i] == "U"):
                vowels += 1
            else:
                consonants += 1
    print("number of vowels in string = ", vowels)
    print("number of consonants in string = ", consonants)
# question_twenty_five()
