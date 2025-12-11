class Student:

   student_name = "Sharik"  # this is local variable

   def student_info(self):
     print("Student name is :", self.student_name)


my_object = Student()  # creating object of class Student
print(my_object.student_name)   # Sharik
my_object.student_info()  # calling method of class Student