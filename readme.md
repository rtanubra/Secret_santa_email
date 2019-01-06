Simple Secret Santa App:
1. Takes input of {name:email} AND random Seed number
    -Random seed is used to be able to revisit a specific selection.
2. Selects the names in secret
3. Sends emails out to each user of each santa's chosen selection

How To use:
Necessary inputs and creation. 
1. Create the following files : (This will house the necessary inputs)
        /inputs/Names_emails.csv
        File should look like the following:
            Name,Email
            name1,email1
            name2,email2
            name3,email3

        /inputs/user_email.txt
            user_email@gmail.com
            password
    1.-Note see sample inputs for "sample inputs to create"

2. Initiate using run_me.py 
    -Utilizes Secret_santa module to conduct santa selection
    -Utilizes emails_sender module to send emails out to each santa

Dependencies:
1. pandas - to work with CSV
2. Gmail Account to act as your Elf King of santas. 
    -this app will utilize the created email to send emails from 
    -once created and submissions sent it is a good idea not to login to this email. 
        -sent folder of this email will display the selection and may ruin the surprise :9

Creating a Gmail Account:
1. Create a dedicated gmail account for this application
2. To allow this application to send emails through the new email follow these steps:
    - go into email settings
    - security
    - Less secure app access 
        - turn this on. Run the app. THEN for your own safety turn this back off.
3. Store email username and password
    /inputs/user_email.txt
    should take the following format below. See sample_inputs/user_email.txt for sample
        user_email@gmail.com
        password
    