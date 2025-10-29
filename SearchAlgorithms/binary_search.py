def binary_search(arr, target):
    '''
    Perform a binary search for the target in a sorted array.
    Args:
        arr (list): The sorted list to search through.
        target: The value to search for.
    Returns: 
        int: The index of the target if found, otherwise -1.
    '''
    pass

if __name__ == "__main__":
    sample_array = [1, 2, 3, 4, 5, 7, 10] # already sorted very important
    target_value = 7
    result = binary_search(sample_array, target_value)
    
    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found in the array.")