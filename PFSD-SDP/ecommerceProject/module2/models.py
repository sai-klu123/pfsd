from django.db import models
class Register_user(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    phonenumber = models.BigIntegerField(max_length=10)
    password = models.CharField(max_length=100)
    class Meta:
        db_table="Register_user"
class contact_fb(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField(primary_key=True)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    class Meta:
       db_table="contact_fb"
