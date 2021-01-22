def arithmetic_arranger(problems, display_ans):
    problems = [ string.split(' ') for string in problems ]
    
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
#              4      6        6       6         1    4     4    4  1   4    2    

