from cv2 import cv2
from flask import Response
from emailSend import emailimg
from matplotlib import image
from sendSms import sendsms
import os


class process:
    
    frame=0
    def imgProcess(img,password):
        
        
        cv2.imshow('Original',img)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        facecascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')        #haarcascade file

        faces=facecascade.detectMultiScale(gray,
                                            scaleFactor=1.2,  #20% size resolution get reduce
                                            minNeighbors=5,
                                            minSize= (20,20)  #faces whose size is less than this get ignored
                                        )
        print("------------------------------------------------\n")
        print("           Total no. of People in Elevator......\n")  
        print(faces)
        print("No. OF People=",len(faces))

        img_data=[]
        if len(faces)>0:
            for (x,y,w,h) in faces:
                data=(x,y,x+w,y+h)
                cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)       # Draw rectangle on Face  
                cv2.imshow("Detected Image",gray)
                img_data.append(data) 

            length=[]
            breadth=[]
            total_dist=[]
            dist_flag=False

            if (len(faces) > 1 and len(faces) < 5) :    #if more than 4 faces detected,send mail and SMS  (or len(faces) < 5)
                for i in img_data:
                    length.append(i[0]/2)            #contains x axis info of image(x axis values)
                    breadth.append(i[1]/2)           #contains y axis info of image(y axis values)
    
                for i in range(len(faces)-1):        
                    for j in range(1,len(faces)):
                        if(i!=j): #this logic is being added to avoid the calculation of distance between you and yourself!   
                            distance=(((length[j]-length[i])**2)+((breadth[j]-breadth[i])**2))**0.5
                            distance=float(distance)*0.0264583333   #distance conversion px->cm 
                            total_dist.append((distance))


                            print("------------------------------------------------\n")
                            print("                Distance Between People......\n")
                            print(i,j)                                       #Pair of person on which distance is calculated
                            print('distance:',str(total_dist),'cm')          #This array consist of all the distances in pixels between each other
                        
                        
                        elif (i<50 for i in total_dist):         # Min. Distance between two people 
                            print("------------------------------------------------\n")
                            
                            print('         Social Distancing violated!!!!.........') 
                            
                            dist_flag=True
        
        
            if len(faces)>=5 or dist_flag==True :       # no of people > 5 and distance between people
                print('         Social Distancing violated!!!!.........')
                try: 
      
    # creating a folder named data 
                    if not os.path.exists('C:\\images'): 
                        os.makedirs('C:\\images') 
  
    # if not created then raise error 
                except OSError: 
                    print ('Error: Creating directory of data')
               
               
                name ='C:\\images\\frame' +str(process.frame) + '.jpg'  # creating file
                print ('Creating...' + name) 
                cv2.imwrite(name,gray)             # saving a file
                sendsms.sendSms(len(faces))        # sending SMS
                emailimg.sendEmail(name,password)  # sending Email
                process.frame +=1
        
        cv2.waitKey(1)
        return
           