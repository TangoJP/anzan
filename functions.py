# functions to run Anzan Apps
from models import AddQuestion
import os

def display_AdditionQ(level, num_questions):

    score = 0
    counter = 0

    while counter < num_questions:
        question = AddQuestion(level)
        while True:
            print("-------------------------")
            print("Level %d : Question # %d" % (level, counter+1))
            print("-------------------------")
            answer = input("    %d + %d = " % (question.int1, question.int2))
            if answer.isdigit():
                answer = int(answer)
                break
            else:
                os.system('clear')
                print("Answer Must be an Integer")
        if answer == question.ans:
            score += 1
        counter += 1
        os.system('clear')

    return score
