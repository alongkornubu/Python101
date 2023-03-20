class School:
    # Attribute
    schoolName = 'ลุงวิศวกร สอนคำนวณ'
    
    # Constructor
    def __init__(self,subject='Pyton Programming'):
        print('ให้แสดงข้อความนี้ เมื่อมีการสร้าง Instance')
        self.subject = subject
        
    # Method
    def hello(self):
        print('สวัสดีตอนเช้า ยินดีต้อนรับนักเรียนทุกคน')
    def teach(self):
        print(f'โรงเรียนนี้ เปิดสอนวิชา {self.subject}')
    
class Student(School):
    def __init__(self,fullname, level,scores,subject):
        super().__init__(subject)
        self.fullname = fullname
        self.level = level
        self.scores = scores
    
    def checkGrade(self):
        if self.scores >= 80:
            print(f'วิชา {self.subject} ได้เกรด A')
        elif self.scores >= 70:
            print(f'วิชา {self.subject} ได้เกรด B')
        elif self.scores >= 60:
            print(f'วิชา {self.subject} ได้เกรด C')
        elif(self.scores >= 50):    
            print(f'วิชา {self.subject} ได้เกรด D')
        else:    
            print(f'วิชา {self.subject} ได้เกรด F')    
# Instance
# school1 = School('Mathmetric')
# print(f'ชื่อโรงเรียน: {school1.schoolName}')
# school1.hello()
# school1.teach()
print('========================')
student01 = Student('มาณี ลมโชย', 1 , 75,'math')
print(f'ชื่อโรงเรียน: {student01.schoolName}')
print(f'ชื่อนักเรียน: {student01.fullname}')
print(f'ระดับชั้น: {student01.level}')
print(f'คะแนนสอบ: {student01.scores}')
student01.checkGrade()
print('=================')
student02 = Student('ปลาหยุด ห้าวจัง',7, 90, 'science')
print(f'ชื่อโรงเรียน: {student02.schoolName}')
print(f'ชื่อนักเรียน: {student02.fullname}')
print(f'ระดับชั้น: {student02.level}')
print(f'คะแนนสอบ: {student02.scores}')
student02.checkGrade()

