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

        self.work_label = Labels.objects.create(name="Work")
        self.personal_label = Labels.objects.create(name="Personal")
        self.urgent_label = Labels.objects.create(name="Urgent")

    def test_label_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("labels"))
        self.assertEqual(len(response.context["labels"]), 3)

    def test_label_create(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("labels_create"), {"name": "Important"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("labels"))

        response = self.client.get(reverse("labels"))
        self.assertEqual(len(response.context["labels"]), 4)

    def test_label_update(self):
        self.client.force_login(self.user)
        label = self.work_label
        response = self.client.post(
            reverse("labels_update", kwargs={"label_id": label.id}),
            {"name": "Work-related"},
        )
        self.assertEqual(response.status_code, 302)
        label.refresh_from_db()
        self.assertEqual(label.name, "Work-related")

    def test_label_delete(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("labels_delete", kwargs={"label_id": self.urgent_label.id})
        )
        self.assertRedirects(response, reverse("labels"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Labels.objects.count(), 2)
        self.assertEqual(Labels.objects.get(pk=self.work_label.id).name, "Work")
        self.assertEqual(
            Labels.objects.get(pk=self.personal_label.id).name, "Personal")
