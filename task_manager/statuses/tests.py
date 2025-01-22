from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Statuses
from task_manager.users.models import User


class TestStatuses(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="johndoe",
            password="testpassword",
            first_name="John",
            last_name="Doe"
        )
        cls.todo_status = Statuses.objects.create(name="To Do")
        cls.in_progress_status = Statuses.objects.create(name="In Progress")
        cls.completed_status = Statuses.objects.create(name="Completed")

    def setUp(self):
        self.client.force_login(self.user)

    def test_status_list(self):
        response = self.client.get(reverse("statuses"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["statuses"]), 3)

    def test_status_create(self):
        response = self.client.post(
            reverse("statuses_create"),
            {"name": "On Hold"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("statuses"))
        self.assertEqual(Statuses.objects.count(), 4)
        self.assertTrue(Statuses.objects.filter(name="On Hold").exists())

    def test_status_update(self):
        response = self.client.post(
            reverse("statuses_update", kwargs={"status_id": self.todo_status.id}),
            {"name": "Backlog"}
        )
        self.assertEqual(response.status_code, 302)
        self.todo_status.refresh_from_db()
        self.assertEqual(self.todo_status.name, "Backlog")

    def test_status_delete(self):
        response = self.client.post(
            reverse("statuses_delete", kwargs={"status_id": self.completed_status.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("statuses"))
        self.assertEqual(Statuses.objects.count(), 2)
        self.assertTrue(Statuses.objects.filter(pk=self.todo_status.pk).exists())
        self.assertTrue(Statuses.objects.filter(pk=self.in_progress_status.pk).exists())
