import json  # to read JSON data File
import difflib  # this lib has function to get_close_matches to get close matches


with open("data.json","r") as read_file:
    data=json.load(read_file)     #reading json file
word=input("enter a word")
word=word.lower()    #converting word to lower case letters

try:
    print(data[word])  #word meaning is printed
except:
    print("oops word not found")
    print("DId you mean :-",difflib.get_close_matches(word,data))
    #if your word is wrong then some suggestions are given