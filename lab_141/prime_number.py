# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# List to store prime numbers
prime_numbers = []

# Finding prime numbers between 1 to 250
for i in range(1, 251):
    if is_prime(i):
        prime_numbers.append(i)

# Writing prime numbers to results.txt
with open('results.txt', 'w') as file:
    for prime in prime_numbers:
        file.write(str(prime) + '\n')

print("Prime numbers between 1 to 250 have been saved in results.txt.")
