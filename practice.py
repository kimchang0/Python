
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

from random import *

id = range(1, 21) # range 함수를 이용해 1 ~ 20 까지의 숫자들을 생성함
id = list(id) # id는 range 함수이므로 list로 변환함
shuffle(id) # 현재의 id는 1부터 20까지 나열되어있는 형태이므로 shuffle 함수를 통해 섞어줌
pick = sample(id, 4) # pick 변수에 id리스트에서 임의로 뽑은 4개의 숫자들을 저장함

print("-- 당첨자 발표--")
print("치킨 당첨자 : {0}".format(pick[0])) # pick의 첫 번째를 치킨 당첨자로 정함
print("커피 당첨자 : {0}".format(pick[1:])) # pick의 2, 3, 4번째를 커피 당첨자로 정함
print("-- 축하합니다 --")






