
def bubble_sort(lst, ascending = True):
    '''
    Sorts a list in ascending order using the bubble sort algorithm.
    Args:
        lst (list): The list to be sorted.
    Returns:
        list: The sorted list.
    Pseudo-code:
        nrPasses = 0;     
	    nrSwaps = 1;     
	   
	    WHILE (nrSwaps > 0 && nrPasses < size);       
		  nrSwaps = 0        
		  FOR i = 0 TO size-nrPasses-1             
			IF (lst[i] > lst[i+1])            
		        nrSwaps++ 
                swap lst[i] with lst[i+1]
			ENDIF
		     i++ 
		  ENDFOR 
		nrPasses++
	    ENDWHILE
    '''
    # add code
    nr_passes = 0
    nr_swaps  = 1 

    while nr_swaps > 0 and nr_passes <= len(lst):
        nr_swaps = 0
        for i in range(len(lst)- nr_passes-1): # each pass you do one less comparison
                                                   # because the last items in the array are already sorted
            if ascending:
                if lst[i] > lst[i+1]: # if iteam at index i is greater than item at index i+1, swap them
                    nr_swaps += 1
                    temp     = lst[i]   # save lst[i] to a temporary variable
                    lst[i]   = lst[i+1] # copy over lst[i+1] to lst[i]
                    lst[i+1] = temp     # copy temp to lst[i+1]
            else: # descending
                if lst[i] < lst[i+1]: # if iteam at index i is greater than item at index i+1, swap them
                    nr_swaps += 1
                    temp     = lst[i]   # save lst[i] to a temporary variable
                    lst[i]   = lst[i+1] # copy over lst[i+1] to lst[i]
                    lst[i+1] = temp  

        nr_passes += 1

    return lst    

        

if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(sample_list, ascending = False) # sample_list is mutable, pass the original list to the function, the function sorts the original list
    print("Sorted list is:", sorted_list)
    print("Sample list is:", sample_list) # a sorted list
  