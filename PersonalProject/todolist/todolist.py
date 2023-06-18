import csv
import os


class ToDoListAction():
    def __init__(self,mylist):
        self.mylist = mylist

    def getlist(self):
        """
        이 메서드는 self.mylist의 데이터를 프린트하여 가지고 있는 데이터의 정보를 보여줍니다.
        """
        print("------------")
        print("My todo list")
        print("------------")
        for i in range(len(self.mylist)):
            print(i+1, self.mylist[i][0], self.mylist[i][1])
        print("------------")
        return

    def addlist(self, addline):
        """
        이 메서드는 새로운 addline을 self.mylist에 추가합니다.
        추가 후에는 self.getlist()를 실행하여 추가된 내용을 확인 합니다.

        Args:
            addline (str): 새로운 Todo 아이템 문자열
        """
        for i in self.mylist:
            if addline == i[0]:
                print("이미 중복된 내용입니다.")
                return
        self.mylist.append([addline,"  "])
        self.getlist()
        return

    def editlist(self,num):
        """
        이 메서드는 self.mylist의 인덱스값을 받아 해당 self.mylist요소를 수정한다.
        수정 후 self.getlist()를 실행하여 수정한 내용을 확인한다.

        Args:
            num (int): self.mylist에서 수정할 index값
        """
        index = self.check_item(num)
        editline=input("편집할 내용 : ")
        self.mylist[index][0] = editline
        self.getlist()
        return

    def deletelist(self,num):
        """
        이 메서드는 self.mylist의 인덱스값을 받아 해당 self.mylist요소를 삭제한다.
        Args:
            num (int): self.mylist에서 삭제할 index값
        """
        index = self.check_item(num)
        del self.mylist[index]
        self.getlist()
        return

    def check_item(self, index):
        """
        주어진 인덱스값으로 self.mylist에서 해당 인덱스의 값을 확인하여 리턴합니다. 
        Args:
            index (int): self.mylist에서 확인할 인덱스값

        Returns
            int : item index 값
        """
        if index <= len(self.mylist[index-1][0]) + 1 and index != 0:
            return index-1
        else:
            print("다시 입력하세요")

    def done(self,num):
        """
        이 메서드는 self.mylist의 인덱스값을 받아 해당 self.mylist의 Done요소를 변경한다.
        수정 후 self.getlist()를 실행하여 수정한 내용을 확인한다. 

        Args:
            num (int): _description_
        """
        index = self.check_item(num)
        if self.mylist[index][1] == "V":
            self.mylist[index][1] = "  "
        elif self.mylist[index][1] == "  ":
        return self.getlist()

    def mypath(self):
        """
        todolist의 경로를 입력하고 접근한다.
        Returns:
            string : csv_path 
        """
        path = input("주소를 입력하시오 : ")
        csv_path = os.path.expanduser(path+"/todolist.csv")
        return csv_path

    def save(self):
        """
        self.mypath(self)를 통해 경로를 받아 csv파일을 열어 저장한다.
        """
        my_path = self.mypath()
        with open(my_path, 'w') as f:
            writer = csv.writer(f)
            for i in self.mylist:
                writer.writerow([i][0])
        return
    
    def load(self):
        """
        self.mypath(self)를 통해 경로를 받아 csv파일을 로드한다.
        Returns:
            list: self.mylist
        """
        mypath = self.mypath()
        with open(mypath, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.mylist.append(row)
        return self.mylist
        
    def create(self):
        """
        self.mypath(self)를 통해 경로를 받아 csv파일을 만든다.
        """
        mypath = self.mypath()
        with open(mypath, 'w') as f:
            writer = csv.writer(f)
        return
    
    def print_input_help(self):
        """
        유저가 입력하기 전
        현재 가지고 있는 리스트의 갯수를 출력 
        """
        print("------------")
        print("Select a number : ",1,"~",len(self.mylist))


if __name__=="__main__":
    print("\nToDoList를 만드시오\n")
    mylist=[]

    todo_action = ToDoListAction(mylist)

    try:
        """
        경로를 입력했을때 기존 파일이있으면 로드하고 없으면 새로 만듬
        """
        todo_action.load()
        print("\n load a list")
    except:
        print("\ncreate a list")

    while 1:
        act = input("원하는 행동을 입력하시오. get add edit delete done save 종료는 exit를 입력하시오")
        if act == "get":
            todo_action.getlist()
        elif act == "add":
            addline=input("추가할 내용 : ")
            todo_action.addlist(addline)
        elif act == "edit":
            todo_action.print_input_help()
            editnum=int(input("편집할 항목 순서를 입력하시오"))
            todo_action.editlist(editnum)
        elif act == "delete":
            todo_action.print_input_help()
            delnum=int(input("삭제할 항목 순서를 입력하시오"))
            todo_action.deletelist(delnum)
        elif act == "done":
            todo_action.print_input_help()
            donenum=int(input("다 한 항목을 입력하시오"))
            todo_action.done(donenum)
        elif act == "save":
            todo_action.save()
        elif act == "exit":
            print("종료합니다.")
            break
        else:
            print("다시 입력하세요")
