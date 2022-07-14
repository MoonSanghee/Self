# 251 클래스, 객체, 인스턴스

# Q. 클래스, 객체, 인스턴스에 대해 설명해봅시다.

# A.


# 252 클래스 정의

# Q. 비어있는 사람 (Human) 클래스를 "정의" 해보세요.

# A.
# class Human:
#     pass

# 253 인스턴스 생성

# Q. 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.

# A.
# class Human:
#     pass

# areum = Human()
# 참고.     객체를 생성하고 바인딩을 안 하면 소멸됨.
#           격체 생성 시 변수를 통해 바인딩 해줄것.

# 254 클래스 생성자-1

# Q. 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.

# A.
# class Human:
#     def __init__(self):
#         print('응애응애')
# areum = Human()

# 255 클래스 생성자-2

# Q. 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.

# A.
# class Human :
#     def __init__(self, 이름, 나이, 성별):
#         self.name = 이름
#         self.age = 나이
#         self.sex = 성별

# areum = Human('아름', 25, '여자')


# 256 인스턴스 속성에 접근

# Q. 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.

# A.
# class Human :
#     def __init__(self, 이름, 나이, 성별):
#         self.name = 이름
#         self.age = 나이
#         self.sex = 성별

# areum = Human('아름', 25, '여자')

# print(areum.name)
# print(areum.age)
# print(areum.sex)


# 257 클래스 메소드 - 1

# Q. 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.

# A.
# class Human :
#     def __init__(self, 이름, 나이, 성별):
#         self.name = 이름
#         self.age = 나이
#         self.sex = 성별

#     def who(self):
#         print('이름: {} 나이: {} 성별: {}'.format(self.name, self.age, self.sex))

# 258 클래스 메소드 - 2

# Q. 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.

# A.
# class Human :
#     def __init__(self, 이름, 나이, 성별):
#         self.name = 이름
#         self.age = 나이
#         self.sex = 성별

#     def who(self):
#         print('이름: {} 나이: {} 성별: {}'.format(self.name, self.age, self.sex))

#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human('불명', '미상', '모름')
# areum.who()
# areum.setInfo('아름', 25, '여자')
# areum.who()

# 259 클래스 소멸자

# Q. 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
# >>> areum = Human("아름", 25, "여자")
# >>> del areum
# 나의 죽음을 알리지 말라

# A.
# class Human :
#     def __init__(self, 이름, 나이, 성별):
#         self.name = 이름
#         self.age = 나이
#         self.sex = 성별

#     def __del__(self):
#         print('나의 죽음을 알리지마라')

#     def who(self):
#         print('이름: {} 나이: {} 성별: {}'.format(self.name, self.age, self.sex))

#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human('불명', '미상', '모름')
# del(areum)

# 260 에러의 원인

# Q. 아래와 같은 에러가 발생한 원인에 대해 설명하세요.

# class OMG : 
#     def print() :
#         print("Oh my god")

# >>> >>> myStock = OMG()
# >>> myStock.print()
# TypeError Traceback (most recent call last)
# <ipython-input-233-c85c04535b22> in <module>()
# ----> myStock.print()

# TypeError: print() takes 0 positional arguments but 1 was given


# A.
