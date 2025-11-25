from django.test import TestCase, Client
from django.urls import reverse
from .models import Student
import json


class StudentApiTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse("student-list")
        self.crud_url = reverse("student-view")

    def test_should_list_students(self):
        Student.objects.create(name="Alice", address="Paris")

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        body = json.loads(response.content)
        self.assertEqual(len(body["students"]), 1)
        self.assertEqual(body["students"][0]["name"], "Alice")

    def test_should_create_student(self):
        payload = json.dumps({"name": "Bob", "address": "London"})

        response = self.client.post(
            self.crud_url,
            data=payload,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.count(), 1)
        student = Student.objects.first()
        self.assertEqual(student.name, "Bob")
        self.assertEqual(student.address, "London")
