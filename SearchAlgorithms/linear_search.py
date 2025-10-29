
def linear_search(arr, target):
    """Perform a linear search for the target in the array.

    Args:
        arr (list): The list to search through.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    pass

if __name__ == "__main__":
    sample_array = [4, 2, 7, 1, 3, 10, 5]
    target_value = 7
    result = linear_search(sample_array, target_value)
   
    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found in the array.")