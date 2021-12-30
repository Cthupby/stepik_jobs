from django.db.models import Count
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError

from .models import Vacancy, Company, Speciality


def main_view(request):
    companies = Company.objects.all().annotate(vacancies_count=Count('vacancies'))
    specialities = Speciality.objects.all().annotate(vacancies_count=Count('vacancies'))

    context = {
        'specialities': specialities,
        'companies': companies
    }
    return render(request, "jobs/index.html", context=context)


def vacancies_view(request):
    vacancies = Vacancy.objects.all()

    context = {
        'vacancies': vacancies,
    }
    return render(request, "jobs/vacancies.html", context=context)


def speciality_view(request, speciality_id):
    try:
        category = Speciality.objects.get(code=speciality_id)
    except Speciality.DoesNotExist:
        raise Http404
    vacancies = Vacancy.objects.filter(speciality=category)

    context = {
        'vacancies': vacancies
    }
    return render(request, "jobs/vacancies.html", context=context)


def company_view(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        raise Http404
    vacancies = Vacancy.objects.filter(company=company)

    context = {
        'vacancies': vacancies,
        'title': company.name,
        'count': company.vacancies.count
    }
    return render(request, "jobs/company.html", context=context)


def vacancy_view(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(pk=vacancy_id)
    except Vacancy.DoesNotExist:
        raise Http404

    context = {
        'vacancy': vacancy,
    }
    return render(request, "jobs/vacancy.html", context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена.</h2>')


def custom_handler500(request):
    return HttpResponseServerError('<h2>Ошибка сервера.</h2>')
