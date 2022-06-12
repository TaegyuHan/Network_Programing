"""
    SSH 사용하기

    SSH: 원격 시스템에서 연속적으로 명령어 실행하기
"""

import getpass
import paramiko
import time

BUF_SIZE = 65535

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input("Username: ")
pwd = getpass.getpass("Password:")

cli.connect("114.71.220.5",
            username=user,
            password=pwd)

channel = cli.invoke_shell()  # 새로운 셸 세션(channel) 생성

# 채널을 통해 명령어 전송
channel.send("cat /proc/cpuinfo\n")
time.sleep(0.5)

channel.send("cat /proc/meminfo\n")
time.sleep(0.5)

channel.send("mkdir test\n")
time.sleep(0.5)

channel.send("cd test\n")
time.sleep(0.5)

channel.send("echo iot > iot.txt\n")
time.sleep(0.5)

channel.send("cat iot.txt\n")
time.sleep(0.5)

output = channel.recv(BUF_SIZE).decode()  # 명렁어 실행결과를 수신
print(output)

cli.close()
