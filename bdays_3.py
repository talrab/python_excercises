import json
from collections import Counter

with open("Bdays_3.json",'r') as f:
    bdays_dictionary = json.load(f)

print (bdays_dictionary)
print(bdays_dictionary["Romi"])
print(bdays_dictionary["Romi"]["Day"])

print('Welcome to the birthday dictionary. We know the birthdays of:\n')
for name in bdays_dictionary.keys():
    print (name + ': ' +
           bdays_dictionary[name]["Day"] + ' ' +
           bdays_dictionary[name]["Month"] + ' ' +
           bdays_dictionary[name]["Year"])


while (True):
    answer = input("\nYou can either:\n"
                   "(1) Query for a name\n"
                   "(2) Enter a new one.\n"
                   "(3) Count bdays months.\n"
                   "what will it be ?")
    if (answer=='1'):
        input_name = input("Who's birthday do you want to look up?\n")
        if (input_name in bdays_dictionary):
            print (input_name + ' birthday is in: ' + bdays_dictionary[input_name]["Day"] + ' ' + bdays_dictionary[input_name]["Month"] + ' ' + bdays_dictionary[input_name]["Year"])
        else:
            print("Sorry, we don't know this name...")
    elif (answer=='2'):
        new_name = input("Please enter a name:\n")
        new_date_day = input("Please enter the birthday's day of the month:\n")
        new_date_month = input("Please enter the birthday's month of the year:\n")
        new_date_year = input("Please enter the birthday's year:\n")
        bdays_dictionary[new_name]={"Day":new_date_day,"Month":new_date_month,"Year":new_date_year}
        with open("Bdays_3.json",'w') as f:
            json.dump(bdays_dictionary,f)
    elif (answer=='3'):
        months = []
        for name in bdays_dictionary.keys():
            months.append(bdays_dictionary[name]["Month"])
        c = Counter(months)
        print (c)
    else:
        print ("Please enter either '1' or '2' or '3'")


