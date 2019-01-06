"""
Takes names and emails from the input to obtain the selection.
Module input:
1. names and emails
    inputs/names_emails.csv 
        Name,email
        name1,email1
        name2,email2
        name3,email3
2. Dictionaries:
    2a.Selection dictionary: {santa:kid}
    2b.Contact list: {name:email}

"""
def obtain_names_emails_from_file():
    import pandas as pd 
    df = pd.read_csv("inputs/names_emails.csv")
    names = list(df["Name"])
    emails = list(df["Email"])
    my_dict = {}
    for i,name in enumerate(names):
        my_dict[name] = emails[i]
    return my_dict

def randomize_names(my_dict,seed = 42):
    import random 
    random.seed(seed)
    santas = list(my_dict.keys())
    kids = list(my_dict.keys())
    my_selection = {}
    while len(santas) >0:
        santa = santas.pop(0)
        possible_kid = kids[random.randint(0,len(kids)-1)]
        counter = 0
        while santa == possible_kid and counter < 50:
            possible_kid = kids[random.randint(0,len(kids)-1)] 
            counter += 1 #stop from crashing if we go into an impossible situation
        my_selection[santa] = possible_kid
        kids.remove(possible_kid)
    return my_selection

