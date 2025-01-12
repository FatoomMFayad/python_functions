#4.	Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

number = 5
print(f"The factorial of {number} is: {factorial(number)}")