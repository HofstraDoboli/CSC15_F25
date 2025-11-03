def binary_search(arr, target):
    '''
    Perform a binary search for the target in a sorted array.
    Args:
        arr (list): The sorted list to search through.
        target: The value to search for.
    Returns: 
        int: The index of the target if found, otherwise -1.
    '''
    start_index = 0
    end_index = len(arr) - 1
    num_comparisons = 0 
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        mid_value = arr[mid_index]
        num_comparisons += 1
        if mid_value == target:
            return mid_index
        elif mid_value > target: # search first half (middle value is larger than target)
            end_index = mid_index - 1
        else: # search in the second half (middle value is smaller than target)
            start_index = mid_index + 1

    return -1, num_comparisons


if __name__ == "__main__":
    sample_array = [1, 2, 3, 4, 5, 7, 10, 15, 19, 20] # already sorted very important
    target_value = 6
    result, num_comparisons = binary_search(sample_array, target_value)

    print("Number of comparisons made:", num_comparisons)
    
    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found in the array.")