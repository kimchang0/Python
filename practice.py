
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

# index = python.index("n") # 몇번째에 n이 포함되는지 위치를 물어봄
# print(index)
# index = python.index("n", index + 1) # 다음 n은 어디인지 위치를 물어봄
# print(index)

# print(python.find("Java")) # find는 내가 찾는 값이 있으면 위치를, 없으면 -1을 반환하고
# print(python.index("Java")) # index는 내가 찾는 값이 있으면 위치를, 없으면 오류가 난다.
# print("hi")

# print(python.count("n")) # n의 개수를 세는 함수

# 문자열 포맷
# print("a" + "b")
# print("a", "b")

# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple은 %c로 시작해요." % "A")
# # d는 정수형, s는 문자열, c는 문자 하나이지만, s형으로 쓰면 무엇이든 상관없이 쓸 수 있다.

# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# print("나는 {}살입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간")) # 중괄호에 번호를 적으면 인자값의 번호대로 입력됨
# print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간")) # 중괄호에 번호를 적으면 인자값의 번호대로 입력됨
# '''210102'''
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간")) # print 안에 변수를 선언하는 것 처럼 사용함
# print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20)) # 변수의 순서가 바뀌어도 출력은 동일하지만 출력하는 곳의 순서가 바뀌면 출력은 달라짐

# age = 20
# color = "빨간"

# print(f"나는 {age}살이며, {color}색을 좋아해요.") # python 버전 3.6 이상부터 사용 가능한 기능으로 실제 변수를 가져와서 값을 출력함

# 탈출문자
# print("백문이 불여일견 \n백견이 불여일타") # 줄바꿈 옵션

# print("저는 \"김창영\" 입니다.") # 큰 따옴표 표현옵션 1
# print('저는 "김창영" 입니다.') # 큰 따옴표 표현옵션 2

# print("c:\\work\\working\\start") # \표현옵션

# print("Red Apple \rPine") # 커서를 앞으로 옮겨 덮어쓰기 함

# print("Redd\b Apple") # 한 글자를 지우는 옵션

# print("Red\tApple") # 한 번 tab누르는 옵션

# 퀴즈
# ''' Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# 예) http://naver.com

# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 e 갯수 + !로 구성

# 예) 생성된 비밀번호 : nav51!'''

# url = "http://naver.com"
# memory = url.replace("http://", "")
# memory = memory[:memory.find(".")]
# password = memory[:3] + str(len(memory)) + str(memory.count("e")) + "!"

# print(f"{url}의 비밀번호는 {password}입니다.")

# 리스트
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# print(subway.index("조세호"))

# subway.append("하하")
# print(subway)

# subway.insert(1,"정형돈")
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)

# num_list = [5, 2, 4, 3, 1]
# mix_list = ["조세호", 20, True]

# num_list.extend(mix_list)
# print(num_list)

# 사전
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(5, "사용가능"))

# print(3 in cabinet)
# print(5 in cabinet)

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# cabinet["C-20"] = "조세호"
# print(cabinet.get("C-20"))

# del cabinet["A-3"]
# print(cabinet)
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())

# cabinet.clear()
# print(cabinet)

# 튜플
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# name, age, hobby = "김종국", 20, "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# 세트 (집합) set 중복없고 순서도 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# print(java & python)
# print(java.intersection(python))

# print(java | python)
# print(java.union(python))

# print(java - python)
# print(java.difference(python))

# python.add("김태호")
# print(python)

# java.remove("김태호")
# print(java)

# 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# 퀴즈
''' Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표--
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --'''

# from random import *

# id = range(1, 21) # range 함수를 이용해 1 ~ 20 까지의 숫자들을 생성함
# id = list(id) # id는 range 함수이므로 list로 변환함
# shuffle(id) # 현재의 id는 1부터 20까지 나열되어있는 형태이므로 shuffle 함수를 이용해 섞어줌
# pick = sample(id, 4) # pick 변수에 id리스트에서 임의로 뽑은 4개의 숫자들을 저장함

# print("-- 당첨자 발표--")
# print("치킨 당첨자 : {0}".format(pick[0])) # pick의 첫 번째를 치킨 당첨자로 정함
# print("커피 당첨자 : {0}".format(pick[1:])) # pick의 2, 3, 4번째를 커피 당첨자로 정함
# print("-- 축하합니다 --")
'''20210119'''

# if문 (조건문)
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요없어요.")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요.")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요.")
# else:
#     print("너무 추워요. 나가지 마세요.")

# for문 (반복문 1)
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# print("대기번호 : 5")

# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1, 6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 고객님 커피가 준비되었습니다.".format(customer))

# while문(반복문 2)
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 손님 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 손님 커피가 준비 되었습니다. {1}번 불렀어요.".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0} 손님 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")
#     if person == customer:
#         print("{0} 고객님 주문하신 커피 나왔습니다.".format(person))
#     elif person != customer:
#         print("{0} 고객님의 커피는 준비 중이니 잠시만 기다려주세요.".format(person))


# continue와 break
# absent = [2, 5]
# no_book = [7] #책이 없음
# for  student in range(1, 11): #1번부터 10번
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}번은 교무실로 따라와".format(student))
#         break
#     print("{0}번 책을 읽어봐".format(student))

# 한 줄 for문(반복문 3)
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "Groot"]
# print(students)
# students = [len(i) for i in students]
# print(students)

# students = ["Iron man", "Thor", "Groot"]
# students = [i.upper() for i in students]
# print(students)
# students = [i.lower() for i in students]
# print(students)

# 퀴즈
''' 당신은 코코아 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 분'''

# from random import *
# # 내 풀이
# i = 1
# count = 0
# while i <= 50:
#     time = randrange(5, 51)
#     if 5 <= time <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         count += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#     i += 1

