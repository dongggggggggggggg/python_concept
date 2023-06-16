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
'''
'''
# 베스킨 라빈스 31 게임

import random
print('베스킨 라빈스 31 게임')
print('1~31의 숫자를 번갈아 불러 31을 부르는 사람이 지는 게임')

#변수 선언
number=0 #1부터 31까지 증가할 수
turn=0 #누구차례냐, 0=사용자, 1=컴퓨터

while True:
    if number>=31: break
    if turn ==0: #내차례면 여기를 실행하겠다
        #부를 숫자 입력
        count=int(input('내가 부를 숫자 갯수(1~3) :'))
        if count>3:
            print('다시입력하세요')
            continue
        while count!=0:
            count=count-1
            number=number+1
            print(f'나: {number}')
        turn=1
        
    elif turn==1:
        com_c=random.randrange(1,4)
        while com_c!=0:
            com_c=com_c-1
            number=number+1
            print(f'컴퓨터: {number}')
        turn=0
if turn ==0:
    print('사용자승리')
else:
    print('컴퓨터승리')
'''
'''
list1 = ["abc","dfg","hij",123,456]
list1[1] = "lee"
print(list1)
'''
'''
arr=[4,8,12,16,20,24,28,32]
print(arr)
'''
'''
arr1=[]
a=1
while True:
    if a==9: break
    a=a+1
    arr1.append(4*a)
print(arr1)
'''
'''
arr=[21,12,4,32,31]
size=len(arr) # 리스트의 크기 변수
print(size)

idx=0 #인덱스 변수
while True:
    idx1=idx+1
    if idx1==size: break
    if arr[idx]>arr[idx1]:
        tmp = arr[idx]
        arr[idx]=arr[idx1]
        arr[idx1]=tmp
    idx=idx+1
    print(arr)
print('-----------------------------')
print(sorted(arr))
print(list(reversed(arr)))
'''
''' 
import datetime
today= datetime.datetime.now()
print(f'오늘은 {today.year}년도입니다')
print(f'오늘은 {today.month}월입니다')
print(f'오늘은 {today.day}일입니다')


if today.weekday() == 6 or today.weekday()==5:
    print('주말')
else:
    print('평일')
print('태어난 날의 요일 맞추기')
y = int(input('년입력: '))
m = int(input('월입력: '))
d = int(input('일입력: '))

date=datetime.datetime(y,m,d)

if date.weekday()==0: print('월')
elif date.weekday()==1: print('화')
elif date.weekday()==2: print('수')
elif date.weekday()==3: print('목')
elif date.weekday()==4: print('금')
elif date.weekday()==5: print('토')
elif date.weekday()==6: print('일')
'''

import random

while True:
 com=random.choice('RSP')
 print(com)

 user=input('R, S, P 중 하나를 고르세요:')

 if user==com :
    print('비김')
 elif (com=='R' and user=='P') or (com=='S' and user=='R') or (com=='P' and user=='S'):
    print('이김')
    break
 elif (user=='R' and com=='P') or (user=='S' and com=='R') or (user=='P' and com=='S'):
    print('짐')
 print(f'컴퓨터 : {com}, 인간:{user}')















    
