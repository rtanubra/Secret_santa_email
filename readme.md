Simple Secret Santa App:
1. Takes input of {name:email} AND random Seed number
    -Random seed is used to be able to revisit a specific selection.
2. Selects the names in secret
3. Sends emails out to each user of each santa's chosen selection

How To use:
Necessary inputs and creation. 
1.Create the following files : (This will house the necessary inputs)
        /inputs/Names_emails.csv
        File should look like the following:
            Name,Email
            name1,email1
            name2,email2
            name3,email3

        /inputs/user_email.txt
            user_email@gmail.com
            password
        
2.Initiate using run_me.py 
    -runs Secret_santa.py to make necessary selection.
    -runs emails.py to send the necessary emails.

Dependencies:
1. pandas - to work with CSV