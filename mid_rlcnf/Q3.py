str = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'

str = str.split('?')
#str = {'where':'nexearch', 'ie':'utf8', 'query':'iot'}
str2 = str[1]
print(str2)

str2 = str2.split('&')
print(str2)

str3 = []
for i in range (3):
    str3.append(str2[i].split('='))

print(str3)

answer = dict()
for i in range(3):
    answer[str3[i][0]] = str3[i][1]
print(answer)