
class students():

    def __init__(self, age,name):
        self.age = age
        self.name = name


Students = students(35,"Hope")

print(f"Hello {Students.name} you are {Students.age}")