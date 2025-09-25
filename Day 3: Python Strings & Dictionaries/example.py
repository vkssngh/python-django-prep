s = "  Hello World  "
print(s.strip())
print(s.lower())
print(s.upper())
print(s.split())
print(''.join(['Hello', 'World']))
print(' '.join(['Hello', 'World']))


student = {"name": "Alice", "age": 22, "course": "Python"}
print(student['name'])
print(student.get("grade", "N/A"))  # N/A if key doesn’t exist
student['email']='vikas@gmail.com'
print(student)
del student["course"]         # delete
print(student.keys())         # dict_keys(['name','age','email'])
print(student.values())       # dict_values(['Alice', 23, 'alice@test.com'])

min_max=[1,2,3,4,5,6,7,8,9]
def min_max_number(num):
    mini=num[0]
    maxi=num[0]
    for n in num:
        if n>maxi:
            maxi=n
        if n<mini:
            mini=n
    return maxi, mini

min_max_number(min_max)
print(min_max_number(min_max))

# reverse the string
def reverse_string(s):
    return s[::-1]

#reverse the string without using slice 
def reverse_string_no_slice(s):
    rev=""
    for char in s:
        rev=char+rev
    return rev


# resverse the string using recursion
def reverse_string_recursion(s):
    if len(s)==0:
        return s
    else:
        return s[-1]+reverse_string_recursion(s[:-1])   
    
print(reverse_string_recursion("hello"))
print(reverse_string_no_slice("hello"))

def reverse_string1(s):
    return "".join(reversed(s))

print(reverse_string1("jai ho"))


#pailndrome
def is_palindrome(s):
    return s==s[::-1]   

#count vowels
def count_vowels(s):
    count=0
    vowels="aeiouAEIOU"
    for char in s:
        if char in vowels:
            count+=1
    return count    

print(count_vowels("hello world"))

def count_vowels1(s):
    vowels="aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

#Character frequency
def char_frequency(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq     

print(char_frequency("hello world"))
