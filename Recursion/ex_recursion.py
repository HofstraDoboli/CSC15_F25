"""
recursion_examples.py
CSC 15 – Examples of Recursive Functions
----------------------------------------
Includes:
  1. is_palindrome(s)
  2. count_occurrences(lst, target)
  3. power(x, n)
  4. find_max(lst)
Each function contains documentation, pseudo-code, and test calls.
"""

# ------------------------------------------------------------------
def is_palindrome(s):
    """
    Checks whether a string is a palindrome using recursion.

    Parameters:
        s (str): The string to check.

    Returns:
        bool: True if s reads the same forward and backward, False otherwise.

    Pseudo-code:
        1. If the string length <= 1, return True  (base case)
        2. If the first and last characters are different, return False
        3. Otherwise, call is_palindrome on the substring s[1:-1]
    """
 


# ------------------------------------------------------------------
def count_occurrences(lst, target):
    """
    Counts how many times 'target' appears in a list using recursion.

    Parameters:
        lst (list): List of elements.
        target: Value to count.

    Returns:
        int: Number of times target appears in lst.

    Pseudo-code:
        1. If list is empty, return 0  (base case)
        2. If first element == target:
              return 1 + count_occurrences(rest of list, target)
           Else:
              return count_occurrences(rest of list, target)
    """
 

# ------------------------------------------------------------------
def power(x, n):
    """
    Computes x raised to the power of n recursively.

    Parameters:
        x (float): Base number.
        n (int): Exponent (assume n >= 0).

    Returns:
        float: x^n

    Pseudo-code:
        1. If n == 0, return 1  (base case)
        2. Otherwise, return x * power(x, n - 1)
    """



# ------------------------------------------------------------------
def find_max(lst):
    """
    Finds the maximum value in a non-empty list recursively.

    Parameters:
        lst (list of numbers): List to search.

    Returns:
        number: The maximum value in lst.

    Pseudo-code:
        1. If the list has one element, return it  (base case)
        2. Otherwise:
            a. Find maximum of rest of list (recursive call)
            b. Return the larger between first element and max_rest
    """



# ------------------------------------------------------------------
# Testing block
if __name__ == "__main__":
    print("=== Testing Recursive Functions ===")

    # Test 1: Palindrome
    print("\n1. Testing is_palindrome:")
    words = ["level", "racecar", "hello", "a", ""]
    for w in words:
        print(f"{w!r} -> {is_palindrome(w)}")

    # Test 2: Count Occurrences
    print("\n2. Testing count_occurrences:")
    numbers = [1, 2, 3, 2, 4, 2, 5]
    print(f"List: {numbers}")
    print("Count of 2:", count_occurrences(numbers, 2))
    print("Count of 6:", count_occurrences(numbers, 6))

    # Test 3: Power
    print("\n3. Testing power:")
    print("2^4 =", power(2, 4))
    print("5^0 =", power(5, 0))
    print("3^3 =", power(3, 3))

    # Test 4: Find Maximum
    print("\n4. Testing find_max:")
    lists_to_test = [[7], [3, 8, 1, 9, 2], [10, 5, -2, 0]]
    for lst in lists_to_test:
        print(f"{lst} -> max = {find_max(lst)}")

    print("\n=== End of Tests ===")
