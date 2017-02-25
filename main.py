# Execute Anzan Program

import os
import functions as func

num_questions = 3
max_level = 2

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
        score = func.display_Questions(level, num_questions, 'subtract')
        total_score += score
        if score >= int(0.8 * num_questions):
            result = "PASSED"
        else:
            result = "FAILED"
        func.display_round_result(level, num_questions, score, total_score, result)

        if result == "PASSED":
            if level == max_level:
                func.display_all_levels_passed(level, num_questions, total_score)
                break
            else:
                level_up = input("Wanna Move On to the Next Level? y / n\n")
                if level_up != 'y':
                    print("SEE YOU NEXT TIME!")
                    print("")
                    break
                level += 1
        else:
            func.display_levels_incomplete(level, num_questions, total_score)
            break
