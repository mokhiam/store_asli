from email import header
from wsgiref.headers import Headers
from django.test import TestCase

class ViewTests(TestCase):
    def test_Charge(self):
        data = {'cardnumber': '123', 'password': '123','cv2': '123'}
        response = self.client.post('/charge/1/',body=data,headers={'Authorization':'Token 523a49fc514ccd1b30ac7aaf0063760a3b1a18af'})
        self.assertEqual(response.status_code, 200)


