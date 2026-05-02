import csv
import json
import unittest
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise TypeError("name must be a string")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be greater than 0")
        self._age = value

    @abstractmethod
    def get_details(self):
        pass

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self._grades = []

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

    @property
    def grades(self):
        return self._grades

    def get_details(self):
        print(f"{self.name} {self.age} {self.student_id} {self.average_grades}")

    @property
    def average_grades(self):
        if len(self._grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def __iadd__(self, grade):
        if not isinstance(grade, int) or not (0 <= grade <= 100):  # fix
            raise ValueError("Grade must be an integer")
        self._grades.append(grade)
        return self

    def __len__(self):
        return len(self.grades)


students = {}
with open("Studentt.csv", "r") as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)

    for row in reader:
        student_id, name, age, course, grade = row
        student_id = int(student_id)

        if student_id not in students:
            students[student_id] = Student(name, int(age), student_id)

        students[student_id] += int(grade)

for student in students.values():
    print(f"Name: {student.name}, Number of grades {len(student.grades)}", student.average_grades)

student_json = {}
with open("student.json", "r") as f:
    data = json.load(f)

for row in data:
    student_id = int(row["id"])
    name = row["name"]
    age = int(row["age"])
    course = row["course"]
    grade = int(row["grade"])

    if student_id not in student_json:
        student_json[student_id] = Student(name, age, student_id)
    student_json[student_id] += grade

for student in student_json.values():
    print(f"Name: {student.name}, Number of grades {len(student.grades)}", student.average_grades)


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Atanasia", 21, 1)

    def test_get_age(self):
        self.assertEqual(self.student.age, 21)

    def test_set_age_invalid(self):
        with self.assertRaises(ValueError):
            self.student.age = -123

    def test_get_set_age(self):
        self.student.age = 25          # fix
        self.assertEqual(self.student.age, 25)  # fix

    def test_iadd(self):
        self.student += 85             # fix
        self.assertIn(85, self.student.grades)

    def test_iadd_multiple(self):
        self.student += 80             # fix
        self.student += 90             # fix
        self.assertEqual(len(self.student), 2)

    def test_iadd_negative(self):
        with self.assertRaises(ValueError):
            self.student += -85

    def test_iadd_string(self):
        with self.assertRaises(ValueError):
            self.student += "85"

    def test_iadd_float(self):
        with self.assertRaises(ValueError):
            self.student += 8.5        # fix

if __name__ == "__main__":
    unittest.main()
















