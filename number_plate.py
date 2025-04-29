import cv2
import easyocr,os
import warnings 
warnings.filterwarnings('ignore')
reader = easyocr.Reader(['en']) 
harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640) # width
cap.set(4, 480) #height

min_area = 500
count = 0

while True:
    success, img = cap.read()
    if not success:
        break 

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            detected_plate =  img[y:y+h,x:x+w]
            result = reader.readtext(detected_plate)
            cv2.putText(img, f"Plate : {result[0][-2]}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y+h, x:x+w]
        cv2.imshow("ROI", img_roi)
cap.release()
k = cv2.waitKey(0) 
if k == ord('q'):
    cv2.destroyAllWindows()


