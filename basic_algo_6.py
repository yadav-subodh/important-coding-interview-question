import numbers


def question_first(array):
    """Given an array of size-1such that it only contains distinct integers
     in the range of 1 to N. Find the missing element.
    Example 1:
    Input:
    N = 5
    A[] = {1,2,3,5}
    Output: 4
    Example 2:
    Input:
    N = 10
    A[] = {1,2,3,4,5,6,7,8,10}
    Output: 9"""
    try:
        if len(array) == 0:
            print("array is empty")
            return
        total_sum = 0
        for i in range(len(array)):
            total_sum += array[i]
        n = len(array) + 1
        missing_element = (n * (n + 1) // 2) - total_sum
        print("missing element = {} ".format(missing_element))
    except Exception as e:
        print(e)
        return


# question_first([1, 2, 3, 4, 5, 6, 7, 8, 10])

def question_second(array):
    """Given a sorted array A of size N, delete all the duplicates elements from A.
    Example 1:
    Input:
    N = 5
    Array = {2, 2, 2, 2, 2}
    Output: 2
    Explanation: After removing all the duplicates
    only one instance of 2 will remain"""
    try:
        if len(array) == 0:
            print("array is empty")
            return
        new_array = []
        for i in range(len(array)):
            if array[i] in new_array:
                continue
            else:
                new_array.append(array[i])
        print(new_array)
    except Exception as e:
        print(e)
        return


question_second([2, 2, 2, 2, 2])


# copy from geeksforgeeks
def question_third(str_arg):
    """"""
    try:
        res = [str_arg[i: j] for i in range(len(str_arg))
               for j in range(i + 1, len(str_arg) + 1)]

        # printing result
        print("All substrings of string are : " + str(res))
    except Exception as e:
        print(e)
        return


def question_four(string_arg, sub_str):
    """Your task is to implement the function strstr.
     The function takes two strings as arguments (s,x)
     and locates the occurrence of the string x in the
     string s. The function returns and integer denoting
      the first occurrence of the string x in s (0 based indexing)"""
    try:
        if len(string_arg) == 0:
            print("empty string is not allowed")
            return -1
        if len(sub_str) > len(str):
            print("sub string is larger than string")
            return -1
        return string_arg.find(sub_str)
    except Exception as e:
        print(e)
        return -1


def question_five(N):
    """You are given an integer N. You need to convert all zeroes of to 5"""
    try:
        if isinstance(N, int):
            if N == 0:
                print(5)
                return
            if N < 0:
                N = abs(N)
            digit_list = [x for x in str(N)]
            for i in range(len(digit_list)):
                if digit_list[i] == 0:
                    digit_list[i] = 5
            number_as_string = "".join(digit_list)
            print("number =", int(number_as_string))
            return
        else:
            print("invalid input")
            return

    except Exception as e:
        print(e)
        return


def question_six(str_arg):
    """ Given a string s of lowercase alphabets, check if it is isogram or not.
     An Isogram is a string in which no letter occurs more than once."""
    try:
        if isinstance(str_arg, str):
            unique_char = {}
            for i in range(len(str_arg)):
                if str_arg[i] in unique_char.keys():
                    print("string is not an Isogram")
                    return
                else:
                    unique_char[str_arg[i]] = 1
            print("String is an Isogram")
        else:
            print("invalid input")
            return

    except Exception as e:
        print(e)
        return


# question_six("machinee")

def question_seven():
    """ Given an array arr[] of N positive integers.
    Push all the zero’s of the given array to the
    right end of the array while maintaining the order
     non-zero elements."""
    pass


def question_ten(a, b, c):
    """ You are required to check if a given set of numbers is a valid pythagorean triplet.
    2. Take as input three numbers a, b and c.
    3. Print true if they can form a pythagorean triplet and false otherwise.
    Pythagorean Triplet is a2+ b2= c2

    INPUT – 5 3 4
    OUTPUT – True

    Input – 123
    Output - false"""
    try:
        if isinstance(a, numbers.Real) and isinstance(a, numbers.Real) and \
                isinstance(a, numbers.Real):
            triplet_list = [a, b, c].sort()
            square_sum = triplet_list[0] * 2 + triplet_list[1] * 2
            if triplet_list[2] * 2 == square_sum:
                print("numbers are pythagorean triplet")
                return
            else:
                print("numbers are not pythagorean triplet")
                return

        else:
            print("invalid input")
            return

    except Exception as e:
        print(e)
        return
