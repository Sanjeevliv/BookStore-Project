from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user= User.objects.create_user(
            username="Sanjeev", email="sanjeev@sanjeev.com", password="HelloIndia123"
        )
        self.assertEqual(user.username, "Sanjeev")
        self.assertEqual(user.email, "sanjeev@sanjeev.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="Sanjeevliv", email="sanjeevsethilive@gmail.com", password= "HelloIndia123"
        )
        self.assertEqual(admin_user.username, "Sanjeevliv")
        self.assertEqual(admin_user.email, "sanjeevsethilive@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)