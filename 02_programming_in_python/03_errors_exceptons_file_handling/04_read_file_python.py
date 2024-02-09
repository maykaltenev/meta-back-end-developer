with open('newFile.txt', "r") as file:
    print(file.read(44))
    data = file.readlines()

    for x in data:
        print(x)
