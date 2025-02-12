import os
import subprocess

# Dasturlarni joylashgan papkalar
program_directories = [
    "C:\\Program Files",  # 64-bit ilovalar
    "C:\\Program Files (x86)",  # 32-bit ilovalar
    "C:\\Windows\\System32",  # Windows tizim dasturlari
]

# Papkada mavjud bo'lgan barcha fayllarni tekshirish
def get_installed_programs():
    programs = []
    for directory in program_directories:
        try:
            # Papkada fayllarni o'qish
            for filename in os.listdir(directory):
                # Dastur fayllarini faqat .exe kengaytmasiga ega bo'lganlarini olish
                if filename.endswith(".exe"):
                    program_path = os.path.join(directory, filename)
                    programs.append(program_path)
        except FileNotFoundError:
            print(f"{directory} papkasi topilmadi.")
        except PermissionError:
            print(f"{directory} papkasiga kirish imkoni yo'q.")
    return programs

# Foydalanuvchidan ilova nomini olish va ishga tushirish
def open_program(program_name):
    programs = get_installed_programs()
    for program in programs:
        if program_name.lower() in program.lower():  # Ilova nomini qidirish
            print(f"Ochilyapti: {program}")
            subprocess.Popen([program])
            return
    print(f"Bu ilova topilmadi: {program_name}")

# Python dasturini boshqarish uchun buyruqlarni qabul qilish
def main():
    while True:
        command = input("Ilova nomini kiriting (exit uchun 'exit' deb yozing): ").lower()

        if command == "exit":
            print("Dasturdan chiqyapti...")
            break
        else:
            open_program(command)

# Asosiy dastur funksiyasini chaqirish
if __name__ == "__main__":
    main()
