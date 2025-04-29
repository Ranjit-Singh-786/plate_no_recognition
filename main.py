import cv2
import easyocr
import warnings

warnings.filterwarnings('ignore')

# Load OCR reader and cascade model once
reader = easyocr.Reader(['en'])
harcascade = "model/haarcascade_russian_plate_number.xml"
plate_cascade = cv2.CascadeClassifier(harcascade)

# Open webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500

while True:
    success, img = cap.read()
    if not success:
        break

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h
        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            detected_plate = img[y:y + h, x:x + w]
            result = reader.readtext(detected_plate)

            if result:
                plate_text = result[0][-2]
                cv2.putText(img, f"Plate: {plate_text}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
                cv2.imshow("ROI", detected_plate)

    cv2.imshow("Video", img)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
