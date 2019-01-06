from Secret_santa import obtain_names_emails_from_file,randomize_names
from emails_sender import send_email

#Select a random seed here if you would like
seed = 42 

#Use Secret_santa module to conduct selection
contact_list = obtain_names_emails_from_file()
selection = randomize_names(contact_list)

#Use emails_sender module to send emails 
for santa in selection:
    send_email(santa,selection[santa],contact_list)
print("Completed")

