class grandfather:
    grandfather_property="Hotel BY"
    def Grandfather_Assets(Self):
        print("His Property")
class Father:
    father_property="Lambo"
    def Father_Assets(Self):
        print("Houses")

class Son(grandfather,Father):
    Son_Property="Nothing"
    def Son_Assets(Self):
        print("Nothing Special")


obj_Son = Son()
print(obj_Son.grandfather_property)
obj_Son.Grandfather_Assets()
print(obj_Son.father_property)
obj_Son.Father_Assets()
print(obj_Son.Son_Property)
obj_Son.Son_Assets()

