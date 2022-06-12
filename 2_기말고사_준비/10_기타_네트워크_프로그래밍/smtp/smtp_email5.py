"""
   메일 보내기: 특정 폴더를 압축한 후 전송하기
"""
import smtplib
from email.message import EmailMessage
import zipfile
import os

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = "gksxorb147@gmail.com"
recipient = "gksxorb147@naver.com"
password = "#"

zf_name = "email.zip"  # 압출 파일 이름 (현재 디렉토리에 생성됨)
folder = 'test'  # 현재 디렉토리에 있는 압출할 폴더

# folder 하위의 모든 폴더와 파일을 zf_name으로 압축
zf = zipfile.ZipFile(zf_name, "w")
print("Zipping current dir", folder)
for dirs, subdirs, files in os.walk(folder):
    zf.write(dirs)
    for file in files:
        zf.write(os.path.join(dirs, file))
zf.close()

msg = EmailMessage()
msg["Subject"] = "Source Code"
msg["From"] = sender
msg["To"] = recipient

# 압축파일 메일에 첨부
with open(zf_name, "rb") as f:
    msg.add_attachment(f.read(),
                       maintype="application",
                       subtype="zip",
                       filename="e_mail.zip")

if __name__ == '__main__':
    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.login(sender, password)
    s.send_message(msg)
    s.quit()
    print("Success!")
