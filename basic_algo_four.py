def right_rotate_array(array, abs_k):
    print(array)
    if abs_k > len(array):
        rotation_time = abs_k % len(array)
    else:
        rotation_time = abs_k
    for i in range(rotation_time):
        last_element = array[len(array) - 1]
        for j in range(len(array) - 1, 0, -1):
            array[j] = array[j - 1]
        array[0] = last_element
    print("right rotate array==", array)
    return array


def left_rotate_array(array, k):
    print("before rotation= ", array)
    if k == len(array):
        print(array)
    if k > len(array):
        k = k % len(array)
    else:
        k = k
    print("rotation time= ", k)
    for i in range(k):
        first_element = array[0]
        for j in range(len(array) - 1):
            array[j] = array[j + 1]
        array[len(array) - 1] = first_element
    print("after rotation = ", array)
    return array


def question_first(n, k):
    """i. You are given two numbers n and k. You are required to rotate n, k times to the right.
     If k is positive, rotate to the right i.e. remove rightmost digit and make it leftmost. Do
     the reverse for negative value of k. Also k can have an absolute value larger than number
      of digits in n.
        ii. Take as input n and k.
        iii. Print the rotated number.
        iv. Note - Assume that the number of rotations will not cause leading 0's in the result.
        e.g. such an input will not be given
           n = 12340056
           k = 3
           r = 05612340
        """
    try:

        if n < 0:
            n = abs(n)
        else:
            n = n
        array = [int(x) for x in str(n)]
        if k < 0:
            array = left_rotate_array(array, abs(k))
        elif k == 0:
            print("nothing to rotate", array)
        else:
            array = right_rotate_array(array, k)
        # print("after rotation array ", array)
        digit_str = [str(x) for x in array]
        number_as_str = "".join(digit_str)
        print("after rotation number is", int(number_as_str))
    except Exception as e:
        print(e)


def get_gcd_of_two_number(a, b):
    try:
        if a == 0 or b == 0:
            return -1
        smaller = 1
        larger = 1
        gcd = 1
        if a == b:
            return a
        elif a > b:
            smaller = b
            larger = a
        else:
            smaller = a
            larger = b
        while smaller != 0:
            if larger % smaller == 0:
                gcd = smaller
            temp = smaller
            smaller = larger % smaller
            larger = temp
        return gcd
    except Exception as e:
        print(e)


def get_lcm_of_two_numbers(a, b):
    try:
        if a == 0 or b == 0:
            return 0
        if a < 0 or b < 0:
            return -1
        gcd = get_gcd_of_two_number(a, b)
        lcm = (a * b) // gcd
        return lcm
    except Exception as e:
        print(e)
        return -1


def question_two(a, b):
    """i. You are required to print the Greatest Common Divisor (GCD) of two numbers.
        ii. You are also required to print the Lowest Common Multiple (LCM) of the same numbers.
        iii. Take input "num1" and "num2" as the two numbers.
        iv. Print their GCD and LCM."""
    try:
        gcd = get_gcd_of_two_number(a, b)
        lcm = get_lcm_of_two_numbers(a, b)
        if gcd == -1 or lcm == -1:
            print("invalid input")
            return
        print("gcd = {} and lcm ={}  of two numbers {},{} are ".format(gcd, lcm, a, b))
        return
    except Exception as e:
        print(e)
        return


