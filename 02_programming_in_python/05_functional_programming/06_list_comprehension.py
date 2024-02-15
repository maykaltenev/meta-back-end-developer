data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x % 4 == 0]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x % 4 == 0]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x % 9 == 0]
print("Nines: ", nines)

# List comprehension:
data = [x+3 for x in data]

# Regular for loop:
for x in range(len(data)):
    data[x] = data[x] + 3
    print(data[x])

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end=" ")


def square(num):
    return num * 2


result = square(4)


newdata = map(square, data)
print(newdata)
newdata = [x + 3 for x in data]
print(newdata)
a = [[96], [69]]

print(''.join(list(map(str, a))))

z = ["alpha", "bravo", "charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)


def sum(n):
    if n == 1:
        return 0
    return n + sum(n-1)


a = sum(5)
print(a)


numbers = [15, 30, 47, 82, 95]


def lesser(numbers):
    return numbers < 50


small = list(filter(lesser, numbers))
print(small)
