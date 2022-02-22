from django.test import TestCase

class ViewTests(TestCase):
    def test_signup(self):
        data = {'username': 'test', 'password1': 'test1234','password2': 'test1234'}
        response = self.client.post('/signup/', data=data)
        self.assertEqual(response.status_code, 200)
