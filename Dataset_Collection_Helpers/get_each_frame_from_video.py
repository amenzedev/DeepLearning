import cv2
dir = ''
saving_dir = "images/"
imageSource = "1-on_1-off.mp4"
cap = cv2.VideoCapture(dir+imageSource)
i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite(saving_dir+imageSource+str(i)+".jpg",frame)
    i+=1
cap.release()
cv2.destroyAllWindows()