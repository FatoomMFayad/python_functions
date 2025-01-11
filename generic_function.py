def genral_function(*x):
    sum = 0
    for i in x:
        sum+=i
    return sum
print(genral_function(1, 8, 5, 9))

def sum_min_max(*x):
    sum = 0
    for i in x:
        sum+=i
    ma = max(x)
    mi = min(x)
    return sum, ma, mi

print(sum_min_max(10, 8, 5, 9))