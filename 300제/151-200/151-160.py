# 151-160

# 151
# Q.리스트에는 네 개의 정수가 저장돼 있다.
# 리스트 = [3, -20, -3, 44]
# for문을 사용해서 리스트의 음수를 출력하라.
# -20
# -3

# 리스트 = [3, -20, -3, 44]
# for i in 리스트:
#     if i < 0:
#         print(i)

# 152
# Q. for문을 사용해서 3의 배수만을 출력하라.
# 리스트 = [3, 100, 23, 44]

# 리스트 = [3, 100, 23, 44]
# for i in 리스트:
#     if i % 3 == 0:
#         print(i)

# 153
# Q. 리스트에서 20 보다 작은 3의 배수를 출력하라
# 리스트 = [13, 21, 12, 14, 30, 18]
# 12
# 18

# 리스트 = [13, 21, 12, 14, 30, 18]
# for i in 리스트:
#     if (i < 20) and (i % 3 ==0):
#             print(i)

# 154
# Q. 리스트에서 세 글자 이상의 문자를 화면에 출력하라
# 리스트 = ["I", "study", "python", "language", "!"]
# study
# python
# language

# 리스트 = ["I", "study", "python", "language", "!"]
# for i in 리스트:
#     if len(i) > 3:
#         print(i)

# 155
# Q. 리스트에서 대문자만 화면에 출력하라.
# 리스트 = ["A", "b", "c", "D"]
# A
# D

# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#     if i.isupper():
#         print(i)

# 156
# Q. 리스트에서 소문자만 화면에 출력하라.
# 리스트 = ["A", "b", "c", "D"]
# b
# c

# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#   if not i.isupper():
#     print(i)

# 157
# Q. 이름의 첫 글자를 대문자로 변경해서 출력하라.
# 리스트 = ['dog', 'cat', 'parrot']
# Dog
# Cat
# Parrot

# 리스트 = ['dog', 'cat', 'parrot']
# for 변수 in 리스트:
#   첫글자 = 변수[0]              
#   대문자 = 첫글자.upper()     
#   print(대문자 + 변수[1:])

# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i[0].upper() + i[1:])

# 158
# Q. 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro

# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# for i in 리스트:
#     print((i.split('.'))[0])

# 159
# Q. 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# define.h

# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in 리스트:
#     u = i.split('.')
#     if u[1] =='h':
#         print(i)

# 160
# Q. 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# intra.c
# define.h

# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in 리스트:
#     u = i.split('.')
#     if (u[1] =='h') or (u[1] =='c'):
#         print(i)