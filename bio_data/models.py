from django.db import models
# from django.core.exceptions import ValidationError
import uuid

# Create your models here.
class BioData(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    age = models.PositiveIntegerField()
    marital_status = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    alternate_phone_number = models.CharField(max_length=15, blank=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    
    height = models.FloatField(help_text= "Height in cm")
    weight = models.FloatField(help_text= "Weight in kg")
    blood_group = models.CharField(max_length=5)
    
    highest_qualification = models.CharField(max_length=100)
    university_name = models.CharField(max_length=150)
    year_of_passing = models.PositiveIntegerField()
    
    occupation = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150, blank=True)
    job_title = models.CharField(max_length=150, blank=True)
    years_of_experience = models.PositiveIntegerField()
    expected_salary = models.PositiveIntegerField(null=True, blank=True)
    
    website = models.URLField(blank=True)
    linkedin_profile = models.URLField(blank=True)
    github_profile = models.URLField(blank=True)
    
    skills = models.TextField(blank=True)
    languages_known = models.TextField(blank=True)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
