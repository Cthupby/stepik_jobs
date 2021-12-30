from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.URLField(default='https://place-hold.it/100x60')
    location = models.CharField(max_length=50)
    description = models.TextField()
    employee_count = models.IntegerField()


class Speciality(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=40)
    picture = models.URLField(default='https://place-hold.it/100x60')


class Vacancy(models.Model):
    title = models.CharField(max_length=45)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=100)
    description = models.TextField()
    salary_min = models.DecimalField(max_digits=20, decimal_places=2)
    salary_max = models.DecimalField(max_digits=20, decimal_places=2)
    posted = models.DateField(auto_now=True)
