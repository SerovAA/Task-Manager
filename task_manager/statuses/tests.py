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

    def setUp(self):
        self.client.force_login(self.user)
        Statuses.objects.all().delete()

    def test_status_list(self):
        self.assertEqual(Statuses.objects.count(), 0)

        Statuses.objects.create(name="To Do")
        Statuses.objects.create(name="In Progress")
        Statuses.objects.create(name="Completed")

        response = self.client.get(reverse("statuses"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["statuses"]), 3)

    def test_status_create(self):
        self.assertEqual(Statuses.objects.count(), 0)

        response = self.client.post(
            reverse("statuses_create"),
            {"name": "On Hold"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("statuses"))

        self.assertEqual(Statuses.objects.count(), 1)
        self.assertTrue(Statuses.objects.filter(name="On Hold").exists())

    def test_status_update(self):
        status = Statuses.objects.create(name="To Do")

        self.assertEqual(Statuses.objects.count(), 1)
        initial_name = status.name
        self.assertEqual(initial_name, "To Do")

        response = self.client.post(
            reverse("statuses_update", kwargs={"status_id": status.id}),
            {"name": "Backlog"}
        )
        self.assertEqual(response.status_code, 302)
        status.refresh_from_db()

        self.assertEqual(status.name, "Backlog")

    def test_status_delete(self):
        status = Statuses.objects.create(name="Completed")

        self.assertEqual(Statuses.objects.count(), 1)

        response = self.client.post(
            reverse("statuses_delete", kwargs={"status_id": status.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("statuses"))

        self.assertEqual(Statuses.objects.count(), 0)
        self.assertFalse(Statuses.objects.filter(pk=status.pk).exists())