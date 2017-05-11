

bdays_dictionary = {}
fr = open('Bdays.txt','r')
for line in fr.readlines():
    name,date = line.split(',')
    bdays_dictionary[name]=str(date).strip()

print('Welcome to the birthday dictionary. We know the birthdays of:')
for name in bdays_dictionary.keys():
    print (name + ': ' + bdays_dictionary[name])
while (True):
    input_name = input("Who's birthday do you want to look up?\n")
    if (input_name in bdays_dictionary):
        print (input_name + ' birthday is in: ' + bdays_dictionary[input_name])
    else:
        print("Sorry, we don't know this name...")




