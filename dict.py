import json
from difflib import get_close_matches

data = json.load(open("Interactive-English-Dictionary\data.json"))

def getDef(word):
    if word in data:
        return data[word.lower()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else: 
            return "We didn't understand your query."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ").lower()

output = (getDef(word))

if type(output) == list: 
    for item in output:
        print(item)
else:
    print(output)