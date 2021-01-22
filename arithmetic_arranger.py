def arithmetic_arranger(problems, display_ans):
    problems = [ string.split(' ') for string in problems ]
    # problemDict = [{
    #     "top": problems[x][0],
    #     "operator": problems[x][1]
    #     "bottom": problems[x][2],
    #     "top_len": problems[x][0].length
    #     "bottom_len": problems[x][2].length
    #     "max_char_len": max(top_len, bot_len),
    #     "total_char_len": max_char_length + 2,
    #     "string_1": '{total_char_len - top_len * " "}{top}'
    #     "string_2": '{operator}{total_char_len - bottom_len - 1 * " "}{bottom}'
    #     "string_3": '{total_char_len * "-"}
    # }]
    # 
    # dont form the answer until after the dictionary array is filled
    # answer = [string_1, string_2, string_3, (string_4)]
    # return answer.join("\n")
    
    print("{0}  {1}  {2}  {3}".format(problems[0][0], problems[1][0], problems[2][0], problems[3][0]))
    return "done"

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
