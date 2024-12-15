import mymath

print("Addition:", mymath.add(10, 56))
print("Subtraction:", mymath.subtract(20, 20))
print("Multiplication:", mymath.multiply(10, 5))
print("Division:", mymath.divide(10, 5))

import math

print("Ceil of 3.4:", math.ceil(3.4))           # Ceil
print("Trunc of 3.9:", math.trunc(3.9))         # Trunc
print("Floor of 3.9:", math.floor(3.9))         # Floor
print("Factorial of 5:", math.factorial(5))     # Factorial
print("Fabs of -5.7:", math.fabs(-5.7))         # Fabs
print("Pow of 2^3:", math.pow(2, 3))             # Pow
print("Fmod of 5.5 and 2:", math.fmod(5.5, 2))  # Fmod
print("Fsum of [1.1, 2.2, 3.3]:", math.fsum([1.1, 2.2, 3.3]))  # Fsum
print("Prod of [1, 2, 3]:", math.prod([1, 2, 3]))  # Prod
print("Square root of 16:", math.sqrt(16))      # Sqrt

import random

print("Random number between 0 and 1:", random.random())      # random()
print("Random integer between 1 and 10:", random.randint(1, 10))  # randint()
print("Random floating point number between 1 and 10:", random.uniform(1, 10))  # uniform()
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))  # choice()

# Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)  # shuffle()

print("Random number from range 0 to 10 with step 2:", random.randrange(0, 10, 2))  # randrange()