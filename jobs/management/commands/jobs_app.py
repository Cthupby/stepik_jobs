from django.core.management import BaseCommand

from jobs.models import Company, Speciality, Vacancy
from jobs.data import jobs, companies, specialties


class Command(BaseCommand):
    help = 'Command for adding content from data to database'

    def handle(self, *args, **options):

        for company in companies:
            Company.objects.create(
                    name=company['title'],
                    location=company['location'],
                    description=company['description'],
                    employee_count=company['employee_count']
                )

        for speciality in specialties:
            Speciality.objects.create(
                    code=speciality['code'],
                    title=speciality['title'],
                )

        for job in jobs:
            Vacancy.objects.create(
                    title=job['title'],
                    speciality=Speciality.objects.get(code=job['specialty']),
                    company=Company.objects.get(pk=job['company']),
                    skills=job['skills'],
                    description=job['description'],
                    salary_min=job['salary_from'],
                    salary_max=job['salary_to'],
                    posted=job['posted']
            )
