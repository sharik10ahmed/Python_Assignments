class Student:

              student_name = "Wilmot"
              email = "wilmot@example.com"
              __atm_pin = 1234 # private variable

              def student_info(self):
                    print("Student name is :", self.student_name)
                    print("Student email :", self.email)

object_student = Student()  

object_student.student_info() # first method to call a function


my_functon = object_student.student_info
my_functon()    # second method to call  a funciton 

