class Student:
    def __init__(self, id, name, testScore):
        self.id = id
        self.name = name
        self.testScore = testScore

    def display(self):
        print(self.id, self.name, self.testScore)
