'''
list 타입을 선언하고 list에 엘리먼트 추가,삭제
'''
num_list = [10, 20, 40, 50, 60]
print(type(num_list), num_list)
print(num_list[0], num_list[0:3], num_list[3:])

for idx, num in enumerate(num_list):
    print(idx, num)

str_list = ['python', 'java', 'kotlin', 'C++', 'Scalar']
print(type(str_list), str_list)
# index로 list의 엘리먼트 값을 변경
str_list[1] = 'java script'
print(str_list[1], str_list[2:4])
# 엘리먼트 추가
str_list.append('Cobol')
str_list.insert(1, 'type script')
print(str_list)


for idx, val in enumerate(str_list):
    print(idx, val)

mix_list = [100, 3.14, True, '파이썬']
for mix in mix_list:
    print(type(mix), mix)
