import webbrowser
import subprocess

# Google'ni ochish
def open_google():
    webbrowser.open('https://www.google.com')
    print("Google sayti ochildi!")

# YouTube'ni ochish
def open_youtube():
    webbrowser.open('https://www.youtube.com')
    print("YouTube sayti ochildi!")

# Facebook'ni ochish
def open_facebook():
    webbrowser.open('https://www.facebook.com')
    print("Facebook sayti ochildi!")

# Instagram'ni ochish
def open_instagram():
    webbrowser.open('https://www.instagram.com')
    print("Instagram sayti ochildi!")

# Notepad ilovasini ochish
def open_notepad():
    subprocess.Popen(['notepad.exe'])
    print("Notepad ochildi!")

# Calculator ilovasini ochish
def open_calculator():
    subprocess.Popen(['calc.exe'])
    print("Calculator ochildi!")

# Command Prompt (cmd) ni ochish
def open_cmd():
    subprocess.Popen(['cmd.exe'])
    print("Command Prompt ochildi!")

# Google Chrome ni ochish
def open_chrome():
    subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'])
    print("Google Chrome ochildi!")

# Visual Studio Code ni ochish
def open_vscode():
    subprocess.Popen(['C:\\Program Files\\Microsoft VS Code\\Code.exe'])
    print("Visual Studio Code ochildi!")

# Python ni ishga tushirish
def open_python():
    subprocess.Popen(['python'])
    print("Python ishlayapti!")

# Python dasturini boshqarish uchun buyruqlarni qabul qilish
def main():
    while True:
        # Foydalanuvchidan buyruq olish
        command = input("Buyruq kiriting (googlega kirish, youtube ochish, facebook ochish, instagram ochish, notepad ochish, calculator ochish, cmd ochish, chrome ochish, vscode ochish, python ochish, exit): ").lower()

        if command == 'googlega kirish':
            open_google()

        elif command == 'youtube ochish':
            open_youtube()

        elif command == 'facebook ochish':
            open_facebook()

        elif command == 'instagram ochish':
            open_instagram()

        elif command == 'notepad ochish':
            open_notepad()

        elif command == 'calculator ochish':
            open_calculator()

        elif command == 'cmd ochish':
            open_cmd()

        elif command == 'chrome ochish':
            open_chrome()

        elif command == 'vscode ochish':
            open_vscode()

        elif command == 'python ochish':
            open_python()

        elif command == 'exit':
            print("Dasturdan chiqyapti...")
            break

        else:
            print("Noto'g'ri buyruq! Iltimos, qayta urinib ko'ring.")

# Asosiy dastur funksiyasini chaqirish
if __name__ == '__main__':
    main()
