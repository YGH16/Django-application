from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from ckeditor.fields import RichTextField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clientid = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " | ClientID: " + str(self.clientid)

    def FirstName(self):
        return self.user.first_name
        FirstName.short_description = 'Client First Name'
    
    def LastName(self):
        return self.user.last_name
        lastName.short_description = 'Client Surname'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Report(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='reports/', null=True, verbose_name="")
    
    class Meta:
        verbose_name = "Monthly Report"

    def __str__(self):
        return self.user.username + " | " + str(self.date)

    def FirstName(self):
        return self.user.first_name
    
    def LastName(self):
        return self.user.last_name
 
        
class ClientAgreement(models.Model):
    agreement_name = models.CharField(max_length=80, blank=False, null=True)
    pdf = models.FileField(upload_to='client-agreements/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " | " + self.agreement_name

    def FirstName(self):
        return self.user.first_name
    
    def LastName(self):
        return self.user.last_name

       
class QuarterlyReport(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, blank=False, null=True)
    pdf = models.FileField(upload_to='quarterlyreports/', null=True)

    def __str__(self):
        return self.user.username + " | " + str(self.date)

    def FirstName(self):
        return self.user.first_name
    
    def LastName(self):
        return self.user.last_name

class SupportTicket(models.Model):
    email = models.CharField(max_length=120, blank=True, null=True)
    subject = models.CharField(max_length=500, blank=True, null=True)
    detail = models.TextField()

    def __str__(self):
        return self.email + " | " + self.subject + " | " 

class serviceUpdate(models.Model):
    message = RichTextField()


    def __str__(self):
        return self.message
