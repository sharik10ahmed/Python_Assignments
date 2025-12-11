class grandfather:
    grandfather_property="Hotel BY"
    def Grandfather_Assets(Self):
        print("His Property")
class Father(grandfather):
    father_property="Lambo"
    def Father_Assets(Self):
        print("Houses")

obj_of_Father= Father()
print(obj_of_Father.father_property)
obj_of_Father.Father_Assets()
print(obj_of_Father.grandfather_property)
obj_of_Father.Grandfather_Assets()