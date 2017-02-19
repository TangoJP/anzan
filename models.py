import random

random.seed()

# class to hold user information
class Challenger():
    pass

# class for addition
class AddQuestion():

    def __init__(self, level):
        if level == 1:
            self.int1 = random.randint(1, 9)
            self.int2 = random.randint(1, 9)
            self.ans = self.int1 + self.int2
        elif level == 2:
            self.int1 = random.randint(10, 49)
            self.int2 = random.randint(10, 49)
            self.ans = self.int1 + self.int2
        elif level == 3:
            self.int1 = random.randint(10, 99)
            self.int2 = random.randint(10, 99)
            self.ans = self.int1 + self.int2
        elif level == 4:
            self.int1 = random.randint(10, 99)
            self.int2 = random.randint(100, 999)
            self.ans = self.int1 + self.int2
        elif level == 5:
            self.int1 = random.randint(100, 999)
            self.int2 = random.randint(100, 999)
            self.ans = self.int1 + self.int2
        else:
            print("Error: Level has to be and int between 1 & 5")

class SubtractionQuestion():

    def __init__(self, level):
        if level == 1:
            self.int1 = random.randint(1, 9)
            self.int2 = random.randint(1, 9)
            self.ans = self.int1 + self.int2
        elif level == 2:
            self.int1 = random.randint(10, 49)
            self.int2 = random.randint(10, 49)
            self.ans = self.int1 + self.int2
        elif level == 3:
            self.int1 = random.randint(10, 99)
            self.int2 = random.randint(10, 99)
            self.ans = self.int1 + self.int2
        elif level == 4:
            self.int1 = random.randint(10, 99)
            self.int2 = random.randint(100, 999)
            self.ans = self.int1 + self.int2
        elif level == 5:
            self.int1 = random.randint(100, 999)
            self.int2 = random.randint(100, 999)
            self.ans = self.int1 + self.int2
        else:
            print("Error: Level has to be and int between 1 & 5")
