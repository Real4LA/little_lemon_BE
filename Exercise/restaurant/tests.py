from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class RegistrationViewTests(TestCase):
    def test_registration_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register')

    def test_registration_success(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'Testpass123!',
            'password2': 'Testpass123!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration_complete.html')
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_registration_invalid(self):
        response = self.client.post(reverse('register'), {
            'username': '',
            'password1': 'pass',
            'password2': 'pass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertFormError(response, 'form', 'username', 'This field is required.')
