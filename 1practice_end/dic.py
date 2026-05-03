my = {
    "name" : "Sharik",
    "class" : "12"
}

print(my.get("name"))
print(my.keys())

print(my.values())

print(my.items())

my.update({"id no.":"112"})

my.pop("class")
my.popitem()
my.clear()
print(my.items())