# ============================================================
# Function: binary_search_recursive
# Description: 
#   Performs a binary search on a sorted list using recursion.
#   Returns the index of the target value if found, otherwise -1.
# Parameters:
#   data_list : sorted list of numbers
#   target    : value to find
#   low, high : current search boundaries
'''
Example [1,2,3,5,7,9,10], target = 9. low = 0, high = 6

    # base case: 
        if low > high
            return False
    # recursive case
        target is in [1,2,3,5,7,9,10]:
          if target is in the middle of the list or
          if target is greater than the middle list
            target is in the second half # recursive case if target is greater than middle
          else
            target is in the first half # recursive case if target is lower than middle
'''
# ============================================================
def binary_search_recursive(data_list, target, low, high):
    # TODO: Base case(s)
    result = False

    if low > high:
        result = False
    else:   # TODO: Recursive case: divide search space in half

        middle_index = (low + high) // 2
        if data_list[middle_index] == target:
            result = True 
        elif data_list[middle_index] < target:
            result = binary_search_recursive(data_list, target, middle_index+1, high)
        else: # search in the first half
            result = binary_search_recursive(data_list, target, low, middle_index-1)
    
    return result

# ============================================================
# Function: linear_search_recursive
# Description:
#   Searches a list sequentially using recursion.
#   Returns the index of the target value if found, otherwise -1.
# Parameters:
#   data_list : list of numbers
#   target    : value to find
'''
Ex: [3, 5, 2, 4, 10, 2], target=4
    # base case
    if list is empty:
            return False
    # recursive case:
        the target is in the list [3, 5, 2, 4, 10, 2] 
        if the first item is equal to target or the target is in the list  [5, 2, 4, 10, 2] 

'''
# ============================================================
def linear_search_recursive(data_list, target):
    # TODO: Base case(s)
    result = False
    if len(data_list) == 0:
        result = False

    else:  # TODO: Recursive step: move to next index

        if data_list[0] == target:
            result = True
        else:
            result = linear_search_recursive(data_list[1:], target) # recursive call

    return result


# ============================================================
# Function: merge_sort
# Description:
#   Sorts a list using the recursive merge sort algorithm.
#   Returns a new sorted list.
# Parameters:
#   data_list : list of numbers to be sorted
# ============================================================
def merge_sort(data_list, low, high):
    # TODO: Base case: list of length 1
    print("merge_sort called with low =", low, "high =", high)
    if low >= high:
        return data_list
    # TODO: Recursive case: split list, sort halves, merge
    middle_index = (low + high)//2
    merge_sort(data_list, low, middle_index) # first half
    merge_sort(data_list, middle_index+1, high) # second half
    merge_sorted_lists(data_list, low, high) # merge the two sorted halves -> a big sorted list
    # TODO: Use merge_sorted_lists() helper to combine halves
    print("After merging from low =", low, "to high =", high, "list is:", data_list)
    return data_list

# ============================================================
# Helper Function: merge_sorted_lists
# Description:
#   Merges two sorted lists into a single sorted list.
#   Used by merge_sort to combine sorted halves.
# Parameters:
# input:  list is sorted from low to middle and from middle to high
# at the end: list is sorted from low to high
# ============================================================
def merge_sorted_lists(lst, low, high):
    print("\tMerging sorted lists from low =", low, "to high =", high, "in list:", lst)
    # TODO: Initialize empty result list
    result = []
    # TODO: Compare elements from left and right halves
    middle_index = (low + high) // 2

    left_index = low
    right_index  = middle_index + 1  

    while left_index <= middle_index and right_index <= high:
        if lst[left_index] <= lst[right_index]:      
            result.append(lst[left_index])
            left_index += 1
        else:
            result.append(lst[right_index])
            right_index += 1
    
    if left_index <= middle_index:
        result += lst[left_index:middle_index+1]

    if right_index <= high:
        result += lst[right_index:high+1]

    # copy result back to list
    for i in range(len(result)):
        lst[low + i] = result[i]
    print("\tMerged list from low =", low, "to high =", high, "is:", lst)
# ============================================================
# Main testing section
# ============================================================
if __name__ == "__main__":
    # Sample data for testing
    sample_list = [38, 27, 43, 3, 9, 82, 10]
    target_value = 43

    # TODO: Call linear_search_recursive to find target
    linear_result = linear_search_recursive(sample_list, target_value)
    print(f'Linear Search Result for {target_value} : {linear_result}')
    
    # TODO: Call merge_sort to sort the list
    sorted_list = merge_sort(sample_list, 0, len(sample_list)-1)
    print("Sorted List:", sorted_list)
   
    # TODO: Call binary_search_recursive to find target in sorted list
    binary_result = binary_search_recursive(sorted_list, target_value, 0, len(sorted_list)-1)
    print(f"Binary Search Result for {target_value}: {binary_result}")
    # TODO: Print results for each test
    