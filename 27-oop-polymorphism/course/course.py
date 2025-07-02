from file_manager import *
from utils import *
import random

"""
JsonManager() -> class variable -> teachers.json, courses.json, students.json
Student() -> name, phone_number
Teacher() -> name, phone_number, experience, profession
Course() -> name, price, teacher(object)
"""


class Course:
    def __init__(self):
        self.teacher_manager = JsonManager(filename="teachers")
        self.courses_manager = JsonManager(filename="courses")
        self.students_manager = JsonManager(filename="students")

    def create_course(self):
        name = input("name: ")
        price = input("price: ")
        teacher_phone_num = input("phone number: ")

        course = {
            "name": name,
            "price": price,
            "teacher_phone_num": teacher_phone_num
        }
        courses = self.courses_manager.read_file()
        courses.append(course)
        self.courses_manager.write_file(data=courses)
        print("course is added")

    def register_to_course(self):
        name = input("full name: ")
        email = input("email: ")
        phone_num = input("phone number: ")
        course = input("course: ")
        new_id = self.students_manager.generate_new_id()

        random_num = random.randint(1000, 10000)
        send_email(receiver_email=email, body=str(random_num))
        if self.check_otp(correct_code=random_num):
            student = {
                "id": new_id,
                "full_name": name,
                "email": email,
                "phone_num": phone_num,
                "course": course
            }
            students = self.students_manager.read_file()
            students.append(student)
            self.students_manager.write_file(data=students)
            print("Registration successful")
            return True
        print("try again")
        return False

    def check_otp(self, correct_code):
        code = input("enter the code: ")
        return code == str(correct_code)

    def delete_course(self):
        name = input("name: ")
        courses = self.courses_manager.read_file()
        for c in courses:
            if c["name"] == name:
                courses.remove(c)
                self.courses_manager.write_file(courses)
                print("Course is deleted")
                return

        print("course is not found")


    def get_registered_courses(self):
        registered_courses = []
        phone_num = input("phone num: ")
        students = self.students_manager.read_file()
        for student in students:
            if student.get("phone_num") == phone_num and "course" in student:
                registered_courses.append(student["course"])
        if registered_courses:
            print(f"Registered courses for {phone_num}:")
            for course in registered_courses:
                print(f"- {course}")
        else:
            print("this phone number is not found")

    def get_users_by_course(self):
        users = []
        course = input("course: ")
        students = self.students_manager.read_file()

        for student in students:
            if student.get("course") == course and "full_name" in student:
                users.append(student["full_name"])

        if users:
            print(f"registered users for {course}:")
            for u in users:
                print(f"- {u}")
        else:
            print("no users found")


class Teacher(Course):
    def __init__(self):
        super().__init__()

    def create(self):
        name = input("Name: ")
        phone_num = input("Phone number: ")
        age = int(input("Age: "))
        profession = input("Profession: ")

        teacher = {
            "name": name,
            "phone_num": phone_num,
            "age": age,
            "profession": profession
        }

        teachers = self.teacher_manager.read_file()
        teachers.append(teacher)
        self.teacher_manager.write_file(data=teachers)
        print("New teacher created")

    def delete(self):
        phone_num = input("phone number: ")
        teachers = self.teacher_manager.read_file()
        for teacher in teachers:
            if teacher["phone_num"] == phone_num:
                teachers.remove(teacher)
                self.teacher_manager.write_file(teachers)
                print("Teacher is deleted")
                return

        print("no teacher with this phone number")
