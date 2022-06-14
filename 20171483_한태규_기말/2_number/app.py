"""
    1. SSH 서버 접속

"""
import getpass
import paramiko
import smtplib
from email.message import EmailMessage
import filetype  # 파일 유형을 판단해 주는 모듈

PORT = 22

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input("Username: ")
pwd = getpass.getpass('Password: ')

cli.connect("114.71.220.5",
            port=PORT,
            username=user,
            password=pwd)

stdin, stout, stderr = cli.exec_command("mkdir /home/net_pro/20171483")
lines = stout.readlines()
print("".join(lines))

stdin, stout, stderr = cli.exec_command("echo iot > iot.txt")
lines = stout.readlines()
print("".join(lines))

filename = "20171483.zip"  # 압축파일의 이름
dirname = "/home/net_pro/20171483"  # 압축할 폴더
CMD = f"zip -r {filename} {dirname}"  # 리눅스의 압축 명령어

stdin, stout, stderr = cli.exec_command(CMD)
lines = stout.readlines()
print("".join(lines))

# 파일 가져오기
sftp = cli.open_sftp()
sftp.get(filename, filename)
sftp.close()
cli.close()

# ------------------------ 메일 전송 ------------------------ #

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# 이메일 파일 첨부 파일로 전송
sender = "gksxorb147@gmail.com"
password = "<google app 비밀번호>"

family = [
    "gksxorb147@nate.com",
    "gksxorb147@naver.com",
]

msg = EmailMessage()
msg["Subject"] = "네트워크 프로그래밍 기말고사"
msg["From"] = sender  # 보내는 사람
msg["To"] = ", ".join(family)  # 받는 사람
msg.set_content("네트워크 프로그래밍 기말고사 답안 제출합니다.")

# 첨부할 파일 열기
with open("profile.jpg", "rb") as f:
    img_data = f.read()

msg.add_attachment(img_data,
                   maintype="zip",
                   subtype=filetype.guess_mime(img_data),
                   filename=filename)

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()

print("Success!")
