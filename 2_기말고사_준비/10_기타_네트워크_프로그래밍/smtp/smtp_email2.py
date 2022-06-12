"""
    메일 보내기: 여러 사람에게 메일 전송 + 이미지 파일 첨부하기
"""

import smtplib
from email.message import EmailMessage
import filetype  # 파일 유형을 판단해 주는 모듈

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

sender = "gksxorb147@gmail.com"
recipient = "gksxorb147@naver.com"
password = "#"

family = [
    "gksxorb147@nate.com",
    "gksxorb147@naver.com",
]

msg = EmailMessage()
msg["Subject"] = "우리 가족 사진 테스트"
msg["From"] = sender  # 보내는 사람
msg["To"] = ", ".join(family)  # 받는 사람
msg.set_content("우리가족의 행복한 사진 입니다.")
msg.preamble = "You will not see this in a MIME-aware mail reader.\n"

# 첨부할 파일 열기
with open("profile.jpg", "rb") as f:
    img_data = f.read()

# add_attachment 함수를 이요해 파일 첨부, 파일 첨부시 첨부된 파일의 mine-type 지정
msg.add_attachment(img_data,
                   maintype="image",
                   subtype=filetype.guess_mime(img_data),
                   filename="test.jpg")


if __name__ == '__main__':
    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.login(sender, password)
    s.send_message(msg)
    s.quit()

    print("Success!")