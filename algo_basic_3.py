def get_max_element_from_array(array):
    max_element = array[0]
    for i in range(1, len(array)):
        if max_element < array[i]:
            max_element = array[i]
    return max_element


def question_first(array):
    """Write a program to find the second largest element in an array."""
    if len(array) < 2:
        return
    if len(array) == 2 and array[0] == array[1]:
        print("there is no second largest number in given array")
    else:
        max_element = get_max_element_from_array(array)
        min_diff = float('inf')
        second_largest_element = float('-inf')
        for i in range(len(array)):
            if array[i] != max_element and min_diff > max_element - array[i]:
                min_diff = max_element - array[i]
                second_largest_element = array[i]
        print("second largest element in array", second_largest_element)


def get_minimum_element(array):
    minimum_element = array[0]
    for i in range(1, len(array)):
        if minimum_element > array[i]:
            minimum_element = array[i]
    return minimum_element


def question_second(array):
    """Write a program to find the second smallest element in an array"""
    if len(array) < 2:
        print("array size at least 2")
        return
    minimum_element = get_minimum_element(array)
    flag = 0
    second_min_element_index = -1
    second_min_element = float('inf')
    for i in range(len(array)):
        if second_min_element > array[i]:
            if array[i] != minimum_element:
                second_min_element = array[i]
                second_min_element_index = i
                flag = 1
    if flag != 1:
        print("there is no second minimum element")
    else:
        print("the index second min element = {} and element = {}".format(second_min_element_index, second_min_element))


# question_second([1, 2, 3, 4, 5, 6, 7, 7, 9])


def question_third(array):
    """Program to find average of an int Array"""
    if len(array) <= 0:
        print("array can not be empty")
        return
    total = 0
    for i in range(len(array)):
        total += array[i]
    print("average is =", total / len(array))
    return


def question_four(array):
    """Write a Java program to compute the average value of
     an array of integers except the largest and smallest values"""
    if len(array) < 3:
        print("please enter the array with minimum different three element")
        return
    min_element = get_minimum_element(array)
    max_element = get_max_element_from_array(array)
    total = 0
    for i in range(len(array)):
        total += array[i]
    average = (total - (min_element + max_element)) // (len(array) - 2)
    print("average of array element except min and max element", average)
    return


def question_five(array):
    """a Java program to find the number of even and odd integers in a given array of integers."""
    if len(array) < 1:
        print("Array is empty")
        return
    even_count = 0
    odd_count = 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("even count = {} and odd count = {}".format(even_count, odd_count))


def question_six(array1, array2):
    """ Program to merge two arrays """
    if len(array1) == 0:
        if len(array2) != 0:
            print(array2)
            return
        else:
            print("both array are empty")
            return
    if len(array2) == 0:
        if len(array1) != 0:
            print(array1)
            return
        else:
            print("both array are empty")
            return
    len_array1 = len(array1)
    len_array2 = len(array2)
    total_size = len_array2 + len_array1
    new_array = [0] * total_size
    for i in range(len_array1):
        new_array[i] = array1[i]
    i = len_array1
    for j in range(len_array2):
        new_array[i] = array2[j]
        i += 1
    print("after merging the array ", new_array)
    return


def question_seven(array1, array2):
    """Program to compare two arrays, return true if they are equal else return false."""
    # python code
    # if array1 == array2:
    #     return True
    # else:
    #     return False
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[2]:
            return False
    return True


def question_eight(array, element):
    """Program to remove a particular element from an array."""
    if len(array) == 0:
        print("array is empty")
        return
    if element in array:
        array.remove(element)
        print("element is removed, current array = ", array)
    else:
        print("element is not present in given array")


def question_nine(array):
    """Program to sort an array in ascending order"""
    try:
        if len(array) == 0:
            print("array is empty")
            return
        print("before sorting ", array)
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
        print("after sorting array =", array)
    except Exception as e:
        print(e)


def question_ten(array):
    """Program to sort an array in descending order"""
    try:
        if len(array) == 0:
            print("array is empty")
            return
        print("before sorting ", array)
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
        print("after sorting array =", array)
    except Exception as e:
        print(e)



