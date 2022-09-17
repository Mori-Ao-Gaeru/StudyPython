import math
def is_prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

print("Please Input a natural number")
n = int(input())
print(is_prime(n))


