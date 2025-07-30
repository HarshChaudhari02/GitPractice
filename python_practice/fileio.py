with open("data.txt", "w") as file:
    file.write("Hey! Newly Created")


with open("data.txt", "r") as file:
    for line in file:
        print(line)


with open("data.txt", "a") as file:
    file.write("Now Added")

with open("data.txt", "r") as file:
    print(file.read())