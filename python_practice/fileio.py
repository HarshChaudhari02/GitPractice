# with open("data.txt", "w") as file:
#     file.write("Hey! Newly Created")


# with open("data.txt", "r") as file:
#     for line in file:
#         print(line)


# with open("data.txt", "a") as file:
#     file.write("Now Added")

# with open("data.txt", "r") as file:
#     print(file.read())


#CSV

# import csv

# filename = "data.csv"
# data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]

# with open(filename, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)


# with open(filename, "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


#using dictioneries
# import csv

# data = [{"Name": "Alice", "Age": 30}, {"Name": "Bob", "Age": 25}]

# with open("data.csv", "w", newline="") as file:
#     fieldnames = ["Name", "Age"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)

## Json

import json

data = {"Name": "Alice", "Age": 34, "Skills": ["Python", "SQL"]}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    out = json.load(file)
    print(type(out))
