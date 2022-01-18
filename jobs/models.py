from django.contrib.auth.models import User
from django.db import models

from stepik_jobs.settings import MEDIA_SPECIALITY_IMAGE_DIR, MEDIA_COMPANY_IMAGE_DIR


class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR)
    location = models.CharField(max_length=50)
    description = models.TextField()
    employee_count = models.IntegerField()
    # owner = models.OneToOneField(User, on_delete=models.CASCADE)


class Speciality(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=40)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)


class Vacancy(models.Model):
    title = models.CharField(max_length=45)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=100)
    description = models.TextField()
    salary_min = models.DecimalField(max_digits=20, decimal_places=2)
    salary_max = models.DecimalField(max_digits=20, decimal_places=2)
    posted = models.DateField(auto_now=True)


class Application(models.Model):
    written_username = models.CharField(max_length=20)
    written_phone = models.IntegerField()
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
