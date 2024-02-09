import random
# f = open("petnames.txt", "r")
# f_content = f.read()
# f_content_list = f_content.split("\n")
# # print(f_content)
# print(f_content_list)
# f.close()
# print(random.choice(f_content_list))


f_name = input('Type the file name: ')
f = open(f_name)  # "r" omitted as it's the default
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()
print(random.choice(f_content_list))
