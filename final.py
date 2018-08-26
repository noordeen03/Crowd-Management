import cv2
import time
face_cascade = cv2.CascadeClassifier('E:\Counting-number-of-faces-in-a-picture-using-python-opencv-master\haarcascade_frontalface_default.xml')
camera=cv2.VideoCapture(0)
for i in range(1):
     return_valve,image=camera.read()
     cv2.imwrite("TrainingData\Trainimg."+str(i)+".jpg",image)
     img = cv2.imread("TrainingData\Trainimg."+str(i)+".jpg")
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
     print (len(faces))
     time.sleep(6)
del(camera)