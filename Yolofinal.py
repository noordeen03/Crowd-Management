import cv2
import time
import subprocess
import sys
import os

i=1
while i<2:
    try:
        last = time.time()

        cap = cv2.VideoCapture(0)

        ret, frame = cap.read()

        # Convert to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB);

        # Use relative path for output image
        cam_jpg = os.path.join(os.path.dirname(__file__), 'cam.jpg')
        cv2.imwrite(cam_jpg, frame)

        # Build command with cross-platform paths
        darknet_path = os.path.join(os.path.dirname(__file__), 'darknet')
        cfg_path = os.path.join(os.path.dirname(__file__), 'cfg', 'yolov3.cfg')
        weights_path = os.path.join(os.path.dirname(__file__), 'yolov3.weights')
        cmd = f"{darknet_path} detect {cfg_path} {weights_path} {cam_jpg}"

        output = subprocess.check_output(cmd.split())

        output = output.decode("utf-8").split("\n")
        
        # Count the number of lines that contain "person"
        numPeople = len([i.split(":")[0] for i in output if i.split(":")[0] == 'person'])

        print(output[0])
        print("{}  people detected.".format(numPeople))

        # Use os.path.join for cross-platform compatibility
        restaurant_file = os.path.join(os.path.dirname(__file__), 'restaurant.txt')
        with open(restaurant_file, "a") as myfile:
            myfile.write("{},{}\n".format(last, numPeople))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        i=i+1

    # On keyboard interrupt, terminate program
    except KeyboardInterrupt:
        print("Program exiting")
        break

    # If an unknown exception occurs, print it and continue looping.
    except:
        print(sys.exc_info()[0])
        continue