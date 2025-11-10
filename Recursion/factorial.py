def factorial(n):
    print("Calling factorial(", n, ")")
    if n == 0:
        return 1
    else:
        result = n * factorial(n - 1)
        print("Returning", result, "for n =", n)
        return result

#print(factorial(0))
#print(factorial(1))
#print(factorial(2))
print(factorial(5))