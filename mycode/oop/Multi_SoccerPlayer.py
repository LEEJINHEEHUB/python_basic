# 선수명, 선수 포지션, 선수 등번호 (클래스, 객체 예시문제 너무너무 중요!!)
names = ['홍길동', '박지성', '손흥민', '둘리', '파이썬']
positions = ['DF', 'MF', 'GK', 'DF', 'WF']
back_numbers = [5, 10, 20, 30, 15]

# Class 없이 여러명의 선수정보를 2차원 배열에 저장하기
for na, po, ba in zip(names, positions, back_numbers):
    print(na, po, ba)

playser = [[names, positions, back_numbers] for name, position, back_number in zip(names, positions, back_numbers)]
# print(playser)
playser1 = playser[0]
# back_number 를 변경
playser1[2] = 20
# print(playser1)

# SoccerPlayer 클래스를 import
from mycode.oop.python_class import SoccerPlayer

playser = SoccerPlayer('dooly', 'MF', 10)
print(playser)
# 객체를 여러가 가지고 있는 리스트를 만듦
playser_obj = [ SoccerPlayer(name, position, back_number) for name, position, back_number in zip(names, positions, back_numbers)]
print(playser_obj)
playser1 = playser_obj[0]
# back_number 변경
playser1.change_back_number(30)
print(playser1)




