class father:
    father_1st_property="Taj Hotel"

    def father_assets(self):    
        print("Bhardwaj apartment")
        print("Willing Restaurant")

class son(father):
    son_1st_property = "minee restro"


son_obj = son()

print(son_obj.son_1st_property)
print(son_obj.father_1st_property)
son_obj.father_assets()