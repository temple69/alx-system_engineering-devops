import os
files=['0-simply_match_school.rb','1-repetition_token_0','100-textme','2-repetition_token_1','3-repetition_token_2','4-repetition_token_3','5-beginning_and_end','6-phone_number','7-OMG_WHY_ARE_YOU_SHOUTING'

]
def createfile(arr):
    for i in range(len(arr)):
       open(f'{os.getcwd()}/{arr[i]}.rb','x')

createfile(files)  