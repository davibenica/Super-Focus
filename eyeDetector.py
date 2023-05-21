
# This will be a class used to detect the eyes of the use
import cv2
import time
import threading
import text

class EyeDetector:

    def __init__(self) -> None:
        
        self.eyes = []    #Initialize eyes when class is cotruscted
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.detectorON = False


    def CaptureFace(self,bool):
        cap = cv2.VideoCapture(0)

        self.detectorON = True
        
        while self.detectorON:
            ret, frame = cap.read()

            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            self.eyes = self.eye_cascade.detectMultiScale(gray,1.3,5)
            key = cv2.waitKey(1)

            if bool:
                cv2.imshow('Frame',frame)


            if key == ord('a'):
                return
        
    def isEyesDetected(self):
       
        if len(self.eyes) == 0:
            return False
                
        if len(self.eyes) > 0:

            return True

    def printEyes(self):
     while True:
        time.sleep(3)
        print(self.eyes)
    
    def turnDetectorOff(self):
        self.detectorON = False

    def StartDetector(self, Phone):

        # Starts detecting eyes

        text_bot = text.textBot(Phone)

        thread = threading.Thread(target = self.CaptureFace,args=(False,),)
        thread.start()
        time.sleep(5)
        while self.detectorON:
            if self.isEyesDetected() == False:
                # Waits 10 second to see if eyes are still not detected
                time.sleep(5)
                if not self.isEyesDetected():

                     text_bot.sendMessage("Get off your phone")
                     time.sleep(5)

        thread.join()
        return
         

            
            











    
        
        

