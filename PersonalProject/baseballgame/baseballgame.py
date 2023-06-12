import random


#랜덤한 숫자 만들기
def create_rannums():
    ran_nums=[]

    num = random.randint(1,9)
    ran_nums.append(num)
#같은 숫자가 안겹치도록
    while len(ran_nums)<3:
        nums = random.randint(1,9)
        if not nums in ran_nums:
            ran_nums.append(nums)
    return ran_nums

#세 개의 숫자 각각 입력받기
def user_nums():
    usernums = []
    user = int(input("---\n 1 번째 숫자 입력하세요 :"))
    usernums.append(user)

    while len(usernums)<3:
        print("---\n",len(usernums)+1,"번째 숫자 입력하세요 :")
        user = int(input())
        if not user in usernums:
            usernums.append(user)
    return usernums

#입력받은 숫자와 랜덤숫자 비교하기
def check_nums(randnums):
    while 1:
        users = user_nums()
        print(users,randnums) #확인용 
        strike = 0
        ball = 0
        for i in range(len(users)):
            if users[i] in randnums:
                if users[i] == randnums[i]:
                    strike +=1
                else :
                    ball +=1
        if strike==0 and ball ==0:
            print("OUT")
        print(strike,"strike"",",ball,"ball")
        #다 맞추면 반복문에서 탈출
        if strike ==3:
            print("성공")
            break


check_nums(create_rannums())