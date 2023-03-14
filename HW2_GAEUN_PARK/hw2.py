str = "My name is Gaeun Park"

#문자열 문자수 출력
print(len(str))
#10번 반복
for i in range(10):
    print(str)
#첫번째 문자 출력
print(str[0])
#처음 4문자 출력
print(str[:4])
#마지막 4문자 출력
print(str[-4:])
#거꾸로 출력
print(str[::-1])
#첫번째, 마지막 문자 제거한 문자열 출력
print(str[1:-1])
#대문자 변경 후 출력
print(str.upper())
#소문자 변경 후 출력
print(str.lower())
#'a'를 'e'로 대체하여 출력
print(str.replace('a', 'e'))