import csv

# a) Write data
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Bob", 85])

# b) Read data
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
