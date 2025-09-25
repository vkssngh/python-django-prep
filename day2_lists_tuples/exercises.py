# 1. Reverse a list without using reverse()
def reverse_list(lst):
    return lst[::-1]
# Example usage:
print(reverse_list([1, 2, 3, 4, 5]))


# 2. Find largest and smallest number in a list
def find_min_max(numbers):
    return min(numbers), max(numbers)
# Example usage:
print(find_min_max([3, 1, 4, 1, 5, 9, 2, 6, 5]))

def count_occurrences(lst, value):
    return lst.count(value)

print(count_occurrences([1, 2, 3, 1, 4, 1], 1))

def count_list_elements(lst):
    count={}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count

print(count_list_elements(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))

def countlist_element(lst):
    count={}
    for item in lst:
        count[item]=count.get(item,0)+1
    return count

print(countlist_element(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))


# 4. Swap two variables using tuple unpacking
def swap(a, b):
    a, b = b, a
    return a, b

print(swap(5, 10))

# 5. Check if tuple is palindrome
def is_tuple_palindrome(t):
    return t == t[::-1]
# Example usage:
print(is_tuple_palindrome((1, 2, 3, 2, 1)))

number=[10, 20, 30]
#sumofnumber=sum(number)
#print(sumofnumber)
def sum_of_numbers(num):
    total=0
    for n in num:
        total+=n
    return total
print(sum_of_numbers(number))

max_min=[10, 20, 5, 30, 15]
def max_min_number(num):
    maximum=num[0]
    minimum=num[0]
    for n in num:
        if n>maximum:
            maximum=n
        if n<minimum:
            minimum=n
    return maximum, minimum

remove_duplicates=[1, 2, 3, 2, 1, 4, 5]
list1=list(set(remove_duplicates))
print(list1)


first_list=[1,2,3,4]
second_list=[3,4,5,6]
def common_elements(list1, list2):
    return list(set(list1) & set(list2))    
print(common_elements(first_list, second_list))


students = [("Alice", 20), ("Bob", 22), ("Charlie", 19)]

def print_name_age(students):
    for name,age in students:
        print(f"{name} is {age} years old")
    
print_name_age(students)