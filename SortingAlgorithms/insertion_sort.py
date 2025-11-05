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



if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = insertion_sort(sample_list)
    print("Sorted list is:", sorted_list)