count = 0
while count < 3:
    print("Count:", count)
    count += 1
print("Loop ended")

for i in range(5):
    
    if i==3:
        break
    print(i)
    
else:
    print("loop ended withot break")
#print 1 to 100 except 0    
for i in range(101):
    if i==0:
        continue
    #print(i)
# balance = 1000
# while True:
#     print("\n--- ATM Menu ---")
#     print("1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")
#     choice = input("Enter choice: ")
    
#     if choice == "1":
#         print(f"Your balance is {balance}")
#     elif choice == "2":
#         amount = int(input("Enter deposit amount: "))
#         balance += amount
#         print(f"Deposited {amount}. New balance: {balance}")
#     elif choice == "3":
#         amount=int(input("enter withdraw amount :"))
#         if amount<=balance:
#             balance=balance-amount
#             print(f"withdarw amount is {amount} and new balance is {balance}")
#     elif choice == "4":
#         print("Good boy!")
#         break
#     else:
#         print("Invalid choice, try again.")
        
        
#print only even number from 1 to 100
for i in range(1,101):
    if i%2!=0:
        continue
    print(i)
#find sum of digit in a number
num=12345
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num=num//10
print("sum of digit is :",sum)

fact_num=5
fact=1
for i in range(1,fact_num+1):
    print(i)
    fact=fact*i
print("factorial of number is :",fact)  

#reverse a number
num=12345
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("reverse number is :",rev)

#check number is prime  
num=10
count=0
for i in range(1,(num+1) // 2):
    if num/i:
        count +=1
        
if count >2:
    print(f"given number is not {num} prime number")
else:
    print("number is prime")
#fibonacci series
n=10
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b  
    
#Print a pyramid/star pattern
rows=5
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
    
#Implement FizzBuzz (print "Fizz" for multiples of 3, "Buzz" for 5, "FizzBuzz" for both).

my_dict = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
#3. Updating & Adding Data
my_dict["age"] = 26     # Update value
my_dict["city"] = "Delhi"  # Add new key-value pair
print(my_dict)

my_dict.pop("is_student")  # Remove key-value pair
print(my_dict)
del my_dict["city"]
print(my_dict)

my_dict.clear() 
print(my_dict)

student = {"name": "Vikas", "age": 24, "course": "Django"}
for key in student:
    print(f"{key} value is {student[key]}")
for key, value in student.items():
    print(f"{key} value is {value}")
    
student = {"name": "Vikas", "age": 24, "course": "Django"}
print(student.keys())

print(student.values())

print(student.items())

students = {
    1: {"name": "Alice", "age": 21},
    2: {"name": "Bob", "age": 22}
}
for i  in students:
    print(f"ID: {i}, Name: {students[i]['name']}, Age: {students[i]['age']}")
    
    
students={}
def add_students(roll,name,age):
    students[roll]={"name":name,"age":age}
    print(f"student added with roll no {roll} and name is {name} and age is {age}")
    
add_students(1,"vikas",24)

def view_student():
    for roll,info in students.items():
        print(f" for roll no {roll} name is {info["name"]} and age is {info["age"]}")

view_student()


def remove_student(roll):
    if roll in students:
        removed=students.pop(roll)
        print(f"removed {removed["name"]}")
    else:
        print("student record not found")


remove_student(3)



sentence = "python is great and python is powerful"
word_counts = {}

for word in sentence.split():
    # ✅ safer with .get()
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)

    
my_dict = {"b": 3, "a": 1, "c": 2}
my_dict_sorted_by_key = dict(sorted(my_dict.items()))

print(my_dict_sorted_by_key)  # {'a': 1, 'b': 3, 'c': 2}

my_dict = {"b": 3, "a": 1, "c": 2}

# sort by values
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)

sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_desc)

import json

my_dict = {"name": "Alice", "age": 25, "is_student": False}

# dict → JSON string
json_str = json.dumps(my_dict)
print(json_str)

