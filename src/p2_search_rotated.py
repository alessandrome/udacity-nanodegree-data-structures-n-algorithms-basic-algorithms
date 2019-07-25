def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    list_len = len(input_list)
    left_index = 0
    right_index = list_len - 1
    while not left_index > right_index:
        mid = (left_index + right_index) // 2
        if input_list[mid] == number:
            return mid

        # left -> mid is sorted i can continue as a binary search
        if input_list[left_index] <= input_list[mid]:

            # As this subarray is sorted, we can quickly
            # check if key lies in half or other half
            if input_list[left_index] <= number <= input_list[mid]:
                right_index = mid - 1
            else:
                left_index = mid + 1

        # If arr[l..mid] is not sorted, then arr[mid... r]
        # must be sorted
        elif input_list[mid] <= number <= input_list[right_index]:
            left_index = mid + 1
        else:
            right_index = mid - 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1, 5, 6, 7, 9, 10, 11, 15], 10])  # not rotated array
test_function([[], 5])  # empty array always return -1
test_function([[5], 5])  # 1 element array testp1_root.txt
