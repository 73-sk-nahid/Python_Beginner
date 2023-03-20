class Student:
    pass


class Marks:
    pass


sk_nahid = Student()  # instance of class Student()
passed = Marks()  # instance of class Marks()

check_student = isinstance(sk_nahid, Student)  # checking is instance?
print("sk_nahid is a instance of class Student--", check_student)
check_marks = isinstance(sk_nahid, Marks)  # checking is instance?
print("sk_nahid is a instance of class Marks--", check_marks)
check_student = isinstance(passed, Student)  # checking is instance?
print("passed is a instance of class Student--", check_student)
check_marks = isinstance(passed, Marks)  # checking is instance?
print("passed is a instance of class Marks--", check_marks)

check_student_subclass = isinstance(Student, object)  # classes are subclasses of the built-in object class or not
print("Student class is a subclass of object--", check_student_subclass)

check_marks_subclass = isinstance(Marks, object)  # classes are subclasses of the built-in object class or not
print("Marks class is a subclass of object--", check_marks_subclass)
