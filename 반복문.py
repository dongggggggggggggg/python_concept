#1
'''
print(3==2)
print(4 !=4)
print(5>=10)
'''
'''
#2
a=int(input("C언어 파이썬 : "))
b=int(input("파이썬 성적 : "))
c=int(input("자바 성적 : "))
avg=a+b+c/3
if avg>=80:
    print("합격")
    
else:
    print("불합격")
'''
'''
#3
a=int(input("양의 정수를 입력하세요"))
if a%3==0 and a%2==0:
    print("3과 2의 배수")
elif a%3==0:
    print("3의 배수")
elif a%2==0:
    print("2의 배수")
else:
    print("2와 3의 배수가 아님")
'''
'''
# while로 무한루프 만드는법
while 1:
    num=input('알파벳으로 입력하시오(z를 누르면 종료!)')
    if(num=='z'):
        break
    print(num)
'''
# 4-1
import random
ans=random.randrange(0,100)
c=0
while True:
    c=c+1
    print("----------------------")
    me = int(input("숫자 입력 :"))
    if ans<me:
        print("down")
        print(f"기회 : {c}")
    elif ans>me:
        print("up")
        print(f"기회 : {c}")
    else:
        print("정답")
        print(f"기회 : {c}")
        break
