import sqlite3

class Database:
    def __init__(self):
        self.con = None #connectiom
        self.cur = None 
        self.connectDatabase()
        self.createTable()
        
    def connectDatabase(self): #DB 연결 함수
        self.con = sqlite3.connect("EnrolmentDatabase.db")#test.db와의 연결 '상태'가 conn에 저장된다. 
        # + test.db가 같은 폴더에 있으면 실행, 없으면 생성
        self.cur = self.con.cursor() #통로를 통해서 값을 전달해주는 해석관, 내가 쓴 SQL 문법을 해석해서 DB로 가져감

    def createTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS Student (id TEXT, pw TEXT, name TEXT, age INTEGER, phonenumber TEXT, usercode INTEGER PRIMARY KEY AUTOINCREMENT)") #대소문자 구분하기
        self.cur.execute("CREATE TABLE IF NOT EXISTS Enrolment (usercode INTEGER, classname TEXT, FOREIGN KEY(usercode) REFERENCES Student(usercode))") #대소문자 구분하기
        self.cur.execute("PRAGMA foreign_keys = 1")
        
    def dataCreate(self,dataArr):
        data = dataArr
        self.cur.execute("INSERT INTO Student(id, pw, name, age, phonenumber) VALUES(?, ?, ?, ? ,? )", data) 
        self.con.commit()
    
    def getData(self,id):
        data = [id]
        self.cur.execute("SELECT * FROM Student WHERE id=?",data) 
        result = self.cur.fetchall() 
        return result

    def duplicateCheck(self,id): #중복체크
        data = [id]
        self.cur.execute("SELECT * FROM Student WHERE id=?",data)
        result = self.cur.fetchall() 
        if len(result) == 0:
            return True #아이디가 아직 없다는 것
        else:
            return False #아이디가 이미 있다는 것

    def signInCheck(self,id,pw): #아이디 로그인 체크
        data = [id]
        self.cur.execute("SELECT * FROM Student WHERE id=?",data)
        result = self.cur.fetchall() 
        if len(result) == 0: #아이디가 없거나, 잘못 입력했을 때,
            return False
        if int(result[0][1]) == int(pw):
            return True
        else:
            return False #비밀번호가 틀렸을때,

    #이 밑으로 4개를 중복코드로 작성한 거 같은데, db에서 컬럼명을 변수로 사용하지는 못하나 보네요
    def pwModify(self,id,newInfo):
        data = [newInfo,id]
        self.cur.execute("UPDATE Student SET pw=? WHERE id=?",data) 
        self.con.commit()

    def nameModify(self,id,newInfo):
        data = [newInfo,id]
        self.cur.execute("UPDATE Student SET name=? WHERE id=?",data) 
        self.con.commit()

    def ageModify(self,id,newInfo):
        data = [newInfo,id]
        self.cur.execute("UPDATE Student SET age=? WHERE id=?",data) 
        self.con.commit()

    def pnModify(self,id,newInfo):
        data = [newInfo,id]
        self.cur.execute("UPDATE Student SET phonenumber=? WHERE id=?",data) 
        self.con.commit()

    def accountDelete(self,id):
        data = [id]
        self.cur.execute("DELETE FROM Student WHERE id=?",data) 
        self.con.commit()
        
    def classEnroll(self,className,id):
        usercode = self.getusercode(id)
        data = [usercode,className]
        self.cur.execute("INSERT INTO Enrolment(usercode,classname) VALUES(?,?)", data) 
        self.con.commit()

    def getusercode(self,id):
        data = [id]
        self.cur.execute("SELECT * FROM Student WHERE id=?",data) 
        result = self.cur.fetchall() 
        return result[0][5]