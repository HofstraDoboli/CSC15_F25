

def linear_search(arr, target, start_index = 0):
    """Perform a linear search for the target in the array.

    Args:
        arr (list): The list to search through.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.

    """
    for index in range(start_index, len(arr)):
        if arr[index] == target:
            return index
    return -1   


def linear_search_sorted(sorted_arr, target, start_index = 0):
    """Perform a linear search for the target in a sorted array.

    Args:
        sorted_arr (list): The sorted list to search through.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.

    """
    for index in range(start_index, len(sorted_arr)):
        if sorted_arr[index] == target:
            return index
        elif sorted_arr[index] > target:
            break # you reached a value larger than target
                  # get out of the closest loop 
    return -1 # target is larger than any value in the list, target is not in the list

if __name__ == "__main__":
    '''
    find all occurences of a value in a list
    '''
    sample_array = [4, 2, 7, 1, 7, 10, 5]
    target_value = 7

    result = linear_search_sorted(sample_array, target_value, start_index = 0)
    while result != -1 and result < len(sample_array):
        print(f"Target found at index: {result}")
        result = linear_search_sorted(sample_array, target_value, start_index = result + 1)

    '''
    sample_array = [4, 2, 7, 1, 7, 10, 5]
    target_value = 7
    result = linear_search(sample_array, target_value)
    print(result)
   
    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found in the array.")
    '''