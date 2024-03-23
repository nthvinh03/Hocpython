class Student:
    def __init__(self, masv, ho_ten, ngay_sinh, que_quan, nganh_hoc,ten_lop):
        self.masv = masv
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.que_quan = que_quan
        self.nganh_hoc = nganh_hoc
        self.ten_lop = ten_lop

class Student_List:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def remove_student(self, masv):
        for student in self.student_list:
            if student.masv == masv:
                self.student_list.remove(student)
                break

    def search_student(self, masv):
        for student in self.student_list:
            if student.masv == masv:
                return student
        return None

    def display_all_students(self):
        for student in self.student_list:
            print("Ma sinh vien: ", student.masv)
            print("Ho ten: ", student.ho_ten)
            print("Ngay sinh: ", student.ngay_sinh)
            print("Que quan: ", student.que_quan)
            print("Nganh hoc: ", student.nganh_hoc)
            print("Ten lop: ", student.ten_lop)
            print("-----------------------")

# Example usage:
# Create a Student_List object
student_list = Student_List()

# Create Student objects
student1 = Student("001", "Nguyen Van A", "1995-05-15", "Ha Noi", "Computer Science", "CS101")
student2 = Student("002", "Nguyen Thi B", "1997-09-22", "Ha Noi", "Business Administration", "BA202")
student3 = Student("003", "Tran Van C", "1998-03-10", "Ha Noi", "Engineering", "EN301")

# Add students to the student list
student_list.add_student(student1)
student_list.add_student(student2)
student_list.add_student(student3)

# Display all students
student_list.display_all_students()

# Search for a student
searched_student = student_list.search_student("002")
if searched_student:
    print("Found student with ID '002':", searched_student.ho_ten)
else:
    print("Student with ID '002' not found.")

# Remove a student
student_list.remove_student("001")

# Display all students again
student_list.display_all_students()