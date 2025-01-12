#Python function to find the Max of three numbers
def max_function(x, y, z):
    max = x
    if y > max and y > z:
        max = y
    elif z > max and z > y:
        max = z
    return max

print(max_function(4, 3, 8))