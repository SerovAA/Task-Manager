from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Labels
from task_manager.users.models import User


class TestLabels(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            username="johndoe",
        )
        Labels.objects.all().delete()

    def test_label_list(self):
        self.assertEqual(Labels.objects.count(), 0)

        Labels.objects.create(name="Work")
        Labels.objects.create(name="Personal")
        Labels.objects.create(name="Urgent")

        self.client.force_login(self.user)
        response = self.client.get(reverse("labels"))
        self.assertEqual(len(response.context["labels"]), 3)

    def test_label_create(self):
        self.assertEqual(Labels.objects.count(), 0)

        self.client.force_login(self.user)
        response = self.client.post(
            reverse("labels_create"), {"name": "Important"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("labels"))

        response = self.client.get(reverse("labels"))
        self.assertEqual(len(response.context["labels"]), 1)
        self.assertTrue(Labels.objects.filter(name="Important").exists())

    def test_label_update(self):
        label = Labels.objects.create(name="Work")

        self.assertEqual(Labels.objects.count(), 1)
        initial_name = label.name
        self.assertEqual(initial_name, "Work")

        self.client.force_login(self.user)
        response = self.client.post(
            reverse("labels_update", kwargs={"label_id": label.id}),
            {"name": "Work-related"},
        )
        self.assertEqual(response.status_code, 302)
        label.refresh_from_db()

        self.assertEqual(label.name, "Work-related")

    def test_label_delete(self):
        label = Labels.objects.create(name="Urgent")

        self.assertEqual(Labels.objects.count(), 1)

        self.client.force_login(self.user)
        response = self.client.post(
            reverse("labels_delete", kwargs={"label_id": label.id})
        )
        self.assertRedirects(response, reverse("labels"))
        self.assertEqual(response.status_code, 302)

        self.assertEqual(Labels.objects.count(), 0)
        self.assertFalse(Labels.objects.filter(pk=label.pk).exists())