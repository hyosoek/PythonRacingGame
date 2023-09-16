from Database import *

class Account:

    def __init__(self,db):
        self.id = None
        self.pw = None
        self.name =None
        self.phoneNumber = None
        self.age = None
        self.db = db
        self.sighInFlag = False


    def signIn(self): #로그인을 해줍니다.
        id = input("아이디를 입력해주십시오. : ")
        pw = int(input("비밀번호를 입력해주십시오. : "))
        if self.db.signInCheck(id,pw) == True:
            print("비밀번호가 일치합니다.")
            self.id = id
            self.pw = pw
            print("로그인 완료!")
            self.sighInFlag = True
        else:
            print("로그인 실패!")


    def signUp(self):
        id = input("새 아이디를 입력해주십시오. : ")
        pw = int(input("새 비밀번호를 입력해주십시오. : "))
        name = input("이름을 입력해주십시오. : ")
        age = int(input("나이를 입력해주십시오. : "))
        phoneNumber = input("전화번호를 입력해주십시오. : ")
        if self.db.duplicateCheck(id) == True:
            print("중복체크 완료")#중복 확인 됐으면 나오는 메시지
            self.id = id
            self.pw = pw
            self.name = name
            self.age = age
            self.phoneNumber = phoneNumber
            self.db.dataCreate(id,pw,name,age,phoneNumber)
            print("계정 등록 완료")
        else:
            print("이미 있는 계정입니다.")


    def showMyInfo(self):
        infoArr = self.db.getData(self.id) #self 변수에 접근해야해서 따로 함수 만듬
        #메인 로직에서 바로 데이터베이스 접근하면, account 계정의 id 전역변수 접근을 해야함 -그럼 새로 get 함수
        print("아이디 : "+ infoArr[0][0])
        print("비밀 번호 : "+ str(infoArr[0][1]))
        print("이름 : "+ infoArr[0][2])
        print("나이 : "+ str(infoArr[0][3]))
        print("전화번호 : "+ str(infoArr[0][4]))


    def modifyMyInfo(self):
        print(self.id)
        whichInfoModify = int(input("어떤 정보를 수정하시겠습니까? 1.비밀번호 2.이름 3.나이 4.전화번호 : "))
        if whichInfoModify == 1:
            newPw = input("수정할 비밀번호는? : ")
            self.db.pwModify(self.id,newPw)
        if whichInfoModify == 2:
            newName = input("수정할 이름는? : ")
            self.db.nameModify(self.id,newName)
        if whichInfoModify == 3:
            newAge = int(input("수정할 나이는? : "))
            self.db.ageModify(self.id,newAge)
        if whichInfoModify == 4:
            newNum = input("수정할 전화번호는? : ")
            self.db.pnModify(self.id,newNum)

    def delAccount(self):
        deleteConfirm = int (input("진짜로 계정을 삭제하시겠습니까? 삭제하시려면 1을 눌러주십시오"))
        if deleteConfirm == 1:
            self.db.accountDelete(self.id)
            self.sighInFlag = False
            print("삭제 완료. 메인으로 돌아갑니다.")

    def getSighInFlag(self):
        return self.sighInFlag

    def enrolling(self):
        className = input("수강할 과목 이름을 입력해주십시오.")
        self.db.classEnroll(className,self.id)

        

    