from cv2 import cv2
from flask import Flask, Response, render_template
import os
from imgProc import process
import datetime

# app = Flask(__name__)
app = Flask(__name__)

class Stream:

    @app.route('/')
    def index():
        return render_template('index.html')

    def get_frame():
        
        camera_port = 0
        cam = cv2.VideoCapture(camera_port)
        password=input('Enter the Gmail password:')  # eneter gmail password
        while(True):
            ret,img=cam.read()
            
            font=cv2.FONT_ITALIC
            text=str(datetime.datetime.now())
            img=cv2.putText(img,text,(10,50),font,1,(0,255,255),2,cv2.LINE_4) # Add date and time on video

            imgencode=cv2.imencode('.jpg',img)[1]
            stringData = imgencode.tobytes()
            


            yield (b'--frame\r\n'
                b'Content-Type: Text/plain\r\n\r\n' + stringData +b'\r\n')   #stream on html page
            
            process.imgProcess(img,password)  # call to method

   
            
            
        cv2.waitKey(1)
        cam.release() 
        cv2.destroyAllWindows() 

    
    
    @app.route('/video_stream', methods=['GET', 'POST'])
    def video_stream():
        return Response(Stream.get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)
    
