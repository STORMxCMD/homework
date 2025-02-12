import cv2

# Haar Cascade classifier uchun oldindan tayyorlangan modelni yuklash
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamera bilan ulanish
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Kamera orqali tasvir olish
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Rangni kulrangga aylantirish

    # Yuzlarni aniqlash
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    # Har bir yuzni ramkaga olish
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Natijani ko‘rsatish
    cv2.imshow('Face Detection', frame)

    # "q" tugmasini bosish orqali dasturni to‘xtatish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

from fer import FER
detector = FER()

# Yuzni aniqlashdan so‘ng, tasvirdagi his-tuyg‘ularni aniqlash
emotion, score = detector.top_emotion(frame)
print(f"Emotion: {emotion}, Score: {score}")
