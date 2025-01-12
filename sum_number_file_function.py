#6.	Write a Python function that takes a file path as an argument and prints the sum of all numbers in the file.
def sum_numbers(n):
    try:
        with open(n) as f:
            numbers = f.readlines()
            sum = 0
            for number in numbers:
                sum += int(number)
            return sum
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)

file_path = 'C:/Users/Fatoom/Documents/text_files/numbers2.txt'
print(sum_numbers(file_path))