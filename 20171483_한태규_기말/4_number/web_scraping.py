"""
    웹 스크랩핑
"""
import re
import requests

url = "https://home.sch.ac.kr/iot"
rsp = requests.get(url)
html = rsp.text

class_contact_q_tag = re.findall(r'(<p class="contact">)([\s\S]+?)(</p>)', html)
class_contact_q_tag = "".join(class_contact_q_tag[0])

span_tag_list = re.findall(r'(<span>)([\s\S]+?)(</span>)', class_contact_q_tag)
print(span_tag_list[3][1].split()[-1])
print(span_tag_list[1][1].split()[-1])
print(span_tag_list[2][1].split()[-1])