# def main():
#     try:
#         name = input("Enter your name: ")
#         age = int(input("Enter your age: "))
        
#         if age < 0 or age > 130:
#             raise ValueError("Age should be between 0 and 130 years.")
        
#         print(f"Hello, {name} your age — {age}.")
#     except ValueError :
#         print(f"Error:")

# if str == "main":
#     main()


#2
# def greeting(name, age):
#     if age < 0 or age > 130:
#         raise ValueError("Age should be between 0 and 130 years.")
#     return f"Hello, {name} your age — {age}."

# def main():
#     try:
#         name = input("Enter your name: ")
#         age = int(input("Enter your age: "))
#         greeting = (name, age)
#         print(greeting)
#     except ValueError:
#         print(f"Error:")

# if str == "main":
#     main()


#3
# def main():
#     numbers = []
#     while True:
#         try:
#             number = float(input("Enter a positive number: "))
#             if number < 0:
#                 raise ValueError("A negative value was detected.")
#             numbers.append(number)
#         except ValueError:
#             print(f"Error:")
#             break
    
#     if all(num > 0 for num in numbers):
#         print(f"The sum of all numbers: {sum(numbers)}")
#     else:
#         print("The list contains a negative value. The amount is not calculated.")

# if str == "main":
#     main()







