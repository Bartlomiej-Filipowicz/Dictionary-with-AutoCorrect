import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()

    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input('Did you mean %s instead? Enter y if yes and n if no: ' % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'n':
            return 'There is no such word in the dictionary :('
        else:
            return "We didn't understand your entry"
    else:
        return 'There is no such word in the dictionary :('

word = input('Enter word: ')

output = translate(word)

if type(output) == list:
    for num in range(len(output)):
        print(num+1, end='. ')
        print(output[num])
else:
    print(output)