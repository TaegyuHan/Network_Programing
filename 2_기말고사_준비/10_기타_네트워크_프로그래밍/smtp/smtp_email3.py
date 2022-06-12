"""
    메일 보내기 : HTML 메일 전송하기
"""

import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

sender = "gksxorb147@gmail.com"
recipient = "gksxorb147@naver.com"
password = "#"

msg = EmailMessage()
msg["Subject"] = "HTML 메시지 전송"
msg["From"] = sender
msg["To"] = ("gksxorb147@nate.com", "gksxorb147@naver.com")

# HTML 메시지 작성하기
content_id = 'my_image1'  # 이미지 등의 컨텐츠를 연결하기 위한 id

# multipart/alternative 객체를 만들어 본문에 추가함
msg.add_alternative('''
<html>
    <head></head>
    <body>
        <p>안녕하세요.</p>
        <p>순천향대학교 김대희입니다.</p>
        <p>아래 사이트 확인 부탁 드립니다.</p>
        <p>
            <a href=https://home.sch.ac.kr/iot/>순천향대학교 사물인터넷학과</a>
        </p>
        <p>감사합니다.</p>
        <img src="cid:{cid}" />
    </body>
</html>
'''.format(cid=content_id), subtype='html')

# HTML 메시지의 해당 부분에 이미지 추가하기
with open("iot.png", "rb") as img:
    msg.get_payload()[0].add_related(img.read(),
                                     maintype="image",
                                     subtype="png",
                                     cid=content_id)

# 보내는 메시지 저장하기
with open("outgoing.msg", "wb") as f:
    f.write(bytes(msg))


if __name__ == '__main__':
    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.login(sender, password)
    s.send_message(msg)
    s.quit()
    print("Success!")