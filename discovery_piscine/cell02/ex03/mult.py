a = int(input("Enter the first number:\n"))
b = int(input("Enter the second number:\n"))
result = a * b

print(f"{a} x {b} = {result}")
if result > 0:
    print("This number is positive.")
elif result < 0:
    print("This number is negative.")
else:
    print("This number is both positive and negative.")
