from django.db import models
from django.contrib.auth.models import User


class Registration(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Password = models.CharField(max_length=200)
    Registration_date = models.DateField()
    Qualification = models.TextField()
    Image = models.ImageField(upload_to='media')
    Average_review_rating = models.IntegerField()
    Num_of_reviews = models.IntegerField()
    About_website = models.TextField()
    User_role = models.CharField(max_length=200)
    user = models.OneToOneField(User,on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.First_name



class Messages(models.Model):
    Category = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    From_email = models.EmailField()
    To_email = models.EmailField()
    Message_content = models.TextField(default='Nil')



class Blogs(models.Model):
    Name = models.CharField(max_length=200)
    Blog_content = models.TextField()
    Image = models.ImageField()
    Date_blog = models.DateField()
    Approval_status = models.CharField(max_length=200)

class Requests(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    User_category = models.CharField(max_length=200)
    Old_password = models.CharField(max_length=200)
    New_password = models.CharField(max_length=200)
    Req_reg = models.ForeignKey(Registration, on_delete=models.SET_NULL, null = True)