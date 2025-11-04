import cv2
import time
import os
import sys

# Use relative path for cascade classifier
cascade_path = os.path.join(os.path.dirname(__file__), 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cascade_path)

# Check if cascade classifier loaded successfully
if face_cascade.empty():
    print(f"Error: Could not load cascade classifier from {cascade_path}")
    sys.exit(1)

camera = cv2.VideoCapture(0)

# Check if camera opened successfully
if not camera.isOpened():
    print("Error: Could not open camera")
    sys.exit(1)

for i in range(1):
     return_valve, image = camera.read()

     # Check if frame was captured successfully
     if not return_valve:
         print("Error: Failed to capture image from camera")
         camera.release()
         sys.exit(1)
     # Create TrainingData directory if it doesn't exist
     training_dir = os.path.join(os.path.dirname(__file__), 'TrainingData')
     os.makedirs(training_dir, exist_ok=True)
     # Use os.path.join for cross-platform compatibility
     img_path = os.path.join(training_dir, f"Trainimg.{i}.jpg")
     cv2.imwrite(img_path, image)
     img = cv2.imread(img_path)
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
     print (len(faces))
     time.sleep(6)
del(camera)