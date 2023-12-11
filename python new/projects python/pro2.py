import json
from difflib import get_close_matches
jsonfile = json.load(open("data1.json")) 
word=input("enter the word: ")

def check(d):
    d = d.lower()
    if d in jsonfile:
       return jsonfile[d]
    elif len(get_close_matches(d,jsonfile.keys())) > 0:
       choice = input("Did you mean %s, Enter Y for YES, N for NO" %get_close_matches(d,jsonfile.keys())[0])
       if choice == "Y" or "y":
            return jsonfile[get_close_matches(d,jsonfile.keys())[0]]
       elif choice=="N" or "n":
            return "The word doesn't exist"
       else:
            return "you enterd the wrong choice"
    else:
        return "The word is not available"

result=check(word)
if type(result)==list:
    for i in result:
        print(i)
else:
    print(result)

    