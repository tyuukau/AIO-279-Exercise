import unittest

from mod01.w03.ward import Ward, Student, Doctor, Teacher


class TestWard(unittest.TestCase):

    def test_add_person(self):
        """
        Test adding people to the ward.
        """
        ward = Ward(name="General Ward")
        student = Student(name="Alice", yob=2000, grade="A")
        doctor = Doctor(name="Dr. Smith", yob=1970, specialist="Cardiology")
        ward.add_person(student)
        ward.add_person(doctor)
        self.assertEqual(len(ward.people), 2)
        self.assertIn(student, ward.people)
        self.assertIn(doctor, ward.people)

    def test_describe(self):
        """
        Test the describe method of the ward.
        """
        ward = Ward(name="General Ward")
        student = Student(name="Alice", yob=2000, grade="A")
        doctor = Doctor(name="Dr. Smith", yob=1970, specialist="Cardiology")
        teacher = Teacher(name="Mr. Johnson", yob=1980, subject="Math")
        teacher2 = Teacher(name="Ms. Lee", yob=1985, subject="Science")
        ward.add_person(student)
        ward.add_person(doctor)
        ward.add_person(teacher)
        ward.add_person(teacher2)
        ward.describe()

    def test_count_doctor(self):
        """
        Test counting the number of doctors in the ward.
        """
        ward = Ward(name="General Ward")
        student = Student(name="Alice", yob=2000, grade="A")
        doctor = Doctor(name="Dr. Smith", yob=1970, specialist="Cardiology")
        teacher = Teacher(name="Mr. Johnson", yob=1980, subject="Math")
        ward.add_person(student)
        ward.add_person(doctor)
        ward.add_person(teacher)
        self.assertEqual(ward.count_doctor(), 1)
        ward.add_person(Doctor(name="Dr. Brown", yob=1980, specialist="Pediatrics"))
        self.assertEqual(ward.count_doctor(), 2)

    def test_sort_by_age(self):
        """
        Test sorting the people in the ward by year of birth.
        """
        ward = Ward(name="General Ward")
        student = Student(name="Alice", yob=2000, grade="A")
        doctor = Doctor(name="Dr. Smith", yob=1970, specialist="Cardiology")
        teacher = Teacher(name="Mr. Johnson", yob=1980, subject="Math")
        teacher2 = Teacher(name="Ms. Lee", yob=1985, subject="Science")
        ward.add_person(student)
        ward.add_person(doctor)
        ward.add_person(teacher)
        ward.add_person(teacher2)
        ward.sort_by_age()
        expected_order = [doctor, teacher, teacher2, student]
        self.assertEqual(ward.people, expected_order)

    def test_compute_average_teacher_yob(self):
        """
        Test computing the average year of birth of teachers in the ward.
        """
        ward = Ward(name="General Ward")
        teacher = Teacher(name="Mr. Johnson", yob=1980, subject="Math")
        teacher2 = Teacher(name="Ms. Lee", yob=1985, subject="Science")
        ward.add_person(teacher)
        ward.add_person(teacher2)
        self.assertAlmostEqual(ward.compute_average_teacher_yob(), (1980 + 1985) / 2)
        ward.add_person(Student(name="Bob", yob=2002, grade="B"))
        self.assertAlmostEqual(ward.compute_average_teacher_yob(), (1980 + 1985) / 2)
        ward.add_person(Doctor(name="Dr. Green", yob=1975, specialist="Neurology"))
        self.assertAlmostEqual(ward.compute_average_teacher_yob(), (1980 + 1985) / 2)
        ward.people = []
        self.assertEqual(ward.compute_average_teacher_yob(), 0.0)


if __name__ == "__main__":
    unittest.main()
