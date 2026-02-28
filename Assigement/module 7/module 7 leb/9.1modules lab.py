# Write a Python program to generate random numbers between 1 and 100 using the random module.import random

import random
num = random.randint(1, 100)
print("Random Number:", num)
print("\nFive Random Numbers:")
for i in range(5):
    print(random.randint(1, 100))
