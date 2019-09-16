from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successfull"""
        email = 'abc@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normailzed(self):
        """Test the email for a new user is normailzed"""
        email = 'test@ABC.COM'
        user = get_user_model().objects.create_user(email, 'abc123')
        self.assertEqual(user.email, email.lower())

    def test_user_new_invalid_email(self):
        """Test creating with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'abc123')

    def test_create_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'abc@gmail.com',
            'abc123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
