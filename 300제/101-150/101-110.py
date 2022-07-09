# 101-110

# 101
# a = True
# print(type(a))

# 102 결과예측
# print(3 == 5)
# 아니요

# 103 결과예측
# print(3 < 5)
# 네

# 104 결과예측
# x = 4
# print(1 < x < 5)
# 네

# 105 결과예측
# print ((3 == 3) and (4 != 3))

# 106 원인 설명
# print(3 => 4)
# 존재하지 않는 기호. 이상, 이하를 표시할 때 부등호는 뒤에 위치

# 107 결과예측
# if 4 < 3:
#     print("Hello World")
# 가정이 잘못되어 어떠한 값도 출력되지 않는다.

# 108 결과예측
# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")
# 가정이 잘못 되었기에 Hi, there.이 출력된다.

# 109 결과예측
# if True :
#     print ("1")
#     print ("2")
# else :
#     print("3")
# print("4")

# 110 결과예측
# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")
# 1. if true가 성립하기에 두번째 else는 작동X
# 2. if false가 성립하지 않기에 작동X, 첫번째 else만 작동 - 3
# 3. 마지막의 print 5가 작동하므로 3과 다음줄의 5가 출력