class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, salary): # need to pass origin object to use 
        return  cls(friend_name, origin.school, salary)

    def friend(self, friend_name):
        # Return a new student called 'friend_name' in the same school as self
        return  Student(friend_name, self.school)

anna = Student('Anna', 'Oxford')

friend = anna.friend('Greg')

print(friend.name)
print(friend.school)

## Inheritance, WorkingStudent has all the classes of Student
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school) # inherit from super class
        self.salary = salary


jason = WorkingStudent("Anna", "Oxford", 20.00)

newStudent = WorkingStudent.friend(anna, "Greg")