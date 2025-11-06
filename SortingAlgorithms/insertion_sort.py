#insertion sort algorithm
def insertion_sort(lst):
    '''
    Sorts a list in ascending order using the insertion sort algorithm.
    Args:
        lst (list): The list to be sorted.
    Returns:
        list: The sorted list.
    Pseudo-code:
        FOR i = 1 TO size-1
            key = lst[i]
            ind_sorted = i - 1
            WHILE ind_sorted >= 0 AND a[ind_sorted] > key
                lst[ind_sorted + 1] = lst[ind_sorted]
                ind_sorted = ind_sorted - 1
            ENDWHILE
            lst[ind_sorted + 1] = key
        ENDFOR
    '''
    for i in range(1, len(lst)): # for a number of passes equal to the size of the list minus 1
        key = lst[i]       # the next item to be inserted in the sorted portion of the list
        ind_sorted = i - 1 # index of the last item in the sorted portion of the list

        while ind_sorted >= 0 and lst[ind_sorted] > key: # while items in sorted partition are greater than the key
            lst[ind_sorted + 1] = lst[ind_sorted]        # shift the item to the right
            ind_sorted -= 1                             # move to the next item in the sorted portion  


        lst[ind_sorted + 1] = key # copy the key to its correct position in the sorted portion
        
    return lst

if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = insertion_sort(sample_list)
    print("Sorted list is:", sorted_list)