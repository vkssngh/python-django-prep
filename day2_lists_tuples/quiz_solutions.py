# Q1. Create a list of squares from 1 to 10 using list comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)

cubes = [x**3 for x in range(1, 11)]
print(cubes)

# Q2. Convert list -> tuple
list=[1, 2, 3, 4, 5]
toup=tuple(list)

print(toup)

# Q3. Nested tuple access
nested = (1, (2, 3), 4)
print(nested[1][1])

# Q4. Remove duplicates from list (method 1: set)
def remove_duplicates(lst):
    return list(set(lst))

# Q5. Merge two lists into list of tuples
a = [1, 2, 3]
b = ["x", "y", "z"]
merged = list(zip(a, b))  # [(1, 'x'), (2, 'y'), (3, 'z')]
