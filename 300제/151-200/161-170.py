# 161-170

# 161
# Q. for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.
# for i in range(100):
#     print(i)

# 162
# Q. 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
# 2002
# 2006
# 2010
# ...
# 2042
# 2046
# 2050
# *range의 세번 째 파라미터는 증감폭을 결정

# for i in range(2002, 2051, 4):
#     print(i)

# 163
# Q. 1부터 30까지의 숫자 중 3의 배수를 출력하라.
# 3 
# 6 
# 9 
# 12 
# 15 
# 18 
# 21 
# 24 
# 27 
# 30

# A1
# for i in range(1,30):
#     if i % 3 == 0:
#         print(i)
# A2
# for num in range(3, 31, 3):
#     print (num)

# 164
# Q. 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.

# for i in range(100):
#     print(99 - i)

# 165
# Q. for문을 사용해서 아래와 같이 출력하라.
# 0.0
# 0.1
# 0.2
# 0.3
# 0.4
# 0.5
# ...
# 0.9

# for i in range(10):
#     print('0.',i)

# 166
# Q.구구단 3단을 출력하라.

# for i in range(1, 10):
#     print('3x', i, ' =', i*3)

# 167
# Q. 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.

# A1.
# for i in range(1, 10, 2):
#     print('3x', i, ' =', i*3)
# A2.
# for i in range(1, 10):
#     if i % 2 == 1 :
#         print('3x', i, ' =', i*3)

# 168
# Q. 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.


# result = 0
# for i in range(1, 11):
#     result += i
# print(result)

# result +=i result는 i값을 누적한다.
# result = result + i 와 같다.

# 169
# Q. 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
# a = 0
# for i in range(1, 11, 2):
#     a +=i
# print(a)

# 170
# 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.

# a = 1
# for i in range(1,11):
#     a *=i
# print(a)