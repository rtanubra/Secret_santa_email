import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(santa,kid,contact_list,wishlist=None):
    mail = smtplib.SMTP("smtp.gmail.com",587)
    with open("inputs/user_email.txt","r") as my_file:
        email_id = my_file.readline()
        password = my_file.readline()
    mail.ehlo()
    mail.starttls() #Encrypt login information
    mail.login(email_id, password)
    send_to = contact_list[santa]

    if wishlist == None:
        message_body = f"""
        Hello Santa {santa},

        {kid} has been a very good person this year!
        In Christmas, it is time for you to reward them with an awesome gift(s)!

        {kid} was so selfless they did not even create a 'want list...'
        Best of luck, and happy giving.

        Thank you,
        Rey's Secret Santa Application
        """
    
    else:
        message_body = f"""
        Hello Santa {santa},

        {kid} has been a very good person this year!
        In Christmas, it is time for you to reward them with an awesome gift(s)!

        Here are some of the things {kid} believes they would like for this coming Christmas:
        {wishlist}
        But, don't worry, feel free to be as creative as you would like.
        Best of lick, and happy giving. 

        Thank you,
        Rey's Secret Santa Application
        """
    #Start multimessage
    message = MIMEMultipart()

    #params: From, To Subject
    message["From"] = email_id
    message["To"] = send_to
    message["Subject"] = "Hello Santa, here is your person this Christmas!"

    #Params Body
    message.attach(MIMEText(message_body,"plain"))

    #send the email MIME multipart use .as_string() method
    mail.sendmail(email_id, send_to,message.as_string())
    mail.close()

"""
import Secret_santa as ss 
contact_list = ss.obtain_names_emails_from_file()
selection = ss.randomize_names(contact_list,42)
#send_email(santa,kid,contact_list,wishlist=None)
print(contact_list)
print(selection)
santa1 = "Rey Tanubrata"
send_email(santa1,selection[santa1],contact_list)
"""
