import random

def create_rannums():
    """
    make random numbers
    """
    ran_nums=[]

    num = random.randint(1,9)
    ran_nums.append(num)
    while len(ran_nums)<3:      # to be each numbers different
        nums = random.randint(1,9)
        if not nums in ran_nums:
            ran_nums.append(nums)
    return ran_nums

def user_nums():
    """
    user is able to input 3 numbers
    """
    usernums = []
    while len(usernums)<3:
        try:
            print("\nInput",len(usernums)+1, "th number :")
            user = int(input())
            if not user in usernums:
                usernums.append(user)
            else:
                print("\nThe digits must be all different")
        except ValueError:
            print("input integer number!")
    return usernums

def check_nums(rand_nums):
    """
    Compare random number created with number inputted
    """
    while 1:
        users_number = user_nums()
        print(users_number,rand_nums) # for check
        strike = 0
        ball = 0
        for i in range(len(users_number)):
            if users_number[i] in rand_nums:
                if users_number[i] == rand_nums[i]:
                    strike += 1
                else :
                    ball += 1

        if strike == 0 and ball == 0:
            print("------------------------")
            print("OUT !")
            print("------------------------")
        else:
            print("\n",strike,"strike"",",ball,"ball")
        if strike == 3:     # if match all numbers, escape
            print("------------------------")
            print("Congratulation! Success ! ")
            print("------------------------")
            break

def main():
    print("\n")
    print("------------------------")
    print("Start Baseball game!")
    print("------------------------")
    check_nums(create_rannums())

if __name__ == "__main__":
    main()