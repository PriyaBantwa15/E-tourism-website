from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils.safestring import mark_safe
# Create your models here.

class login(models.Model):
    email_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.email_id


class package(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    schemes = models.TextField()
    prices = models.IntegerField()

    def __str__(self):
        return self.name

class hotel(models.Model):
    package_id=models.ForeignKey(package,on_delete=models.CASCADE)
    active_cases = models.CharField(max_length=30)
    hotel_name=models.CharField(max_length=100)
    address_link=models.TextField()
    time=models.TimeField()
    location=models.CharField(max_length=50)

    def __str__(self):
        return self.hotel_name

class bookings(models.Model):
    package_id = models.ForeignKey(package,on_delete=models.CASCADE)
    login_id = models.ForeignKey(login,on_delete=models.CASCADE)
    first_name =models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    departure_Date = models.DateField()
    arrival_date = models.DateField()
    guest = models.IntegerField()
    certificate = models.FileField(upload_to='certificate')
    b_status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)


class feedback(models.Model):
    login_id = models.ForeignKey(login, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    ratting = models.CharField(max_length=20)
    comment = models.TextField()

class inquiry(models.Model):
    login_id = models.ForeignKey(login, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    i_status = models.IntegerField()

class place_detail(models.Model):
    package_id= models.ForeignKey(package, on_delete=models.CASCADE)
    place_name= models.CharField(max_length=50)
    desc = models.TextField()
    video = EmbedVideoField()