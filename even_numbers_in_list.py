#2.	Write a Python function to print the even numbers from a given list
def even_numbers(nums):
    even_nums = [number for number in nums if number%2==0]
    return even_nums

print(even_numbers([3, 4, 8, 7, 9, 12, 55]))