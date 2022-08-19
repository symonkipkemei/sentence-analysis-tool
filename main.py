
from curses.ascii import islower

print("***************SENTENCE ANALYSIS TOOL *****************")
user_input = input("Insert a text: ")

#create empty dict

items_dict= {"upper_case": 0, "lower_case": 0, "punctuation":0}
# loop through the sentence
count = 0
for item in user_input:
    #skip empty spaces
    if item != " ":
        if item.isupper():
            value = items_dict["upper_case"]
            items_dict["upper_case"] = value + 1
        elif item.islower():
            value = items_dict["lower_case"]
            items_dict["lower_case"] = value + 1
        #for punctuations
        else:
            value = items_dict["punctuation"]
            items_dict["punctuation"] = value + 1

print(f"Upper case:{items_dict['upper_case']} \nLower case {items_dict['lower_case']} \nPunctuation:{items_dict['punctuation']}")



print("********************************************************")