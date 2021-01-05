kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]

midterm_score = [kor_score,math_score,eng_score]
print(midterm_score)
print(midterm_score[0])
print(midterm_score[0][3])

student_score = [0, 0, 0, 0, 0]


for subject in midterm_score:
    # 학생별 과목합계 점수를 계산
    print(subject)
    for student in subject:
        print(student)
else:
    # 평균을 계산 ( unpacking 사용 )
    pass
