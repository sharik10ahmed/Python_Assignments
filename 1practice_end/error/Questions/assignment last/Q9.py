import json
student = {"Name": "Sam", "Roll": 10}

# a) Store
with open("student.json", "w") as f:
    json.dump(student, f)

# b) Read
with open("student.json", "r") as f:
    data = json.load(f)
    print("Data:", data)