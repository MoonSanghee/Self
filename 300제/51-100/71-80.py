# 071
# my_variable = ()
# 괄호는 튜플을 정의하는 기호이다.

# 072
# movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
# 리스트 - 순서가 있고 수정 가능
# 튜플 - 순서가 있지만 수정이 불가능

# 073
# a = (1, )
# print(a, type(a))
# 값이 하나만 있을 경우 쉼표가 있어야 한다.

# 074 - 오류 발생 원인 설명
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
# 튜플은 값을 변경할 수 없음.

# 075
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4
# 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작합니다.
# *그렇기 때문에 숫자 자릿수를 표시하기위해 ','를 사용하면 안 됨.

# 076
# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
# t = ('a', 'b', 'c')
# 튜플은 값을 수정할 수 없으므로 새로운 튜플t = ('A', 'b', 'c')을 만들고 t라는 변수를 업데이트 해야함.
# 이 때 기존의 튜플('a', 'b', 'c')은 자동으로 삭제됨.

# 077
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# print(list(interest))

# 078
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# print(tuple(interest))

# 079 - 튜플 언팩킹(결과 예상)
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)

# 080 range
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
# data = tuple(range(2, 100, 2))
# print( data )