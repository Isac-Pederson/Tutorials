import json

data = json.load(open("data.json"))

def getDef(word):
    if word in data:
        return data[word.lower()]
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ").lower()

print(getDef(word))