# print("총 탑승 승객 : {0} 분".format(count))

# # 강의 풀이
# cnt = 0
# for i in range(1, 51):
#     time = randrange(5, 51)
#     if 5 <= time <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0} 분".format(count))

# # 함수(function)
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# 전달값과 반환값(parameter, return)
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)
# print(balance)
# balance = withdraw(balance, 500)
# print(balance)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

# 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# 키워드 값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=20, name="김태호")

# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# 지역변수, 전역변수 (전역변수는 코드를 어렵게 만들기 때문에 파라미터로 값을 받고 리턴하는 것이 좋음)
# gun = 10

# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# 퀴즈
''' 표준 체중을 구하는 프로그램을 작성하시오.
*표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) X 키(m) X 22
여자 : 키(m) X 키(m) X 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
            * 함수명 : std_weight
            * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.'''

#내 풀이
# def std_weight(height, gender):
#     weight = 0
#     if gender == "남자":
#         weight = round((height * height * 22) / 10000, 2)
#     elif gender == "여자":
#         weight = round((height * height * 21) / 10000, 2)
#     else:
#         print("성별이 이상합니다. 성별을 확인해주세요.")
#     print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight)) 

# std_weight(175, "남자")

#강의 풀이
# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight)) 
'''210120'''

#표준입출력
# print("Python", "Java", sep=",")
# print("Python", "Java", "Javascript", sep=" vs ")
# print("Python", "Java", sep=",", end="?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "java", file=sys.stdout)
# print("Python", "java", file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(3), str(score).rjust(4), sep=":")

# for num in range(1, 21):
#     # print("대기번호 : " + str(num))
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")

# 다양한 출력포멧
# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))

# # 양수일 때는 +로 표시, 음수일 때는 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# # 왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0:_<+10}".format(500))
# print("{0:_<10}".format(500))

# # 3자리 마다 ,찍기
# print("{0:,}".format(1000000000000))

# # 3자리 마다 ,찍기 +,- 부호도 붙이기
# print("{0:+,}".format(1000000000000))
# print("{0:+,}".format(-1000000000000))

# # 3자리 마다 ,찍기 +,- 부호도 붙이고 자리도 확보하고 빈 자리는 ^채우기
# print("{0:^<+30,}".format(1000000000000))

# # 소수점 출력
# print("{0:f}".format(5/3))

# # 소수점 특정 자리까지만 출력(소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

# 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")

# score_file.close()

# pickle
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #프로필에 있는 정보를 파일에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with
# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

''' Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 - 
부서 :
이름 :
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 "1주차.txt", "2주차.txt", ... 와 같이 만듭니다.'''
# 내 풀이
# i = 1
# while i <= 50:
#     with open(str(i) +"주차.txt", "w", encoding="utf8") as study_file:
#         study_file.write("-" + str(i) + "주차 주간보고 -")
#         study_file.write("\n부서 : ")
#         study_file.write("\n이름 : ")
#         study_file.write("\n업무 요약 : ")
#     i += 1

# 강의 풀이
# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("-" + str(i) + "주차 주간보고 -")
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")
'''210120'''

# 클래스
# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력{1}\n".format(hp, damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력{1}\n".format(tank_hp, tank_damage))

# tank_name2 = "탱크"
# tank_hp2 = 150
# tank_damage2 = 35
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력{1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank_name2, "1시", tank_damage2)

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# __init__(파이썬에서 쓰이는 생성자)
# 객체를 생성했을 때 함수에서 쓰이는 파라미터를 전부 채워야 함. 일부를 빼면 실행이 되지 않음

# 멤버변수
# 클래스 내에서 정의된 변수를 멤버변수라고 함.
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True # 밖에서 .을 사용해서 변수를 추가할 수 있음

# if wraith2.clocking == True: # 존재하지 않는 변수를 물어보면 오류가 남 wraith1로 바꾸면 wraith1에는 clocking이 없기 때문에 오류가 남
#     print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))

# 메소드 & 상속 & 다중상속 & 메소드 오버라이딩
# 일반유닛
# class Unit:
#     def __init__(self, name, hp, speed): # __init__함수를 통해 파라미터를 받아옴
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성 되었습니다.".format(name))
#         # self.damage = damage
#         # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 공격유닛
# class AttackUnit(Unit): # 상속받으려는 클래스를 ()안에 쓰면 상속됨
#     def __init__(self, name, hp, speed, damage):
#         # self.name = name
#         # self.hp = hp
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(self.name, location, self.damage))

# #마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# #탱크
# class Tank(AttackUnit):
#     seize_developed = False

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return

#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         else:
#             print("{0} : 시즈모드를 헤제합니다.".format(self.name))    
#             self.damage /= 2
#             self.seize_mode = False
        

# # firebat1 = AttackUnit("파이어뱃", 50, 16)
# # firebat1.attack("5시")

# # firebat1.damaged(25)
# # firebat1.damaged(25)

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)



# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드 헤제합니다.".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clocked = True

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")


# # 실제 게임 진행
# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wraith()

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 ( 마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)

# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# from random import *

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 21)) #공격은 5 ~ 20 까지의 랜덤으로

# game_over()

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# vulture = AttackUnit("벌쳐", 80, 10, 20)

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
# vulture.move("11시")
# battlecruiser.move("9시")
'''210121 ~ 210210'''

''' quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass

    def show_detail(self):
        pass
'''

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        print("[알림] 부동산 정보가 추가되었습니다. {0} {1} {2} {3} {4}".format(location, house_type, deal_type, price, completion_year))

    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

h1 = House("강남", "아파트", "매매", "10억", "2010년")
h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
h3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses = []
houses.append(h1)
houses.append(h2)
houses.append(h3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))

for house in houses:
    house.show_detail()















