numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for number in numbers:
    if number == 1:
        continue

    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            not_primes.append(number)
            break

    else:
         primes.append(number)
print(primes)
print(not_primes)
