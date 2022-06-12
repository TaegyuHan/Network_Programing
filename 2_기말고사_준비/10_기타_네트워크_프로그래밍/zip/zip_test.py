"""
    파일 압축하기
"""
import zipfile


# sample.xlsx와 index.html 파일을 sample.zip으로 압축
zf = zipfile.ZipFile("sample.zip", "w")
zf.write("sample.xlsx")
zf.write("smtp_email1.py")
zf.close()


# sample.zip 파일을 C:\\Users\\student\\Documents\\Network_Programing\\2_기말고사_준비\\10_기타_네트워크_프로그래밍\\smtp
uzf = zipfile.ZipFile("sample.zip", "r")
uzf.extractall(path="/2_기말고사_준비/10_기타_네트워크_프로그래밍/smtp")