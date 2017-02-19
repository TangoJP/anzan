# functions to run Anzan Apps
from models import AddQuestion, SubtractQuestion
import os

def display_Questions(level, num_questions, qtype):

    score = 0
    counter = 0

    while counter < num_questions:

        if qtype == 'add':
            question = AddQuestion(level)
            sign = '+'
        elif qtype == 'subtract':
            question = SubtractQuestion(level)
            sign = '-'
        else:
            question = AddQuestion(level)

        while True:
            print("-------------------------")
            print("Level %d : Question # %d" % (level, counter+1))
            print("-------------------------")
            question_text = "    %d %s %d = " % (question.int1, sign, question.int2)
            answer = input(question_text)
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
