"""
Imports
"""
from django.test import TestCase
from django.contrib.auth.models import User

from profiles.models import UserProfile


class TestProfileModels(TestCase):
    """
    A class for testing the profile model
    """
    def setUp(self):
        """
        This setup creates a test user
        """
        testuser = User.objects.create_user(
            username='syler_test',
            password='syler_password',
            email='syler@syler.com')
        testuser.save()

    def tearDown(self):
        """
        Delete test user
        """
        User.objects.all().delete()

    def test_profile_str_method(self):
        """
        This test tests the users profile username
        """
        testuser = User.objects.get(username='syler_test')
        profile = UserProfile.objects.get(user=testuser)
        self.assertEqual(str(profile), profile.user.username)
