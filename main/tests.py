from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from .models import serviceUpdate, Profile
# Create your tests here.

# todo:
# Write test to add user to profile

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="djangoTest", password="Testinguser67!", first_name="Boris", last_name="Johnson", email="Boris.Johnson@test.com")

    def test_user_create_object(self):
        user1 = User.objects.get(username = "djangoTest")
        

        self.assertEqual(user1.username, "djangoTest")
        self.assertEqual(user1.first_name, "Boris")
        self.assertEqual(user1.last_name, "Johnson")

    def test_profile_object(self):
        user2 = User.objects.get(username = "djangoTest")
        print(user2.id)
        Profile.objects.filter(user_id=user2.id).update(clientid=76121, mobile_number='098437898432')

        userProfile2 = Profile.objects.get(user_id=user2.id)
        self.assertEqual(userProfile2.clientid, 76121)


    

# Test serviceUpdate model
class ServiceUpdateTestCase(TestCase):
    def setUp(self):
        serviceUpdate.objects.create(message="Service is down tomorrow bet 10 and 11")
    
    def test_service_update_object(self):
        message1 = serviceUpdate.objects.get(message="Service is down tomorrow bet 10 and 11")

        self.assertEqual(message1.message, "Service is down tomorrow bet 10 and 11")


