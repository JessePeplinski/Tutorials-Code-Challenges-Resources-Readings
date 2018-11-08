lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5,9,12,3,1,21)
}

class LotteryPlayer:
    def __init__(self, name): #self is like this 
        self.name = name 
        self.numbers = (5,9,12,3,1,21)
    
    def total(self):
        return sum(self.numbers)

player = LotteryPlayer("John") # create object from class. 

print(player.name)
print(player.numbers)
print(player.total())

player2 = LotteryPlayer("Ron")


###

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)
    
    # It doesn't matter who is calling this method, we don't need self.
    @classmethod # tels python we don't need self, and we pass the class Student to the function
    # or we could use @staticmethod if we aren't passing anything
    def go_to_school(cls):
        print('I am going to school')


anna = Student("Anna", "MIT")
anna.marks.append(56)
print(anna.marks)
print(anna.average())


