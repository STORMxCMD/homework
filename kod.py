import qrcode
import cv2
from pyzbar.pyzbar import decode
import numpy as np

# QR-kod yaratish funksiyasi
def create_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save("qr_code.png")
    print("QR-kod yaratildi va 'qr_code.png' nomi bilan saqlandi.")

# QR-kodni skanerlash funksiyasi
def scan_qr_code():
    cap = cv2.VideoCapture(0)
    
    print("QR-kodni skanerlash uchun telefon yoki kamerani to'g'rilab tuting...")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        decoded_objects = decode(frame)
        
        for obj in decoded_objects:
            print(f"QR-kod ma'lumotlari: {obj.data.decode('utf-8')}")
            points = obj.polygon
            if len(points) == 4:
                pts = np.array(points, dtype=np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(frame, [pts], True, (0, 0, 255), 5)
        
        cv2.imshow("QR-kod skanerlash", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Asosiy dastur
def main():
    print("1. QR-kod yaratish")
    print("2. QR-kodni skanerlash")
    choice = input("Tanlovni kiriting (1 yoki 2): ")

    if choice == '1':
        data = input("QR-kod uchun matn yoki havola kiriting: ")
        create_qr_code(data)
    elif choice == '2':
        scan_qr_code()
    else:
        print("Noto'g'ri tanlov. Dastur tugatilmoqda.")

# Dastur ishga tushadi
if __name__ == "__main__":
    main()


# import cv2
# from pyzbar.pyzbar import decode

# def scan_qr_code():
#     # Kamera ochish
#     cap = cv2.VideoCapture(0)
    
#     print("QR-kodni skanerlash uchun telefon yoki kamerani to'g'rilab tuting...")
    
#     while True:
#         ret, frame = cap.read()  # Kameradan tasvir olish
#         if not ret:
#             break
        
#         # QR-kodlarni aniqlash
#         decoded_objects = decode(frame)
        
#         for obj in decoded_objects:
#             # QR-kod ma'lumotlarini ekranga chiqarish
#             print(f"QR-kod ma'lumotlari: {obj.data.decode('utf-8')}")
#             # QR-kodni ekranda belgilash
#             points = obj.polygon
#             if len(points) == 4:
#                 pts = np.array(points, dtype=np.int32)
#                 pts = pts.reshape((-1, 1, 2))
#                 cv2.polylines(frame, [pts], True, (0, 0, 255), 5)
        
#         # Ekranda tasvirni ko'rsatish
#         cv2.imshow("QR-kod skanerlash", frame)
        
#         # Qachonki 'q' tugmasini bosganda dastur to'xtaydi
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     cap.release()
#     cv2.destroyAllWindows()

# # QR-kodni skanerlash funksiyasini chaqirish
# scan_qr_code()

