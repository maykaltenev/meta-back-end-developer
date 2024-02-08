def divide_by(a,b):
    return a/b

try:
    ans = divide_by(40,0)
except ZeroDivisionError as e: 
    print(e,"we cannot devide by zero")
    print("Something went wrong!", e)
    print(e.__class__)
except Exception as e:
    print(e, "something went wrong")
