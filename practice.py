## 숫자형 자료형
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(2*9)
# print(3*(3+1))


## 문자열 자료형
# print('풍선')
# print('나비')
# print("zzz")
# print("z"*10)


## 불리언 연산자
# print(5>10)
# print(5 < 10)
# print(True)
# print(not False)
# print(not True)
# print(not(5 > 10))


## 변수
# 애완동물을 소개해주세요~
# animal = "고양이"
# name = "해피"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name + "에요")
# print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))


## 연산자

# print(1+1)
# print(3-2)
# print(5*2)
# print("--------")

# print(2**3) # 2^3 = 8
# print(5%3) # 나머지
# print(5//3) # 몫
# print("--------")

# print(10 > 3)
# print(10 >= 3)
# print("--------")

# print(3 == 3) # 같다
# print(1 != 3) # 같지 않다
# print(not(1 != 3))
# print("--------")

# print((3>0) and (3<5)) # and
# print((3>0) & (3<5)) # and
# print("--------")

# print((3>0) or (3>5)) # or
# print((3>0) | (3>5)) # or
# print("--------")


## 수식
# print(2 + 3 *4)
# print((2 + 3)*4)
# number = 2 + 3 * 4
# print(number)
# number += 2
# print(number)
# number *= 2
# print(number)
# number /= 2
# print(number)
# number -= 2
# print(number)


## 숫자처리함수
# print(abs(-5)) #절대값
# print(pow(4,2)) # 4^2
# print(max(5,16)) 
# print(min(5,16))
# print(round(3.14)) # 반올림
# print(round(5.99))

# from math import *
# print(floor(4.99)) # 내림
# print(ceil(3.15)) # 올림
# print(sqrt(16)) # 제곱근


## 랜덤함수
# from random import *
# print(random())
# print(random() * 10)
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10))

# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)

# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)

# print(randint(1,45)) # 1~45 이하의 임의 값 생성


##Quiz
#당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
#월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
#아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

#조건1 : 랜덤으로 날짜를 뽑아야 함
#조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
#조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

#(출력문 예제)
#오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

# from random import *
# # date = int(random() * 29)
# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")


## 문자열
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)


## 슬라이싱
# jumin = "921102-1234567"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) #0자리부터 2직전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6]) #처음부터 6직전까지
# print("뒤 7자리 : " + jumin[7:])
# print("뒤 7자리(뒤에서부터) : " + jumin[-7:])


## 문자열처리함수
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1) #n의 두번째 위치
# print(index)

# print(python.find("Java"))
# # print(python.index("Java")) #index에서 없는 문자를 찾을 경우 에러남
# print("hi")

# print(python.count("n"))


## 문자열포맷
# print("a" + "b")
# print("a", "b")

# #방법1
# print("나는 %d살입니다." % 20)
# print("니는 %s을 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요." % "A")
# # %s
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# #방법2
# print("나는 {}살입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))

# #방법3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20))

# #방법4 (v3.6이상 ~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")


## 탈출문자
# print("백문의 불여일견\n백견이 불여일타")

# \" \" : 문장 내에서 따옴표
#저는 "나도코딩" 입니다.
# print("저는 '나도코딩' 입니다.")
# print('저는 "나도코딩" 입니다.')
# print("저는 \"나도코딩\" 입니다.")

# \\ : 문장 내에서 \
# print("C:\\Users\\user\\Desktop\\PythonWorkspace\\cyesc_Hub>")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")


## Quiz
#Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
#예) http://naver.com
#규칙1 : http:// 부분은 제외 => naver.com
#규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
#규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                (nav)               (5)             (1)                 (!)
#예) 생성된 비밀번호 : nav51!

# url = "http://naver.com"
# url = url[7:12]
# print("생성된 비밀번호 : " + str(url[0:3]) + str(len(url)) + str(url.count("e")) + "!")

# url = "http://naver.com"
# print("생성된 비밀번호 : " + str(url[7:10]) + str(len(url[7:12])) + str(url[7:12].count("e")) + "!")

url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("생성된 비밀번호 : " + password)