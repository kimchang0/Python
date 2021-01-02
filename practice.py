
'''201230'''
# 숫자 자료형
#print(5)
#print(-10)
#print(3.14)
#print(1000)
#print(5+3)
#print(2*8)
#print(3*(3+1))

# 문자 자료형
#print('풍선')
#print("나비")
#print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
#print("ㅋ"*9)

# 불린 자료형
#print(5>10)
#print(5<10)
#print(True)
#print(False)
#print(not True)
#print(not False)
#print(not (5 > 10))

# 변수
# 변수는 코딩을 간결하게 하고, 누구나 자신에게 맞게 내용을 변경할 수 있어서 편리하다.
# animal = "강아지"
# name  = "연탄이"
#age = 4
#hobby = "산책"
#is_adult = age >= 3

#print("우리집 " + animal + "의 이름은 " + name + "예요.")
#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요.")
#print(name + "는 어른일까요? " + str(is_adult))

#animal = "고양이"
#name  = "해피"
#age = 4
#hobby = "낮잠"
#is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name + "예요.")
# 위에 변수를 선언했지만 밑에서 재선언하면 재선언한 내용이 출력된다.
# hobby = "공놀이"
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요.")
# +와 ,로 문장을 더할 수 있고 +는 그냥 더해지지만 ,는 한칸을 자동으로 띄고 더해진다. 또한 + 는 정수나 불린 값을 출력히기 위해 str()로 감싸줘야 하지만 ,는 그냥 출력 가능하다.
# print(name, "는 어른일까요? ", is_adult)

#퀴즈
# station = "사당"

# print(station + "행 열차가 들어오고 있습니다.")

# station = "신도림"

# print(station + "행 열차가 들어오고 있습니다.")

# station = "인천공항"

# print(station, "행 열차가 들어오고 있습니다.")

'''201231'''

#연산자
# print(1+1) # 2
# print(3-2) # 1
# print(5*2) # 10
# print(6/3) # 2

# print(2**3) # 2^3 = 8
# print(5%3) # 나머지 2
# print(10%3) # 나머지 1
# print(5//3) # 몫
# print(10//3)

# print(10 > 3) # true
# print(4 >= 7) # false
# print(10 < 3) # false
# print(5 <= 5) # true

# print(3 == 3) # 같다 true
# print(4 == 2) # false
# print(3 + 4 == 7) # true

# print(1 != 3) # 같지 않다 true
# print(not(1 != 3)) # 1은 3과 같지 않기 때문에 트루지만 not을 붙여서 false가 나옴

# print((3 > 0) and (3 < 5)) #true 동시조건은 and를 사용하거나 &를 하나 붙여서 표현함. 동시에 만족하면 ture가 나옴
# print((3 > 0 ) & (3 < 5)) # ture 하나라도 만족하지 않으면 false

# print((3 > 0) or (3 > 5)) # ture or조건은 or을 사용하거나 |를 사용해 표현함. 하나라도 만족하면 true가 나옴
# print((3 > 0) | (3 > 5)) # true 둘 다 만족하지 않으면 false

# print(5 > 4 > 3) # true 조건을 모두 만족하기 때문에 true
# print(5 > 4 > 7) # false 조건 하나가 맞지 않기때문에 false

# 수식
# print(2 + 3 * 4)
# print((2 + 3) * 4)

# number = 2 + 3 * 4
# print(number)

# number = number + 2
# print(number)

# number += 2
# print(number)

# number *= 2
# print(number)

# number /= 2
# print(number)

# number -= 2
# print(number)

# number %= 2
# print(number)

# #숫자처리 함수
# print(abs(-5)) # 절댓값 absolute
# print(pow(4, 2)) # 제곱 power 4^2
# print(max(5, 12)) #최대값 maximum 둘 중 큰 값을 찾아 반환
# print(min(5, 12)) #최소값 minimum 둘 중 작은 값을 찾아 반환
# print(round(3.14)) # 반올림 round
# print(round(4.99))

# from math import *
# print(floor(4.99)) # 내림 floor
# print(ceil(3.14)) # 올림 ceiling
# print(sqrt(16)) # 제곱근 square root pram의 제곱근을 구함

# 랜덤 함수
# from random import *

# print(random()) # 0.0 이상 1.0 이하의 임의의 값 생성
# print(random() * 10) # 0.0 이상 10.0 이하의 임의의 값 생성
# print(int(random() * 10)) # 0 이상 10 이하의 임의의 정수값 생성
# print(int(random() * 10)) # 0 이상 10 이하의 임의의 정수값 생성
# print(int(random() * 10)) # 0 이상 10 이하의 임의의 정수값 생성
# print(int(random() * 45) + 1)# 1 이상 45 이하의 임의의 정수값 생성
# print(int(random() * 45) + 1)# 1 이상 10 이하의 임의의 정수값 생성
# print(int(random() * 45) + 1)# 1 이상 10 이하의 임의의 정수값 생성
# print(int(random() * 45) + 1)# 1 이상 10 이하의 임의의 정수값 생성
# print(int(random() * 45) + 1)# 1 이상 10 이하의 임의의 정수값 생성
# print(int(random() * 45) + 1)# 1 이상 10 이하의 임의의 정수값 생성

# print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성

# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성 자동으로 1, 45 포함함.
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성 자동으로 1, 45 포함함.
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성 자동으로 1, 45 포함함.
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성 자동으로 1, 45 포함함.
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성 자동으로 1, 45 포함함.
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성 자동으로 1, 45 포함함.
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성 자동으로 1, 45 포함함.

# 퀴즈

''' Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데, 3번은 온라인으로 하고, 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3 : 매월 1 ~ 3일은 스터디 준비를 해야 하므로 제외함

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.'''
# from random import *
# date = randint(4, 28)

# print("오프라인 스터디 모임 날짜는 매월", date, "일로 선정되었습니다.")

'''210101'''

# # 문자열
# sentence = "나는 소년입니다"
# print(sentence)

# sentence2 = "파이썬은 쉬워요"
# print(sentence2)

# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# 슬라이싱
# jumin = "990120-1234567"


# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0번째 자리부터 2번째 자리 사이의 값을 가져옴
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6]) # 콜론 앞에 숫자가 없으면 처음부터 6번째 전까지 가져옴
# print("뒤 7자리 : " + jumin[7:]) # 콜론 뒤에 숫자가 없으면 지정한 숫자부터 끝가지 가져옴
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 뒤에 7번째부터 시작해서 뒤로 끝까지

# 문자열 처리함수
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("Java")) # find는 내가 찾는 값이 없으면 -1을 반환하고
# print(python.index("Java")) # index는 내가 찾는 값이 없으면 오류가 난다.
# print("hi")

# print(python.count("n"))

# 문자열 포맷
print("a" + "b")
print("a", "b")

print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
# d는 정수형, s는 문자열, c는 문자 하나이지만, s형으로 쓰면 무엇이든 상관없이 쓸 수 있다.

print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))
'''210102'''






































