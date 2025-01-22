from django.test import TestCase
from django.urls import reverse

from task_manager.users.models import User


class TestUsers(TestCase):
    def setUp(self):
        User.objects.create(
            first_name="N1",
            last_name="F1",
            username="U1",
        )
        User.objects.create(
            first_name="N2",
            last_name="F2",
            username="U2",
        )

    def test_users_home(self):
        response = self.client.get(reverse("users"))
        self.assertTrue(len(response.context["user"]), 2)

    def test_users_create(self):
        response = self.client.get(reverse("users_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="actions/create_or_update.html"
        )

        response = self.client.post(
            reverse("users_create"),
            {
                "first_name": "N3",
                "last_name": "F3",
                "username": "U3",
                "password1": "userQwerty123",
                "password2": "userQwerty123",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))

        user = User.objects.last()
        self.assertEqual(
            [user.first_name, user.last_name, user.username], ["N3", "F3", "U3"]
        )

        response = self.client.get(reverse("users"))
        self.assertTrue(len(response.context["user"]), 3)

    def test_users_update(self):
        user = User.objects.get(id=2)

        response = self.client.get(
            reverse("users_update", kwargs={"user_id": user.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))

        self.client.force_login(user)
        response = self.client.get(
            reverse("users_update", kwargs={"user_id": user.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="actions/create_or_update.html"
        )
        response = self.client.post(
            reverse("users_update", kwargs={"user_id": user.id}),
            {
                "first_name": "T222",
                "last_name": "M222",
                "username": "TM222",
                "password1": "TM222222TM222222",
                "password2": "TM222222TM222222",
            },
        )
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.first_name, "T222")

    def test_users_delete(self):
        user = User.objects.get(username="U2")
        response = self.client.get(
            reverse("users_delete", kwargs={"user_id": user.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))

        self.client.force_login(user)
        response = self.client.get(
            reverse("users_delete", kwargs={"user_id": user.id})
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse("users_delete", kwargs={"user_id": user.id})
        )
        self.assertRedirects(response, reverse("users"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)