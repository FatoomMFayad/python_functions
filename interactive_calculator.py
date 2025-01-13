#9.	You're going to write an interactive calculator! User input is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
#If the input does not consist of 3 elements, raise an error Exception.
#Try to convert the first and third input to a float (like so: float_value = float(str_value)).
# Catch any ValueError that occurs
#If the second input is not '+' or '-', again raise an Exception

def interactive_calculator():
    my_formula = input("Enter your formula: ")
    elements = my_formula.split()
    if len(elements) != 3:
        raise Exception("Input must consist of a number, an operator, and another number separated by spaces.")
    try:
        first_element = float(elements[0])
        second_element = float(elements[2])
        operator = elements[1]
        if operator not in ('+', '-'):
            raise Exception("Operator must be either '+' or '-'.")

        if operator == "+":
            return first_element + second_element
        else:
            return first_element - second_element

    except ValueError as e:
        print(e)

try:
    print(f"The formula result is {interactive_calculator()}")
except Exception as e:
    print(e)
