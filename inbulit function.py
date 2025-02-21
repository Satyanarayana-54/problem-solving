print("Hello, World!")
# Output: Hello, World!

my_list = [10, 20, 30]
print(len(my_list))
# Output: 3


num = 5
print(type(num))
# Output: <class 'int'>

float_num = 10.6
print(int(float_num))
# Output: 10


num = 100
print(str(num))
# Output: '100'

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
# Output: 15

numbers = [10, 20, 30]
print(max(numbers))
# Output: 30

numbers = [10, 20, 30]
print(min(numbers))
# Output: 10


negative_num = -50
print(abs(negative_num))
# Output: 50

name = input("Enter your name: ")
print(f"Hello, {name}!")
# Output: (User enters 'Alice')
# Enter your name: Alice
# Hello, Alice!


names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = zip(names, ages)
print(list(combined))
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
