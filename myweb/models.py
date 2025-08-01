from django.db import models
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.utils import timezone

class PhotoModel(models.Model):
    Profile_Image = models.ImageField(upload_to="Profile")        

    def photo_tag(self):
        if self.Profile_Image:
            return mark_safe(f"<img src='{self.Profile_Image.url}' width='100px' style='border-radius: 10px;' />")
        return "No Image"
    

class NameModel(models.Model):
    First_name = models.CharField(max_length=15)
    Last_name = models.CharField(max_length=15)
    Passion = models.CharField(max_length=30)

    def __str__(self):
        return self.First_name
    
def validate_pdf(file):
    if not file.name.endswith('.pdf'):
        raise ValidationError("Only PDF files are allowed.")
    
class ResumeModel(models.Model):
    resume = models.FileField(upload_to="Resume", validators=[validate_pdf])

class skillmodel(models.Model):
    title = models.CharField(max_length=30)
    logo = models.ImageField(upload_to="skill")

    def __str__(self):
        return self.title


    def Logo(self):
        if self.logo:
           return mark_safe(f"<img src='{self.logo.url}' width='100px'>")


class filter(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
    
class projectmodel(models.Model):
    Type = models.ForeignKey(filter,on_delete=models.CASCADE)
    Images = models.ImageField(upload_to="projects_photo")
    title = models.CharField(max_length=50)
    live_link = models.URLField()
    

    def __str__(self):
        return self.title
    

class contactmodel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    



    



