class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
      return f'Имя: {self.name}\nФамилия: {self.surname}\nСредний балл за ДЗ: {self.m_grade()}\nКурсы в прцессе мзучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
     
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Error')
            return
        return self.m_grade() < other.m_grade()

    def m_grade(self):
        grade_list = []  
        for grade in self.grades.values():
            grade_list += grade
        # print(self.grades)
        # print(grade_list)
        return sum(grade_list)/len(grade_list)  


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'

  
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
      return f'Имя: {self.name}\nФамилия: {self.surname}\nСредний балл: {self.m_grade()}'
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Error')
            return
        return self.m_grade() < other.m_grade()

    def m_grade(self):
        grade_list = []  
        for grade in self.grades.values():
            grade_list += grade
        return sum(grade_list)/len(grade_list)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def students_m_grade(students, course):
    a = []
    if not isinstance(students, list):
        return
    for student in students:
        if isinstance(student, Student) and course in student.grades.keys():
            a += student.grades[course]
    if not len(a):
        return
    return sum(a)/len(a)


def lectors_m_grade(lectors, course):
    a = []
    if not isinstance(lectors, list):
        return
    for lector in lectors:
        if isinstance(lector, Lecturer) and course in lector.grades.keys():
            a += lector.grades[course]
    if not len(a):
        return
    return sum(a)/len(a)

best_reviewer = Reviewer('Jack', 'Ivanov') 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Jenny', 'Smith', 'female')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['JavaScript']
student_2.finished_courses += ['Введение в программирование']

# Create 2 instances of class Reviewer
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Helen', 'Green')
reviewer_2.courses_attached += ['Git']
reviewer_2.courses_attached += ['JavaScript']

# Create 2 instances of class Lecturer
lecturer_1 = Lecturer('John', 'Smith')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Ivan', 'Ivanov')
lecturer_2.courses_attached += ['Python', 'JavaScript']


# Call all created methods of the classes

# Call Student's method to rate lectures
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Git', 10)
student_1.rate_hw(lecturer_2, 'Python', 10)
student_2.rate_hw(lecturer_1, 'Python', 10)
student_2.rate_hw(lecturer_2, 'Python', 9)
student_2.rate_hw(lecturer_2, 'JavaScript', 10)

# Call Reviewer's method to rate student's homework
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_2, 'JavaScript', 10)


# Call overloaded __str__method of all clases
# also protected method to calculate mean grade will be called from __str__ method
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)


# Call overloaded methods to compare instances of classes by their mean grade
print(student_1 < student_2)
print(student_1 > student_2)
print(lecturer_1 == lecturer_2)
print(lecturer_1 < lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 == lecturer_2)


# Calculate mean grades

print(students_m_grade([student_1, student_2], 'Python'))
print(lectors_m_grade([lecturer_1, lecturer_2], 'Python'))