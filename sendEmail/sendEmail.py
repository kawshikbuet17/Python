# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("kawshik.tiwary@gmail.com", "") 
  
# message to be sent 
message = "Message_you_need_to_send"
  
# sending the mail 
s.sendmail("kawshik.tiwary@gmail.com", "kawshik.kumar.paul@gmail.com", message) 
  
# terminating the session 
s.quit() 