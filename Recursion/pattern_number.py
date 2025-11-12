def print_num_pattern(num1, num2):
    # Base case
    if num1 < 0:
        print(num1, end=" ")
        return

    print(num1, end = " ")
    print_num_pattern(num1 - num2, num2)

    print(num1, end = " ")


if __name__ == "__main__":
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print_num_pattern(num1, num2)