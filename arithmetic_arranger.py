def arithmetic_arranger(problems, display_ans):
    problems = [ string.split(' ') for string in problems ]
    
    for problem in problems:
        problem.append(len(problem[0]))
        problem.append(len(problem[2]))
        problem.append(max(problem[3], problem[4]))
        problem.append(problem[5] + 2)
        problem.append('{spaces}{top}'.format(spaces = (problem[6] - problem[3]) * " ", top = problem[0]))
        problem.append('{operator}{spaces}{bottom}'.format(operator = problem[1], spaces = (problem[6] - problem[4] - 1) * " ", bottom = problem[2]))
        problem.append('{hypen}'.format(hypen = problem[6] * "-"))
        problem.append(str(eval(problem[0] + problem[1] + problem[2])))
        problem.append('{spaces}{answer}'.format(spaces = (problem[6] - len(problem[10])) * " ", answer = problem[10]))

    string_list = [
        "    ".join(problem[7] for problem in problems),
        "    ".join(problem[8] for problem in problems),
        "    ".join(problem[9] for problem in problems),
    ]
    
    ans_string = "    ".join(problem[11] for problem in problems)
    
    formatted_string = "\n".join(string_list)
    
    if display_ans == True:
        return formatted_string + '\n' + ans_string
    else:
        return formatted_string
    

# notes:
# number of hyphens "-" is determined by the longest number of digits by numerator opertor or answer, and add two.
#   for example "380 + 50 = 430" longest number is 3 digits, so use 5 hypens. 
#    380
#   + 50
#  -----
#    430
# 
# but how are the spaces determined?
#   ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
# expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
#              4      6        6       6         1    4     4    4  1   4    2          4         4       4
# 
# ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]
# my expection:
# expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    "
# actual exppectation:
# expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
# [top, bot, max, total]
# 11 + 4 => [2, 1, 2, 4]
# '{total - top * " "}{11}\n{+}{total-bot-1 * " "}{bot}\n{total * "-"}'


    # problemDict = [{
    #     "top": problems[x][0],
    #     "operator": problems[x][1]
    #     "bottom": problems[x][2],
    #     "top_len": problems[x][0].length
    #     "bottom_len": problems[x][2].length
    #     "max_char_len": max(top_len, bot_len),
    #     "total_char_len": max_char_length + 2,
    #     "string_1": '{total_char_len - top_len * " "}{top}',
    #     "string_2": '{operator}{total_char_len - bottom_len - 1 * " "}{bottom}',
    #     "string_3": '{total_char_len * "-"}
    # }]
    # 
    # dont form the answer until after the dictionary array is filled
    # answer = [string_1, string_2, string_3, (string_4)]
    # return answer.join("\n")
