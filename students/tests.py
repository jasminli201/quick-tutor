from django.test import TestCase
from students.models import StudentSignup
from django.contrib.auth.models import User

#test

class BasicTestCase(TestCase):
    def test_1eq1(self):
        self.assertTrue(1 == 1)

class StudentSignUpTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        StudentSignup.objects.create(phone_number="123-456-7890", classes="CS 3240", user=user)
        blank = User.objects.create_user('blank', 'blank@gmail.com', 'password')
        StudentSignup.objects.create(phone_number="5", classes="", user = blank)

    def test_student_equivalence(self):
        student = StudentSignup.objects.get(phone_number="123-456-7890")
        self.assertEqual(student.classes, "CS 3240")

    def test_student_boundary(self):
        blank = StudentSignup.objects.get(phone_number="5")
        self.assertEqual(blank.classes, "")

    def test_student_edit(self):
        student = StudentSignup.objects.get(phone_number="123-456-7890")
        student.phone_number="5"
        student.classes="CS 2150"
        student.save()
        self.assertEqual(student.phone_number,"5")
        self.assertEqual(student.classes,"CS 2150")