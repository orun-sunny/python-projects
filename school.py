class Student:
    def __init__(self,name,current_class,id):
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self) -> str:
        return f'student with name: {self.name},class:{self.current_class},id:{self.id}'
class Teacher:
    def __repr__(self,name,subject,id):
        self.name =name
        self.subject = subject
        self.id = id

    def __refr__(self) ->str:
        return f'Teacher : {self.name},subject: {self.subject}'
class School:
    def __init__(self,name) -> None:
        self.name = name
        self.teachera= []
    def add_teacher(self,name,subject):
        id = len(self.teachers)+101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee <6500:
            return 'not enough'
        else:
            id = len(self.students)+1
            student = Student(name,'C',id)
            self.students.append(student)
            return f'{name} is enrolled with id:{id},extra money {fee-6500}'
        def __refr__(self) ->str:
            print('welcome to',self.name)
            print('-----------Our Teacher---------')
            for teacher in self.teachers:
                print(teacher)
            print('---------oue students---')
            for student in self.students:
                print(student)
# alia = Student('Alia torkari',9,1)
# orun = Teacher('orunpro', 'Algorithn',100)

# print(orun)
# print(alia)
        
phitron = School('Phitron')
phitron.enroll=('alia',5200)
phitron.enroll=('rani',8000)
phitron.enroll('orun',7000)

phitron.add_teacher("ashik",'Ds')
phitron.add_teacher("Rabbe",'Algo')
phitron.add_teacher("ashikaaa",'Data')