from .confusableLetterCodes import confusableLetterCodes

confusable = confusableLetterCodes()

def wordIsMixOfConfusableAndLatinLetters(word):
    latinLetterExist = False
    confusableLetterExist = False
    for char in word:
        if ord(char) >= 65 and ord(char) <= 122:
            latinLetterExist = True
            if latinLetterExist == True and confusableLetterExist == True:
                return True
        elif ord(char) in confusable:
            confusableLetterExist = True
            if latinLetterExist == True and confusableLetterExist == True:
                return True
    return False