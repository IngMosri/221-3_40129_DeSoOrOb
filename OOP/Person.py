class Person:
    def __init__(self, id, first_name,last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        
    def __str__(self):
        return f"Person id:{self.id}, firstname: {self.first_name}, lastname: {self.last_name}"

person_one = Person(100, "Christian", "Rosales")
print(person_one)