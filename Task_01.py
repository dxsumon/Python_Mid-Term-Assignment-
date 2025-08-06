class StudentDatabase:
    student_list = []
    student_count = 0 
    def __init__(self):
        pass
    @classmethod
    def add_student(cls,student_details):
        for student in cls.student_list:
            if student.student_id == student_details.student_id:
                print(f"This student is already Enroll")
                return
        cls.student_list.append(student_details)
        # print(f"{student_details.name} has been student Added")
        cls.student_count +=1
        
    @classmethod
    def view_student_info(cls):
        for student in cls.student_list:
            print(f"ID {student.student_id} Name: {student.name} Department: {student.department} Enrolled: {student.is_enrolled}")
            
    @classmethod
    def enrolling_student(cls):
        name = input("Name: ")
        roll = input("Roll: ")
        student_id = cls.student_count + 1
        age = input("Age: ")
        department = input("Department: ")
        semester = input("Semester: ")
        email = input("E-mail: ")
        phone_number = input("Phone: ")
        address = input("Address: ")
        is_enrolled = True
        new_student = Student(name, roll, student_id, age, department, semester, email, phone_number, address, is_enrolled)
        cls.add_student(new_student)
        
        
class Student(StudentDatabase):
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
        super().__init__()
    def enroll_student(cls):
        check_student_id = int(input("Enter student_ID: "))
        for student in cls.student_list:
            if student.student_id == check_student_id:
                if student.is_enrolled is False:
                    student.is_enrolled = True
                    return
        txt = input(f"""This Student ID: {check_student_id} is not enrolled!
        You want to enrolled? (Y/N): 
        """)
        print(txt)
        if txt.lower() == "y":
            cls.enrolling_student()
        else:
            return
    
    def drop_student(self):
        id = int(input("Enter Student ID to drop: "))
        for student in self.student_list:
            if student.student_id == id:
                print(f"Student {id} has been dropped")
                student.is_enrolled = False
                return
        print(f"This Student ID : {id} is not exist")
        
    def delete_student(self):
        id = int(input("Enter Student ID to drop: "))
        for student in self.student_list:
            if student.student_id == id:
                print(f"Student {id} has been dropped")
                self.student_list.remove(student)
                return
        print(f"This Student ID : {id} is not exist")

std1 = Student("Sumon Barmon",1,101,21,"Computer Department","5th","dxsumon14567@gmail.com", "01300999114", "Gazipur", True)
std2 = Student("Rahim Islam",2,102,22,"Computer Department","5th","rahimislam8870@gmail.com", "0139202302", "Dhaka", True)
std3 = Student("Mahim Hassan",3,103,22,"Computer Department","5th","mahimhassan@gmail.com", "0191291202", "Gazipur", True)


StudentDatabase.add_student(std1)
StudentDatabase.add_student(std2)
StudentDatabase.add_student(std3)

while True:
    print("---- Student Management Menu ----")
    choice = int(input(f"""1. View All Students
2. Enroll Student
3. Drop Student
4. Delete Student
5. Exit
Enter your Choice (1-5): """))
    print(choice)
    if choice == 1:
        StudentDatabase.view_student_info()
    elif choice == 2:
        std3.enroll_student()
    elif choice == 3:
        std3.drop_student()
    elif choice == 4:
        std3.delete_student()
    elif choice == 5:
        break
    else:
        print("Note: Invalid input please type (1-5) number only: ")