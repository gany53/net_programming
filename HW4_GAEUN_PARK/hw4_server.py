from socket import *

def calculate(expression):
    # 공백 제거하기
    expression = expression.replace(" ", "")

    # 연산자 우선순위에 따라 수식 계산하기
    while True:
        # 우선순위가 가장 높은 연산자 찾기
        if '*' in expression:
            operator = '*'
        elif '/' in expression:
            operator = '/'
        elif '+' in expression:
            operator = '+'
        elif '-' in expression:
            operator = '-'
        else:
            break

        # 연산자를 기준으로 수식 분리하기
        left, operator, right = expression.partition(operator)

        # 분리된 피연산자를 숫자로 변환하기
        operand1 = float(left)
        operand2 = float(right)

        # 연산자에 따라 계산하기
        if operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            result = operand1 / operand2
        elif operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2

        # 계산 결과를 수식에 반영하기
        expression = expression.replace(left + operator + right, str(result))

    # 최종 결과 반환하기
    return expression


s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)

print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        try:
            rsp = calculate(data.decode())
            rsp = str(rsp)
        except:
            client.send(b'Try again')
        else:
            client.send(rsp.encode())
    client.close()