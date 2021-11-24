from django.test import TestCase
from .models import Account
from unittest import mock

# Create your tests here.

#Testing models
class ModelTesting(TestCase):
    def test_assignment_model(self):
        philip = Account(firstname="Philip", lastname="K. Dick", email='test@test.test', username='test@test.test')
        philip.save()
        # user = Account.objects.create(email='test@test.test', password='12345')
        self.assertEqual(str(philip), "Philip K. Dick")
        self.assertEquals(philip.email, 'test@test.test')
        self.assertEquals(philip.username, 'test@test.test')
        self.assertEquals(philip.is_active, True)
        self.assertEquals(philip.is_admin, False)
