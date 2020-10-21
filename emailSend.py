import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from cv2 import cv2



class emailimg:
        
 
        def sendEmail(img,password):
                   
                smpt_server="smpt.gmail.com"
                sender_email="xxxxxx@gmail.com"  #user email
                receiver_email=['xxxxx@gmail.com','xxxxx@gmail.com'] #Receiver's email
                port=587
                
                print("------------------------------------------------\n")
                print("             Sending Email........\n")
                

                msg = MIMEMultipart()             #email text
                msg['Subject'] = 'subject'
                msg['To']   =', '.join(receiver_email)
                msg['From'] = 'xxxxxx@gmail.com'
                
                
                img_data = open(img, 'rb')        #sending img as text

                image = MIMEImage(img_data.read())
                img_data.close()
                msg.attach(image)

                server=smtplib.SMTP(smpt_server, port)
                server.starttls()
                server.login(sender_email,password)   #login to gmail account
                print("             login succesfull...........")

                for i in range (len(receiver_email)): #sending email
                        print(receiver_email[i])
                        server.sendmail(sender_email,receiver_email,msg.as_string())
                        print("           send succesfull.........")
                print("------------------------------------------------\n")
                server.quit()
        