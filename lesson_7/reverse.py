import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

def reverse(array):
    for i in range(len(array) // 2):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]

reverse(array)
print(array)

array.reverse()
print(array)

array.sort()
print(array)

print("*" * 50)

t = tuple(random.randint(0, 100) for _ in range(size))
print(t)

t = tuple(sorted(t))
print(t)