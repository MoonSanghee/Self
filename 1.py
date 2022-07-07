#print("Hello World!")

# print('''강한친구 대한육군
# 강한친구 대한육군''')

# print('''\    /\\
#  )  ( ')
# (  /  )
#  \(__)|''')

# print('''|\_/|
# |q p|   /}
# ( 0 )"""\\
# |"^"`    |
# ||_/=\\\__|''')

# A, B = input().split()
# print(int(A)+int(B))

# A, B = input().split()
# print(int(A)-int(B))

# A,B = map(int,input().split())
# print(A+B)
# print(A-B)
# print(A*B)
# print(A/B)
# print(A%B)
# 24-28은 print(A+B, A-B, A*B, A//B, A%B, sep='\n')	으로도 표현 가능
# sep'\n'으로 줄바꿈.

# a = int(input())
# print(a -2541 + 1998)

A,B,C = map(int,input().split())

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)