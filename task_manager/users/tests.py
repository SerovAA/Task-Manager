from django.test import TestCase
from django.urls import reverse
from task_manager.users.models import User

class TestUsers(TestCase):
    def setUp(self):
        self.assertEqual(User.objects.count(), 0)

        self.user1 = User.objects.create(
            first_name="John", last_name="Doe", username="johndoe"
        )
        self.user2 = User.objects.create(
            first_name="Jane", last_name="Smith", username="janesmith"
        )

    def test_users_home(self):
        self.assertEqual(User.objects.count(), 2)

        response = self.client.get(reverse("users"))
        self.assertEqual(len(response.context["user"]), 2)

    def test_users_create(self):
        self.assertEqual(User.objects.count(), 2)

        response = self.client.get(reverse("users_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="actions/create_or_update.html")

        response = self.client.post(
            reverse("users_create"),
            {
                "first_name": "Alice",
                "last_name": "Johnson",
                "username": "alicejohnson",
                "password1": "AlicePass123",
                "password2": "AlicePass123",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))

        user = User.objects.last()
        self.assertEqual([user.first_name, user.last_name, user.username], ["Alice", "Johnson", "alicejohnson"])

        self.assertEqual(User.objects.count(), 3)

        response = self.client.get(reverse("users"))
        self.assertEqual(len(response.context["user"]), 3)

    def test_users_update(self):
        user = self.user2

        self.assertEqual(User.objects.count(), 2)

        response = self.client.get(reverse("users_update", kwargs={"user_id": user.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))

        self.client.force_login(user)
        response = self.client.get(reverse("users_update", kwargs={"user_id": user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="actions/create_or_update.html")

        response = self.client.post(
            reverse("users_update", kwargs={"user_id": user.id}),
            {
                "first_name": "Terry",
                "last_name": "Miller",
                "username": "terrymiller",
                "password1": "TerryPass123",
                "password2": "TerryPass123",
            },
        )

        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.first_name, "Terry")
        self.assertEqual(User.objects.count(), 2)

    def test_users_delete(self):
        user = self.user2

        self.assertEqual(User.objects.count(), 2)

        response = self.client.get(reverse("users_delete", kwargs={"user_id": user.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))

        self.client.force_login(user)
        response = self.client.get(reverse("users_delete", kwargs={"user_id": user.id}))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse("users_delete", kwargs={"user_id": user.id}))
        self.assertRedirects(response, reverse("users"))

        self.assertEqual(User.objects.count(), 1)