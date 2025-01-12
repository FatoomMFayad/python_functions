#3.	Write a Python function to multiply all the numbers in a list

def multiply_list_items_function(my_list):
    try:
        multiplied_list = 1
        for item in my_list:
            multiplied_list *= item
        return multiplied_list

    except ValueError as e:
        print(f"This is not a valid numeric value {e}")

print(multiply_list_items_function([2, 5, 3]))