"""
Imports
"""
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

from checkout.models import Order
from profiles.models import UserProfile


class TestProfileViews(TestCase):

    def setUp(self):
        """
        This setup creates a test user
        """
        testuser = User.objects.create_user(
            username='syler_test',
            password='syler_password',
            email='syler@syler.com')
        testuser.save()

        Order.objects.create(
            order_number='42424242',
            user_profile=UserProfile.objects.get(user=testuser),
            full_name='Syler User',
            email='syler@syler.com',
            phone_number='42424242',
            country='syler Country',
            postcode='syler postcode',
            town_or_city='syler city',
            street_address1='syler address',
            county='syler country',
        )

    def tearDown(self):
        """
        Delete test user and order
        """
        User.objects.all().delete()
        Order.objects.all().delete()

    def test_get_profile_page(self):
        """
        This test logins a test user and
        accesses their profile page
        """
        self.client.login(username='syler_test', password='syler_password')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_post_profile_page(self):
        """
        This test logins a test user and
        accesses their profile page
        """
        self.client.login(username='syler_test', password='syler_password')
        response = self.client.post('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_get_order_detail_page(self):
        """
        This test logins a test user and accesses
        the order history page
        """
        self.client.login(username='syler_test', password='syler_password')
        test_user = User.objects.get(username='syler_test')
        order = Order.objects.get(email=test_user.email)
        response = self.client.get('/profile/order_history/' +
                                   order.order_number)
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'This is a past confirmation for '
                         'order number 42424242. ' +
                         'A confirmation email was sent on the order date.')
