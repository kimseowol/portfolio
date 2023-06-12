import string
import random


class CreatePassword():
    """
    ++++++비밀번호 생성기+++++
    생성할 비밀번호 자릿값을 받아
    대문자, 소문자, 특수문자, 숫자를 
    모두 포함한 비밀번호를 생성
    """
    def __init__(self):
        self.self = self

    #chars범위 설정 (대문자,소문자,숫자,특수문자)
    def chars_source(self):
        chars = string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
        return chars

    #비밀번호 자릿수 설정
    def set_units(self):
        while 1:
            a = input("---\n생성할 비밀번호 자릿수를 입력하세요 : ")
            if not a.isnumeric():
                print("---\n다시 입력하세요")
                continue
            else:
                rangenum=int(a)
                if rangenum < 4:
                    print("---\n4이상 입력하세요")
                    continue
                break
        return rangenum

    #비밀번호 생성
    def create_password(self):
        units = self.set_units()
        while 1:
            pw=str()

            #비밀번호 chars안에서 조합
            for i in range(units):
                pw += random.choice(self.chars_source())

            upper = 0
            lower = 0
            digits = 0
            punctuation = 0

            #대문자, 소문자, 숫자, 특수문자 각각 있는지 확인
            for i in pw:
                if i in string.ascii_uppercase:
                    #print("upper",i)
                    upper += 1
                elif i in string.ascii_lowercase:
                    #print("lower",i)
                    lower += 1
                elif i in string.digits:
                    #print("digits",i)
                    digits += 1
                else:
                    #print("punctuation",i)
                    punctuation +=1
            
            #다 있으면 반복문 탈줄
            if upper*lower*digits*punctuation > 0:
                print("password : ",pw)
                break


if __name__== "__main__":
    pw = CreatePassword()
    pw.create_password()