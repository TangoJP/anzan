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

def display_round_result(level, num_questions, score, total_score, result):
    print("===================================")
    print("     You ", result, " Level %d" % level)
    print("         Score: %d / %d" % (score, num_questions))
    print("      Total Score: %d / %d" % (total_score, level * num_questions))
    print("===================================")
    print("")

def display_all_levels_passed(level, num_questions, total_score):
    print("         CONGRATULATIONS!")
    print("     YOU PASSED ALL THE LEVELS!")
    print("")
    print("      Total Score: %d / %d" % (total_score, level * num_questions))
    print("")
    print("========= END OF GAME =============")
    print("")

def display_levels_incomplete(level, num_questions, total_score):
    print("    YOUR CHALLENGE IS OVER... :( ")
    print("")
    print("     Highest Level Passed: %d" % (level-1))
    print("       Total Score: %d / %d" % (total_score, level * num_questions))
    print("      TRY AGAIN ANOTHER TIME!")
    print("")
    print("========= END OF GAME ============")
    print("")
