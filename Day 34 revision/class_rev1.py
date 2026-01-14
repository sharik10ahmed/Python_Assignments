class father:
      father_property="House"
      
      def Father_assets(self):
          print("Bhardwaj apartment")
          print("hotels")
class son(father):
      son_1st_property = "restaurant"
son_obj = son()

print(son_obj.son_1st_property)
print(son_obj.father_property)
son_obj.Father_assets()
