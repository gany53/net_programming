lst = ['H', 'e', 'l', 'l', 'o,', ',', ' ', 'I', 'o', 'T']

# 조건 1 리스트 마지막에 '!'를 추가한 후 출력하라.
lst.append('!')
print(lst)

# 조건 2 다섯 번째 요소('o')를 제거한 후 출력하라.
lst[4:5] = []
#del lst[4]
print(lst)

# 조건 3 인덱스 4에 'a'를 넣은 후 출력하라.
lst.insert(4, 'a')
#lst[4] = 'a' #이거는 ','가 바뀌게 됨, insert는 'a' 자체를 끼워넣는 거임
print(lst)

# 조건 4 리스트를 문자열로 변환하여 출력하라.
lstr = ''.join(lst)
print(lstr)

# 조건 5 리스트를 오름차순으로 정렬하여 출력하라.
lst.sort(reverse = True) #sort(reverse = False)가 기본임 True는 내림차순임
print(lst)