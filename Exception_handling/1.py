class Student:
    def __init__(self, RollNo,name):
        self.Rollno = RollNo
        self.name = name
        self.marks = None
    def display_detail(self):
        try:
            marks = int(input("Enter marks : "))
            if marks <= 0 or marks > 100:
                raise Exception("Invalid marks")
            self.marks = marks
        except Exception as e:
            print("Error : ",e)
        else:
            print("Display Student Details")
            print("Roll No : ",self.Rollno)
            print("Name : ",self.name)
            print("Marks : ",self.marks)
S = Student(20,"Raj") 
S.display_detail()


