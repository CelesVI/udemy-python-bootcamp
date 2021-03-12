import json
from difflib import get_close_matches

data = json.load(open("dict.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead?" %get_close_matches(word, data.keys())[0])
        decide = input("Press y for yes or n for no: ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            print("Wrong word or word not in the dictionary. Please enter another word")
        else:
            print("Wrong word or word not in the dictionary. Please enter another word")            
    else:
        print("Wrong word or word not in the dictionary. Please enter another word")

word = input("Enter the word to find: ")
output = translate(word)

for item in output:
    print(item)

