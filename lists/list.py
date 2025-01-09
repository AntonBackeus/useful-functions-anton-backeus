import Strings.string as string

#For all the values in a list format it as a normal sentence does. Capital letter to start and after every period and everything else lower letters.
def capitalizeAllValues(list):
    for i, value in enumerate(list):
        list[i] = string.formatSentences(value)
    return list

#For all values in a list format it with every separate "word" capitalized
def capitalizeAllValueWords(list):
    for i, value in enumerate(list):
        list[i] = string.capitalizeAllWords(value)
    return list

#Makes all the values in a list lower case
def listlower(list):
    for i, value in enumerate(list):
        if type(value) == str:
            list[i] = value.lower()
    return list

#Makes all the values in a list upper case
def listupper(list):
    for i, value in enumerate(list):
        if type(value) == str:
            list[i] = value.upper()
    return list