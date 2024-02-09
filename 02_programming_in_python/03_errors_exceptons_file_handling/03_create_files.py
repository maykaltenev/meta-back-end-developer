try:
    with open('newfile.txt', 'w') as file:
        # file.write("This is a new file created")
        file.writelines(["This is a new file created",
                        "\nThis is a new line to be added!."])
except FileNotFoundError as e:
    print("ERROR", e)
