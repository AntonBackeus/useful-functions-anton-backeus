import Strings.string as string

letters = {'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F', 'g':'G', 'h':'H', 'q':'Q', 'w':'W', 'r':'R', 't':'T', 'y':'Y', 'u':'U',
           'i':'I', 'o':'O', 'p':'P', 'å':'Å', 's':'S', 'j':'J', 'k':'K', 'l':'L', 'ö':'Ö', 'ä':'Ä', 'z':'Z', 'x':'X', 'v':'V', 'n':'N', 'm':'M'}

#For all the values in a dict format it as a normal sentence does. Capital letter to start and after every period and everything else lower letters.
def capitalizeAllValues(dict_):
    for key, value in dict_:
        dict_[key] = string.formatSentences(value)
    return dict_

#For all values in a dict format it with every separate "word" capitalized
def capitalizeAllValueWords(dict_):
    for key, value in dict_:
        dict_[key] = string.capitalizeAllWords(value)
    return dict_

#Makes all values in dict lower case
def dictlower(dict_):
    for key, value in dict_:
        if type(value) == str:
            dict_[key] = value.lower()
    return dict_

#Makes all values in dict upper case
def dictupper(dict_):
    for key, value in dict_:
        if type(value) == str:
            dict_[key] = value.upper()
    return dict_