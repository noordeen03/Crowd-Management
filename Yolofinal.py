import cv2
# import time
import subprocess
import sys
i=1
while i<2:
    try:
        # last = time.time()

        cap = cv2.VideoCapture(0)

        ret, frame = cap.read()

        # Convert to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB);
       
        cv2.imwrite('cam.jpg', frame)
       
        cmd = "./darknet detect cfg/yolov3.cfg yolov3.weights cam.jpg"# optional flag: -thresh .2"

        output = subprocess.check_output(cmd.split())

        output = output.decode("utf-8").split("\n")
        
        # Count the number of lines that contain "person"
        numPeople = len([i.split(":")[0] for i in output if i.split(":")[0] == 'person'])

        print(output[0])
        print("{}  people detected.".format(numPeople))

        with open("restaurant.txt", "a") as myfile:
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