def question_three(str_arg):
    if len(str_arg) == 0:
        print("please don't pass empty string")
        return False
    left_index = 0
    right_index = len(str_arg) - 1
    while left_index < right_index:
        if str_arg[left_index] != str_arg[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True


def question_four(str_arg):
    """i. You are given a string.
          ii. You have to print all palindromic substrings of the given string."""
    if isinstance(str_arg, str):
        if len(str_arg) <= 0:
            print("string is empty ")
            return
        string_list = []
        for i in range(len(str_arg)):
            print(str_arg[i])
            string_list.append(str_arg[i])
            left_index = i - 1
            right_index = i + 1
            while True:
                if left_index <= 0:
                    break
                if right_index >= len(str_arg):
                    break
                if str_arg[i] == str_arg[right_index]:
                    string_list.append(str_arg[i:right_index])


# Python3 program to Count number of ways we
# can get palindrome string from a given
# string

# function to find the substring of the
# string
def substring(s, a, b):
    s1 = ""

    # extract the specified position of
    # the string
    for i in range(a, b, 1):
        s1 += s[i]

    return s1


# can get palindrome string from a
# given string
def allPalindromeSubstring(s):
    v = []

    # moving the pivot from starting till
    # end of the string
    pivot = 0.0
    while pivot < len(s):

        # set radius to the first nearest
        # element on left and right
        palindromeRadius = pivot - int(pivot)

        # if the position needs to be
        # compared has an element and the
        # characters at left and right
        # matches
        while ((pivot + palindromeRadius) < len(s) and
               (pivot - palindromeRadius) >= 0 and
               (s[int(pivot - palindromeRadius)] ==
                s[int(pivot + palindromeRadius)])):
            v.append(s[int(pivot - palindromeRadius):
                       int(pivot + palindromeRadius + 1)])

            # increasing the radius by 1 to point
            # to the next elements in left and right
            palindromeRadius += 1

        pivot += 0.5
    return v


#
# v = allPalindromeSubstring("hellolle")
# print(v)

def question_five_i(str_arg):
    """ i. You are given a string.
        ii. You have to compress the given string in the following two ways -
        First compression -> The string should be compressed such that consecutive duplicates
        of characters are replaced with a single character.
        For "aaabbccdee", the compressed string will be "abcde".
        Second compression -> The string should be compressed such that consecutive duplicates
        of characters are replaced with the character and followed by the number of consecutive
        duplicates.
        For "aaabbccdee", the compressed string will be "a3b2c2de2"."""
    try:
        if isinstance(str_arg, str):
            if len(str_arg) == 0:
                print("don't pass empty string")
                return
            new_str = ""
            i = 0
            while i < len(str_arg) - 1:
                while i + 1 < len(str_arg) and str_arg[i] == str_arg[i + 1]:
                    i += 1
                if i < len(str_arg):
                    new_str += str_arg[i]
                i += 1
            if str_arg[len(str_arg) - 2] != str_arg[len(str_arg) - 1]:
                new_str += str_arg[len(str_arg) - 1]
            print("after first compression =", new_str)
        else:
            print("argument is invalid")

    except Exception as e:
        print(e)


# question_five_i("aaabbccdeeghe")
def question_five_ii(str_arg):
    """ i. You are given a string.
        ii. You have to compress the given string in the following two ways -
        First compression -> The string should be compressed such that consecutive duplicates
        of characters are replaced with a single character.
        For "aaabbccdee", the compressed string will be "abcde".
        Second compression -> The string should be compressed such that consecutive duplicates
        of characters are replaced with the character and followed by the number of consecutive
        duplicates.
        For "aaabbccdee", the compressed string will be "a3b2c2de2"."""
    try:
        if isinstance(str_arg, str):
            if len(str_arg) == 0:
                print("don't pass empty string")
                return
            new_str = ""
            i = 0
            while i < len(str_arg) - 1:
                count = 1

                while i + 1 < len(str_arg) and str_arg[i] == str_arg[i + 1]:
                    i += 1
                    count += 1
                if i < len(str_arg):
                    new_str += str_arg[i]
                if count != 1:
                    new_str += str(count)
                i += 1
            if str_arg[len(str_arg) - 2] != str_arg[len(str_arg) - 1]:
                new_str += str_arg[len(str_arg) - 1]
            print("after second compression =", new_str)
        else:
            print("argument is invalid")
            return

    except Exception as e:
        print(e)


def to_string(str_list):
    return ''.join(str_list)


# copy from geeks for geeks
def permute(a, l, r):
    if l == r:
        print(to_string(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)

            # backtrack
            a[l], a[i] = a[i], a[l]


a = list("ABC")
permute(a, 0, len(a) - 1)


def question_seven(string):
    """i. You are given a string that contains only lowercase and uppercase alphabets.
        ii. You have to toggle the case of every character of the given string.
         For eg -  CoEdify  -  cOeDIFY """

    # new_str = string.swapcase()
    # print("Original String =  ", string)
    # print("The Given String After Toggling Case =  ", new_str)
    new_str = ''
    for i in range(len(string)):
        if string[i] >= 'a' and string[i] <= 'z':
            new_str = new_str + chr((ord(string[i]) - 32))
        elif string[i] >= 'A' and string[i] <= 'Z':
            new_str = new_str + chr((ord(string[i]) + 32))
        else:
            new_str = new_str + string[i]

    print("Original String =  ", string)
    print("The Given String After Toggling Case =  ", new_str)


def question_eight(a, b):
    """Write a Program to find Union of Two Arrays."""
    if len(a) == 0 and len(b) == 0:
        print("both array is empty")
        return
    if len(a) == 0 and len(b) != 0:
        print(b)
        return
    elif len(a) != 0 and len(b) == 0:
        print(a)
        return
    for i in range(len(b)):
        a.append(b[i])
    print(a)


def question_nine(a, b):
    """Write a Program to find Intersection of two arrays"""
    if len(a) == 0 and len(b) == 0:
        print("both array is empty")
        return
    if len(a) == 0 and len(b) != 0:
        print("first array is empty")
        return
    elif len(a) != 0 and len(b) == 0:
        print("second array is empty")
        return
    intersection_list = []
    for i in range(len(b)):
        if b[i] in a:
            intersection_list.append(b[i])
    print(intersection_list)



