from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

class TaskAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="pass123")
        self.client = APIClient()
        self.client.login(username="test", password="pass123")

        self.task = Task.objects.create(
            title="Test Task",
            name="Test Name",
            task_description="Test Desc",
            owner=self.user
        )

    def test_get_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        url = reverse('task-list')
        data = {
            "title": "New Task",
            "name": "New Name",
            "task_description": "Some desc"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task.id])
        data = {
            "title": "Updated",
            "name": "Updated Name",
            "task_description": "Updated desc",
            "completed": True
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
