#data

#structure
class Person:
    def __init__(self):
        self.major="cs"
        self.grade="5"
        self.double_major="no"

class Class:
    def __init__(self,testnum):
        self.number=0

        self.name="Advanced mathmatic"+str(testnum)
        self.teacher="Gao Tie"
        self.day=testnum+2
        self.time=[testnum,testnum+1]
        
        self.general=84
        self.quality=66
        self.workload=100
        self.score=59

class Preference:
    def __init__(self,scores):
        self.morning8=scores[0]
        self.score=scores[1]
        self.workload=scores[2]

#functions
def get_recommend():
    classList=[classtest3,classtest4]
    recommendTables.clear()
    recommendTables.append([classtest3,classtest4])
    recommendTables.append([classtest1,classtest2])
    recommendTables.append([classtest1,classtest2])

#tempsave
user=Person()
classtest1=Class(1)
classtest2=Class(2)
classtest3=Class(3)
classtest4=Class(4)
classtabletest=[classtest1,classtest2]
testscores=[0,0,0]
testprefer=Preference(testscores)

majors=['cs','ai']

recommendTables=[[]]

politic_classes=[classtest1]
compulsory_classes=[classtest2]

mustlist=[]
nolist=[]

#培养方案必修
#培养方案选修
#思政
#英语
#体育
#通识
#跨院系
#其他