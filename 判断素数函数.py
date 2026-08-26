def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for m in range(2, n):
            if n % m == 0:
                return False
            return True

print(is_prime(7))
print(is_prime(10))
print(is_prime(2))
print(is_prime(1))

for n in range(1, 101):
    if is_prime(n):
        print(n, end=" ")