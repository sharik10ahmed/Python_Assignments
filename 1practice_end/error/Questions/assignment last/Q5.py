import pickle

with open("data.bin","wb") as file:
     pickle.dump(["apple","orange"],file)
