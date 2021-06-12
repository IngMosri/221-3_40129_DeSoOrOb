class Teacher:
    
    def __init__(self,id, name, employee_id):
        self.id = id
        self.name = name
        self.employee_id = employee_id
    
teacher_one = Teacher(1, "Luis Guerra", 2021001)

print(teacher_one.id)
print(teacher_one.name)
print(teacher_one.employee_id)
        