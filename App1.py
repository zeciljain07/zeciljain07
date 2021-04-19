import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()

    # 1st condition for checking the correct input 
    if w in data:
        return data[w]
    
    #2nd conditon is to make sure the program returns the definiton of words that start with capital letters.
    elif w.title() in data:
        return data[w.title()]

    #3rd condition to make sure the programs outputs definition of Acronyms.

    elif w.upper() in data:
        return data[w.upper()]

    # 4th condition is for checking the closest match incase the input is wrong to a certain degree.    
    elif len(get_close_matches(w, data.keys())) >0:
        yn = input("Did you mean %s instead? \nEnter Y if yes ,or N if no:\n" % get_close_matches(w, data.keys())[0])  
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn =="N":
            yn1 = input("Did you mean %s instead? \nEnter Y if yes or N if no:\n" % get_close_matches(w, data.keys())[1])
            if yn1 =="Y":
                return data[get_close_matches(w, data.keys())[1]]
            elif yn =="N":
                return "The word doesn't exists. Please re-enter correct word."
        else :
            return "We didn't understand your entry."

    # 5th condition is for checking if the input is completely wrong and doesn't match any word to a favourable degree.
    else: 
        return "The the word doesn't exist. Please re-enter correct word."

word = input("Enter word:")

output = (translate(word))

if type(output) == list:
    for item in output:
        print (item)
else:
    print(output)