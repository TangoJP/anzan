# Execute Anzan Program

import os
import functions as func

num_questions = 10
max_level = 5

os.system('clear')
print("=====================================================")
print("Welcome to Anzan App. Challenge Computation by Heat!")
print("=====================================================")
yes_no = input("ARE YOU READY? y / n \n")

os.system('clear')
if yes_no != 'y':
    print("See you next time!")
else:
    level = 1
    total_score = 0

    while level <= max_level:
        os.system('clear')

        # Run a round of questions for that level
        score = func.display_AdditionQ(level, num_questions)
        total_score += score
        if score >= int(0.8 * num_questions):
            result = "PASSED"
        else:
            result = "FAILED"
        print("===================================")
        print("     YOUR RESULT IS OUT!")
        print("         Score: %d / %d" % (score, num_questions))
        print("      Total Score: %d / %d" % (total_score, level * num_questions))
        print("     You ", result, " Level %d" % level)
        print("===================================")
        print("")


        if result == "PASSED":
            if level == max_level:
                print("     YOU PASSED ALL THE LEVELS!")
                print("")
                print("         CONGRATULATIONS!")
                print("      Total Score: %d / %d" % (total_score, level * num_questions))
                print("")
                print("========= END OF GAME =============")
                print("")
                break
            else:
                level_up = input("Wanna Move On to the Next Level? y / n\n")
                if level_up != 'y':
                    print("SEE YOU NEXT TIME!")
                    print("")
                    break
                level += 1
        else:
            print("     END OF YOUR CHALLENGE :( ")
            print("")
            print("         Last Level Passed: %d" % (level-1))
            print("       Total Score: %d / %d" % (total_score, level * num_questions))
            print("      TRY AGAIN ANOTHER TIME!")
            print("")
            print("========= END OF GAME ==========")
            print("")
            break
