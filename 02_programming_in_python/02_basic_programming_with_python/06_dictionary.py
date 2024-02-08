sample_dictionary = {1: "Coffee", 2: "Tea", 3: "Juice"}
sample_dictionary[2] = "Mint Tea"
print(sample_dictionary[1])
print(sample_dictionary[2])
print(sample_dictionary)
del sample_dictionary[3]

my_d = {1:"Test", 'Name': "Jim", 1: "Not A Tes"}

my_d[2]= 'Test 2'
del my_d[1]
print(type(my_d))

print(my_d)
for x in my_d:
    print(x)
    
for key,value in my_d.items():
    print(str(key) + " : " + value)