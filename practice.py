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

from random import *
# date = int(random() * 29)
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")