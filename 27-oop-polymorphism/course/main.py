from course import Course, Teacher
def main():
    print("""
Menu:
    1. Create a new teacher: name, phone_number, profession, age
    2. Create a course: name, price, teacher_phone_number
    3. Register to course: name, email, phone_number, id
    4: Delete a course: name
    5: Delete a teacher: phone_number
    6: Get registered courses: phone_number
    7. Get users by course: course_name
    8. Exit
""")

    choice = input("enter your choice: ")
    courses = Course()
    teachers = Teacher()
    if choice == "1":
        teachers.create()
    elif choice == "2":
        courses.create_course()
    elif choice == "3":
        courses.register_to_course()
    elif choice == "4":
        courses.delete_course()
    elif choice == "5":
        teachers.delete()
    elif choice == "6":
        courses.get_registered_courses()
    elif choice == "7":
        courses.get_users_by_course()
    elif choice == "8":
        print("good bye")
        return None
    else:
        print("invalid choice")

    return main()

if __name__ == '__main__':
    main()


