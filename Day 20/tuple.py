my_dict = {
                    "name": "Sharik",
                    "age" : 19,
                    "department": "CSE",
                    "data" : "11111111111"
}

print(my_dict["name"])  # Sharik
print("using get method => ", my_dict.get("name")) # Sharik
print("get all keys", my_dict.keys())
print("get all values: ", my_dict.values())

print("using items method=> ", my_dict.items())

my_dict["data"]  = "this is my data"
print("after changing the value of data key=> ", my_dict )

my_dict.update({"roll": "111"})
print("after applying update method => ", my_dict)

my_dict.update({"roll" : "222"})
print("after changing the roll using update method ", my_dict)

# my_dict.pop() # it gives error
# print("after applying pop method without any key ", my_dict)

my_dict.pop("department")
print("after applying pop method with any key ", my_dict)

my_new_dict = { "name" : "WIlmot", "roll": 1}

my_new_dict.popitem()

print("my_new_dictionary looks like this ", my_new_dict)

my_new_dict.clear()

print("after applying clear method ", my_new_dict)