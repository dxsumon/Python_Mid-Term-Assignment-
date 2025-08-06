class StudentDatabase:
    student_list = []
    @classmethod
    def add_student(self,student_details):
        for student in self.student_list:
            if student.student_id == student_details.student_id:
                print(f"This student is already Enroll")
                return
        self.student_list.append(student_details)
        print(f"{student_details.name} has been student Added")
    # @classmethod
    # def show_all(self):
        
        
        
class Student():
    def __init__(self,roll, student_id, name, age, department, semester, email, phone, address):
        self.student_id = student_id
        self.name = name
        self.roll = roll
        self.age = age
        self.department = department
        self.semester = semester
        self.email = email
        self.phone = phone
        self.address = address
        
std1 = Student(667083,1456,"Sumon Barmon",21,"Computer Department","5th","dxsumon14567@gmail.com", "01300999114", "Gazipur")
std2 = Student(667083,1456,"Rahim Barmon",21,"Computer Department","5th","dxsumon14567@gmail.com", "01300999114", "Gazipur")
StudentDatabase.add_student(std1)