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
    @classmethod
    def view_student_info(self):
        for student in self.student_list:
            print(f"ID {student.student_id} Name: {student.name} Department: {student.department} Enrolled: {student.is_enrolled}")
        
class Student():
    def __init__(self, name,roll, student_id, age, department, semester, email, phone, address,is_enrolled):
        self.student_id = student_id
        self.name = name
        self.roll = roll
        self.age = age
        self.department = department
        self.semester = semester
        self.email = email
        self.phone = phone
        self.address = address
        self.is_enrolled = is_enrolled
        
std1 = Student("Sumon Barmon",1,101,21,"Computer Department","5th","dxsumon14567@gmail.com", "01300999114", "Gazipur", True)
std2 = Student("Rahim Islam",2,102,22,"Computer Department","5th","rahimislam8870@gmail.com", "0139202302", "Dhaka", True)
std3 = Student("Mahim Hassan",3,103,22,"Computer Department","5th","mahimhassan@gmail.com", "0191291202", "Gazipur", True)
std4 = Student("Mahim Hassan",3,103,22,"Computer Department","5th","mahimhassan@gmail.com", "0191291202", "Gazipur", True)
StudentDatabase.add_student(std1)
StudentDatabase.add_student(std2)
StudentDatabase.add_student(std3)
StudentDatabase.add_student(std4)
StudentDatabase.view_student_info()