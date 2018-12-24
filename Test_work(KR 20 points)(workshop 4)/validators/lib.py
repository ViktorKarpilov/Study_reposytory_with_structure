
"""
    Написати валідатор ....
    Правило валідації
"""

import re

def getUserEmail():

    user_input = input()

    if (re.match(r"?", user_input) ):
        return user_input
    else:
        return False


"""
    Написати валідатор ....
    Правило валідації
"""

def getCar():
    user_input = input("Enter a car number : ")

    if (re.match(r"[A-Z]{4}\-[0-9]{4}", user_input)):
        return user_input
    else:
        return False

def getCompetition():
    user_input = input("Enter a competition : ")
    if (re.match(r"[A-Z]", user_input)):
        return False
    elif(re.match(r"[0-9]", user_input)):
        return False
    elif(re.match(r"[a-z]+(\s[a-z])?", user_input)):
        if re.match(r"[a-z]+[A-Z]", user_input):
            return False
        elif re.match(r"[a-z]+\s[a-z]+\s", user_input):
            return False
        elif re.match(r"[a-z]+\s[a-z]*[A-Z]", user_input):
            return False
        return  user_input
    return False

def getResults():
    user_input = input("Enter results : ")

    if (re.match(r"\[[0-9]{2}\.[0-9]{2}\]", user_input)):
        return user_input
    else:
        return False

if __name__ == '__main__':
    while True:
        print(getCar())

"""
    Написати валідатор ....
    Правило валідації
"""


