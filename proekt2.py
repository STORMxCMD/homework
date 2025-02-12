import cv2
from fer import FER

# Haar Cascade classifier uchun oldindan tayyorlangan modelni yuklash
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamera bilan ulanish
cap = cv2.VideoCapture(0)

# FER yuzni aniqlash uchun modelni yaratish
detector = FER()

while True:
    ret, frame = cap.read()  # Kamera orqali tasvir olish
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Rangni kulrangga aylantirish

    # Yuzlarni aniqlash
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    for (x, y, w, h) in faces:
        # Har bir yuzni ramkaga olish
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Aniqlangan yuz tasvirini FER ga yuborish
        face_roi = frame[y:y+h, x:x+w]  # Yuz qismini kesib olish
        emotion, score = detector.top_emotion(face_roi)  # His-tuyg'ularni aniqlash

        # Natijani ko'rsatish
        text = f"{emotion}: {score:.2f}" if emotion else "No emotion detected"
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Natijani ko‘rsatish
    cv2.imshow('Face and Emotion Detection', frame)

    # "q" tugmasini bosish orqali dasturni to‘xtatish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
