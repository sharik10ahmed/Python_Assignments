import pickle
my_dict = {"name":"John","age":29}

with open("data.bin","wb") as file:
     pickle.dump(my_dict,file)

with open("data.bin","rb") as file:
     var = pickle.load(file)
     print("retrieved",var)

