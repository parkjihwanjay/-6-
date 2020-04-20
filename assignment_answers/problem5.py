print('문제 1. 전화번호 받기')

print('조건 1. 저장할 때는 공백 문자 없이')
print('조건 2. -, ., , 등이 들어올 때 전부 제외 하고 숫자만 저장!')

input_number = input()
input_number = input_number.replace('-', '')
input_number = input_number.replace('.', '')
input_number = input_number.replace(',', '')
print(input_number)
