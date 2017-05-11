
import json

with open("Bdays_2.json",'r') as f:
    bdays_dictionary = json.load(f)

print('Welcome to the birthday dictionary. We know the birthdays of:\n')
for name in bdays_dictionary.keys():
    print (name + ': ' + bdays_dictionary[name])

while (True):
    answer = input("\nYou can either:\n"
                   "(1) Query for a name\n"
                   "(2) Enter a new one.\n"
                   "what will it be ?")
    if (answer=='1'):
        input_name = input("Who's birthday do you want to look up?\n")
        if (input_name in bdays_dictionary):
            print (input_name + ' birthday is in: ' + bdays_dictionary[input_name])
        else:
            print("Sorry, we don't know this name...")
    elif (answer=='2'):
        new_name = input("Please enter a name:\n")
        new_date = input("Please enter a birthday date:\n")
        bdays_dictionary[new_name]=new_date
        with open("Bdays_2.json",'w') as f:
            json.dump(bdays_dictionary,f)
    else:
        print ("Please enter either '1' or '2'")




