from Account import *
from Database import *

class MainPage:

    def __init__(self):
        self.db = Database()
    
    def logic(self):
        while True: #로그인 함수 실행
            print("인하대학교에 오신 것을 환영합니다. 무엇을 하시겠습니까?")
            todoWhat = int(input("1. 로그인 2. 회원가입 : "))

            if todoWhat == 1: #로그인
                account = Account(self.db) #생성자에서 하면, 로그인과 계정생성을 다른 계정으로 못함
                account.signIn()

                if account.getSighInFlag() == True: #로그인 성공 후 기능 성공
                    while True:
                        userChoice = int(input("무엇을 하시겠습니까? 1. 내 정보 출력 2. 내 정보 수정 3. 회원탈퇴 4. 수강신청하기 5. 종료하기 : "))
                        
                        if userChoice == 1:
                            account.showMyInfo()
                        elif userChoice == 2:
                            account.modifyMyInfo()
                        elif userChoice == 3:
                            account.delAccount()
                            if account.getSighInFlag() == False:
                                break
                        elif userChoice == 4:
                            account.enrolling()
                        elif userChoice == 5:
                            break
                else: #로그인 실패 
                    pass

            elif todoWhat == 2: #회원가입
                account = Account(self.db)
                account.signUp()

    