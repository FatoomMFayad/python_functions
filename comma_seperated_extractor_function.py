#8.	Create a Python function that prompts the user for a list of grades separated by commas. Split the string into individual grades and use a list comprehension to convert each string to an integer. You should use a try statement to inform the user when the values they entered cannot be converted.
from traceback import print_tb


def comma_seperated_extractor_function():
    grades_input = input("Enter a list of grades separated by commas: ")
    try:
        real_grades = [int(grade.strip()) for grade in grades_input.split(",")]
        return real_grades
    except ValueError as e:
        print(e)

print(comma_seperated_extractor_function())