def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print("Please input a natural number.")
input_num = int(input())
print( factorial(input_num))
