# Gmail > Settings > Security > App Access ON

import smtplib 
import getpass

def sendEmail(sender = "kawshik.kumar.paul@gmail.com"):
    print('Sender Email : ', sender)
    receiver = input('Receiver Email : ')

    subject = input('Subject : ')
    receiver_name = input('Dear ? ')
    content = input('Email Content : ')
    message_content = """\
Subject: {}

Dear {},
Hope you are quite well by the grace of Almighty.
{}

Regards
Kawshik Kumar Paul
BUET CSE'17 """
    message_content.format(subject, receiver_name, content)

    print('\n-----Sending this Email-----')
    print(message_content.format(subject, receiver_name, content))
    print('-----Sending this Email-----\n')

    password = getpass.getpass()
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login(sender, password) 
        s.sendmail(sender, receiver, message_content.format(subject, receiver_name, content)) 
        s.quit() 
        print('Email has been sent to '+ receiver + ' successfully.')
    except:
        print('Some error occured')

def main():
    sendEmail('kawshik.tiwary@gmail.com')

if __name__ == "__main__":
    main()