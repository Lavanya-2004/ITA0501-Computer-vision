import cv2
import os
cam = cv2.VideoCapture(r"E:\cv lab\animal1.mp4")  
try:
 # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
# frame
currentframe = 0
  
while(True):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
  
        # writing the extracted images
        cv2.imwrite(name, frame)
  
        currentframe += 1
    else:
        break
  cam.release()
cv2.destroyAllWindows()
