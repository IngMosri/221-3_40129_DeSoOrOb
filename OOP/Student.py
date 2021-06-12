class Student:
    
    id = 1
    name = "Christian Alejandro Rosales Alatorre"
    tuition = 2021001
   #methods

    def enroll_school(self):
        return "Welcome to univa"
    
    def enroll_carrer(self, carrer_name):
        return f"Welcome to {carrer_name}"
    

student_one = Student()

print(student_one.id)
print(student_one.name)
print(student_one.enroll_carrer("Ingeneria en sistemas"))
print(student_one.id)