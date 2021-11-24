from django.test import TestCase
from .models import Club

# Create your tests here.

#Testing models
# class ModelTesting(TestCase):
#     def test_club_model(self):
#         apala = Club.objects.create(name="Apala")
#         self.assertEqual(str(apala), "Apala")

# django.db.utils.IntegrityError: NOT NULL constraint failed: clubs_club.head_id