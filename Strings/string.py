
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
    
def capitalizeAllSentences(string):
    if type(string) == str:
        words = string.strip().split()
        new_string = []
        sentance = True
        for word in words:
            if sentance:
                new_string.append(word.capitalize())
                sentance = False
            else:
                new_string.append(word.lower())
            if word[-1] == ".":
                sentance = True
        return " ".join(new_string)
    else:
        print("capitalizeAllSentences got a non string, please send a string! Returning original value.")
        return string


#Testing all the functions
def main():
    testing_string = "tEsTaR hur    dEt gÅr med DeT   HÄR.   Det ÄR lite   TEXt    "
    testing_number = 4397529
    print(capitalizeAllWords(testing_string))
    print(capitalizeAllWords(testing_number))
    print(capitalizeAllSentences(testing_string))
    print(capitalizeAllSentences(testing_number))

main()