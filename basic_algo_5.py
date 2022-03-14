# question first
def question_first(array, k):
    """Given an array arr[] and a number K where K is smaller than
      size of array, the task is to find the Kth Largest element in
      the given array. It is given that all array elements are distinct."""
    if len(array) == 0:
        print("array is empty not allowed")
        return
    if k > len(array):
        print("value of k must not be greater the number of element present in array")
        return
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
        if k == i + 1:
            print("{}th largest element is {}".format(k, array[i]))
            break
    print(array)


# question_first([1, 2, 3, 4, 5, 6, 9], 4)

def question_second(array, k):
    """ Given an array arr[] and a number K where K is smaller than size of array,
         the task is to find the Kth Smallest element in the given array. It is given
         that all array elements are distinct."""
    if len(array) == 0:
        print("array is empty not allowed")
        return
    if k > len(array):
        print("value of k must not be greater the number of element present in array")
        return
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
        if k == i + 1:
            print("{}th largest element is {}".format(k, array[i]))
            break
    print(array)


# question_second([1, 2, 3, 4, 5, 6, 9,-1], 4)

def question_third(array):
    """Given an array,rotate the array by one position in clock-wise direction.
        Example 1:
        Input:
        N = 5
        A[] = {1, 2, 3, 4, 5}
        Output:
        5 1 2 3 4"""
    if len(array) == 0:
        print("array is empty, not allowed")
        return
    last_element = array[len(array) - 1]
    for j in range(len(array) - 1, 0, -1):
        array[j] = array[j - 1]
    array[0] = last_element
    print(array)


question_third([1, 2, 3, 4, 5])


def question_four(array, k):
    """Given an array Arr[] of size, swap the Kth
       element from beginning with Kth element from end"""
    print("before Swapping the element array =", array)
    if len(array) == 0:
        print("array is empty, not allowed")
        return
    if k > len(array):
        print("k should be less than the number of elements present in the array")
        return
    array[k - 1], array[len(array) - k] = array[len(array) - k], array[k - 1]
    print("after swapping the elements =>", array)


# question_four([1, 2, 3, 4, 5], 2)

def question_five(array):
    """Given an array of size and you have to tell whether the array is perfect or not.
     An array is said to be perfect if it's reverse array matches the original array.
     If the array is perfect then print "PERFECT" else print "NOT PERFECT
     Input : Arr[] = {1, 2, 3, 2, 1}
    Output : PERFECT
    Explanation:
    Here we can see we have [1, 2, 3, 2, 1]
    if we reverse it we can find [1, 2, 3, 2, 1]
    which is the same as before.
    So, the answer is PERFECT."""

    if len(array) == 0:
        print("array is empty, not allowed")
        return
    left_index = 0
    right_index = len(array) - 1
    while left_index < right_index:
        if array[left_index] != array[right_index]:
            print("NOT PERFECT")
            return
        left_index += 1
        right_index -= 1
    print("PERFECT")


# question_five([1, 2, 3, 2, 1])

def question_six(array):
    """Given a stream of incoming numbers, find average or mean of the stream at every point.
    Example 1:
    Input:
    n = 5
    arr[] = {10, 20, 30, 40, 50}
    Output: 10.00 15.00 20.00 25.00 30.00
    Explanation:
    10 / 1 = 10.00
    (10 + 20) / 2 = 15.00
    (10 + 20 + 30) / 3 = 20.00
    And so on."""
    if len(array) == 0:
        print("array is empty, not allowed")
        return
    total = 0
    for i in range(len(array)):
        total += array[i]
        average = total / (i + 1)
        print(f'{average:.2f}', end=" ")


# question_six([10, 20, 30, 40, 50])


def question_seven(name_list):
    """Given a list of names, display the longest name.

        names[] = { "God", "Godz", "Godzilla", "Coedify", "Jerry" }

        Output:
        Godzilla"""

    if len(name_list) == 0:
        print("array is empty, not allowed")
        return
    max_len = -1
    name_index = -1
    for i in range(len(name_list)):
        if max_len < len(name_list[i]):
            max_len = len(name_list[i])
            name_index = i

    print('largest name in given list = ', name_list[name_index])


# name_list = ["God", "Godz", "Godzilla", "Coedify", "Jerry"]
# question_seven(name_list)

def question_eight(str_arg):
    """ Given a string S as input. Delete the characters at odd indices of the string.
        Example 1:
        Input: S = "Geeks"
        Output:"Ges"
        Explanation: Deleted "e" at index 1
        and "k" at index 3."""
    if len(str_arg) == 0:
        print("string can not be empty")
        return
    new_str = ""
    for i in range(len(str_arg)):
        if i % 2 == 0:
            new_str += str_arg[i]
    print("after deleting indices", new_str)


# question_eight("subodh yadva")

def question_nine(str_arg):
    """
    Given a string S which consists of alphabets , numbers and special characters.
    You need to write a program to split the strings in three different strings
    S1, S2 and S3 such that the string S1 will contain all the alphabets present in S ,
     the string S2 will contain all the numbers present in S and S3 will contain all
     special characters present in S.  The strings S1, S2 and S3 should have
     characters in same order as they appear in input.

    Example 1:
    Input:
    S = **Docoding123456789everyday##
    Output:
    Docodingeveryday
    123456789
    **##
    :param str_arg:
    :return:
    """
    if len(str_arg) == 0:
        print("string can not be empty")
        return
    symb_str = ""
    number_str = ""
    alphabet_str = ""
    for i in range(len(str_arg)):
        if (str_arg[i] >= "a" and str_arg[i] <= 'z') or (str_arg[i] >= "A" and str_arg[i] <= 'Z'):
            alphabet_str += str_arg[i]
        elif str_arg[i] >= "0" and str_arg[i] <= "9":
            number_str += str_arg[i]
        else:
            symb_str += str_arg[i]
    print(alphabet_str)
    print(number_str)
    print(symb_str)


# question_nine("**Docoding123456789everyday##")


def question_ten(str_arg):
    """
    Given a string of a constant length, print a triangle out of it. The triangle should start with the given
    string and keeps shrinking downwards by removing one character from the begining of the string.
     The spaces on the left side of the triangle should be replaced with dot character.
    Example 1:
    Input:
    S = @io30
    Output:
     @io30
    .io30
    ..o30
    ...30
    ....0
    :param str_arg:
    :return:
    """
    if len(str_arg) == 0:
        print("string can not be empty")
        return
    for i in range(len(str_arg)):
        print(str_arg[i:])


question_ten("@io30")
