"""
    SSH 사용하기
    
    SSH: 원격 시스템의 CPU 및 메모리 정보 조회하기
"""
import getpass
import paramiko

PORT = 22

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input("Username: ")
pwd = getpass.getpass("Password: ")

cli.connect("114.71.220.5",
            port=22,
            useraname=user,
            password=pwd)


stdin, stout, stderr = cli.exec_command("cat /proc/cpuinfo")
lines = stout.readlines()
print("".join(lines))


stdin, stout, stderr = cli.exec_command("cat /proc/meminfo")
lines = stout.readlines()
print("".join(lines))


cli.close()