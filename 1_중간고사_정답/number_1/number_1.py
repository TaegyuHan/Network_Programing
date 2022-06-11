# 문자열을 3번 반복한 문자열을 출력하라
string = "Hello, IoT"
print(string * 3)

# 문자열의 처음 4문자를 출력하라
print(string[:4])

# 문자열의 마지막 4문자를 출력하라
print(string[len(string) - 4: len(string)])

# 문자를 모두 소문자로 변경하여 출력하라
print(string.lower())

# 문자열에서 IoT 시작 인덱스를 출력하라.
print(string.index("IoT"))