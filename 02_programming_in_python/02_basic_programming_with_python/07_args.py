def sum_of(a,b):
    return a + b

def sum_of_args(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
   
print(sum_of(4,5))
print(sum_of_args(4,5,6))
