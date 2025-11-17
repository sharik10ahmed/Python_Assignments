my = {
    "Name" : "Sharik",
    "Class" : "Seven"

}
print("hello - > ",my.get("Name"))
print("all keys - > ",my.keys())
print("all values -> `",my.values())
print("all stuff -> ",my.items())
my.update({"roll":"42"})
print(my)
my["enroll"] = "789456"
print(my)
my.pop("Class")
print("pop -> ",my)
my.popitem()
print(my)
my.clear()
print("clear - > ",my)