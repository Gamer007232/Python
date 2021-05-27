class Student:
    def check_pass_faild(self):
        if self.marks >= 40:
            return True
        else:
            return False

Student1 = Student()
Student1.mame = "harry"
Student1.marks = 85

did_pass = Student1.check_pass_faild()
print(did_pass)

Student2 = Student()
Student2.name = "Janet"
Student2.marks = 30
did_pass = Student2.check_pass_faild()
print(did_pass)
    