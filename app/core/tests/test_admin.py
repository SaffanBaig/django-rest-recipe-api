from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model.objects.create_superuser(
            email = 'saffan@gmail.com',
            password = 'saffan123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model.objects.create_user(
            email = 'user@gmail.com',
            password = 'user123',
            name = 'Saffan'
        )

    def test_users_listed(TestCase):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page_change(TestCase):
        """Test that user edit works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_user_add_page(TestCase):
        """Test that user add page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
