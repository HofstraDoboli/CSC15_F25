# selection sort

def selection_sort(lst):
    '''
    Sorts a list in ascending order using the selection sort algorithm.
    Args:
        lst (list): The list to be sorted.
    Returns:
        list: The sorted list.
    Pseudo-code:
        FOR i = 0 TO size-1
            min_index = i
            FOR j = i+1 TO size
                IF lst[j] < lst[min_index]
                    min_index = j
                ENDIF
            ENDFOR
            swap lst[i] with lst[min_index]
        ENDFOR
    '''
    for i in range(len(lst)): # for a number of passes equal to the size of the list
        min_index = i # assume the smallest item is at index i
        for j in range(i+1, len(lst)): # search for the smallest item in the list from index i+! to end
            if lst[j] < lst[min_index]:
                min_index = j # update min_index if a smaller item is found
        
        # swap lst[i] with lst[min_index]
        temp       = lst[i]
        lst[i]     = lst[min_index]
        lst[min_index] = temp
    return lst


if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = selection_sort(sample_list)
    print("Sorted list is:", sorted_list)