import math
def is_prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def count_Primes(n):
    return [i for i in range(2, n+1) if is_prime(i)]

print("Please Input a natural number")
n = int(input())
print(count_Primes(n))


