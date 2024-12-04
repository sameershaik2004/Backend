from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {
            "title": "Sample Task",
            "description": "Sample Description",
            "due_date": "2024-12-31",
            "status": "OPEN"
        }
        self.task = Task.objects.create(**self.task_data)

    def test_create_task(self):
        response = self.client.post(reverse('task-list'), self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_tasks(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_task(self):
        response = self.client.get(reverse('task-detail', kwargs={'pk': self.task.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        updated_data = self.task_data.copy()
        updated_data["title"] = "Updated Title"
        response = self.client.put(reverse('task-detail', kwargs={'pk': self.task.id}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(reverse('task-detail', kwargs={'pk': self.task.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
