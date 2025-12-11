class grandfather:
    grandfather_property="Hotel BY"
    def Grandfather_Assets(Self):
        print("His Property")
class Father(grandfather):         #First Level
    father_property="Lambo"
    def Father_Assets(Self):
        print("Houses")

class Son(Father):                 #Second Level
    Son_Property="Nothing"
    def Son_Assets(Self):
        print("Nothing Special")


obj_father= Father()
print(obj_father.grandfather_property)
obj_father.Grandfather_Assets()
print(obj_father.father_property)
obj_father.Father_Assets()

obj_son = Son()
print(obj_son.grandfather_property)
obj_son.Grandfather_Assets()
print(obj_son.father_property)
obj_son.Father_Assets()
obj_son.Son_Assets()
print(obj_son.Son_Property)

print("This is the end")

