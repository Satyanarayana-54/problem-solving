age = 20
if age >= 18:
    print("You are an adult.")  # Output: You are an adult.


num = 10
if num % 2 == 0:
    print("Even number")  # Output: Even number
else:
    print("Odd number")


marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")  # Output: Grade: B
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")


x = 10
if x > 5:
    print("Greater than 5")  # Output: Greater than 5
    if x > 8:
        print("Also greater than 8")  # Output: Also greater than 8


a, b = 10, 20
min_value = a if a < b else b
print("Minimum value:", min_value)  # Output: Minimum value: 10