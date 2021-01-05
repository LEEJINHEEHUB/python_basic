'''
문자열 관련 내용들
'''
# escape 문자
greet = 'Hello' * 4 + '\n'
end = '\tGood \'Bye\' !!'
end2 = "\t Good 'Morning' ??"
print(greet + end + end2)

# bool 타입과 str 타입
is_flag = False
my_str = 'False'
print(type(is_flag), type(my_str))
if not is_flag:
    print(my_str)

# 문자열 인덱스(오프셋)
#           012345678910
greeting = 'hello world'
print('문자열 길이 ', len(greeting))
# c언어 스타일
print('파이썬 %s' % greeting)
print('문자열 길이 %i' % len(greeting))

print('문자열 길이 {}, 0번째 인덱스 값은 {}'.format(len(greeting), greeting[0]))
# 3.6 버전이후
print(f'문자열 길이 {len(greeting)}, 1번째 인덱스 값은 {greeting[1]}')

# IndexError: string index out of range
# print(greeting[12])

# 문자열 인덱스 슬라이싱 (end값은 exclusive )
print(f'greeting[0:5] = {greeting[0:5]}')
print(f'greeting[6:11] = {greeting[6:11]}')
print(f'greeting[6:] = {greeting[6:]}')
print(f'greeting[:5] = {greeting[:5]}')
print(greeting, greeting[:])