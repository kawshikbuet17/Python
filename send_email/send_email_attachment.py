import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass


def sendEmail(sender_email = "kawshik.kumar.paul@gmail.com"):
    print('Sender Email : ', sender_email)
    receiver_email = input('Receiver Email : ')
    subject = input('Subject : ')
    receiver_name = input('Dear ? ')
    body = "Dear "+ receiver_name + ",\n\nHope you are quite well by the grace of Almighty.\n\n"
    content = input('Email Content : ')
    body = body + content
    body = body + "\n\nKawshik Kumar Paul\n1705043\nBUET CSE'17\n"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    attach = input('Attach File? (y/n) => ')
    if(attach=='y'):
        print("Filename like : document.zip, document.pdf etc")
        try:
            filename = input('Type filename : ')
            #filename = "document.zip"  # In same directory as script

            # Open file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            
            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)


            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )


            # Add attachment to message and convert message to string
            message.attach(part)
            attach = "ok"
        except:
            attach = "notok"
            print("Attachment Failure")
    
    print('\n-----Sending this Email-----')
    print(body)
    if attach == "ok":
        print("Attachment : " + filename +"\n")
    
    print('-----Sending this Email-----\n')
    password = getpass.getpass()

    # Log in to server using secure context and send email
    try:
        text = message.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        print("Successfully sent email to "+ receiver_email + "\n")
    except:
        print("Some error occured")

def main():
    sendEmail('kawshik.tiwary@gmail.com')

if __name__ == "__main__":
    main()