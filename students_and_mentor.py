class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        if self.grades:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return sum(all_grades) / len(all_grades)
        return 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {in_progress}\n"
                f"Завершенные курсы: {finished}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        if self.grades:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return sum(all_grades) / len(all_grades)
        return 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Функции для подсчета средней оценки
def average_student_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0


def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0


# Создание экземпляров
student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Jane', 'Doe', 'female')
student2.courses_in_progress += ['Python']

lecturer1 = Lecturer('Some', 'Lecturer')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('John', 'Smith')
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('Some', 'Reviewer')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Another', 'Reviewer')
reviewer2.courses_attached += ['Git']

# Выставление оценок
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 7)

# Вывод информации
print("Информация о студентах:")
print(student1)
print()
print(student2)

print("\nИнформация о лекторах:")
print(lecturer1)
print()
print(lecturer2)

print("\nИнформация о проверяющих:")
print(reviewer1)
print()
print(reviewer2)

# Сравнение
print("\nСравнение студентов:")
print(student1 > student2)

print("\nСравнение лекторов:")
print(lecturer1 > lecturer2)



# Подсчет средних оценок
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print("\nСредняя оценка за домашние задания по курсу Python:")
print(average_student_grade(students, 'Python'))

print("\nСредняя оценка за лекции по курсу Python:")
print(average_lecturer_grade(lecturers, 'Python'))
