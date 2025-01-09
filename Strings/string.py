
#Capitalizing all words in the string sent in
def capitalizeAllWords(string):
    if type(string) == str:
        words = string.strip().split()
        new_string = []
        for word in words:
            new_string.append(word.capitalize())
        return " ".join(new_string)
    else:
        print("capitalizeAllWords got a non string, please send a string! Returning original value.")
        return string

#Formating a string to a sentence. Capital letter to start and after a period, everything else lower letters.
def formatSentences(string):
    if type(string) == str:
        words = formatPeriods(string).strip().split()
        new_string = []
        sentence = True
        for word in words:
            if sentence:
                new_string.append(word.capitalize())
                sentence = False
            else:
                new_string.append(word.lower())
            if word[-1] == '.':
                sentence = True
        return " ".join(new_string)
    else:
        print("capitalizeAllSentences got a non string, please send a string! Returning original value.")
        return string
    
#Formating periods to a format of no blank space before a period and a blankspace before a dot unless there is an additional dot after the first one.
def formatPeriods(string):
    if type(string) == str:
        loop = True
        while loop == True:
            endLoop = True
            for i, letter in enumerate(string):
                if letter == '.':
                    if string[i-1] == ' ':
                        string = string[0:i-1] + string[i:-1]
                        endLoop = False
                        break
                    elif i+1 < len(string):
                        if string[i+1] != ' ' and string[i+1] != '.':
                            string = string[0:i+1] + ' ' + string[i+1:-1]
                            endLoop = False
                            break
            if endLoop:
                loop = False
    return string


#Testing all the functions
def main():
    testing_string = "tEsTaR hur    dEt gÅr med DeT   HÄR ..  .Det ÄR lite   TEXt.    "
    testing_number = 4397529
    print(capitalizeAllWords(testing_string))
    print(capitalizeAllWords(testing_number))
    print(formatSentences(testing_string))
    print(formatSentences(testing_number))
    print(formatPeriods(testing_string))

main()