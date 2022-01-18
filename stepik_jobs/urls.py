"""stepik_jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from jobs.views import main_view, vacancies_view, speciality_view, \
    company_view, vacancy_view
from jobs.views import custom_handler404, custom_handler500

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main_url'),
    path('vacancies/', vacancies_view, name='vacanies_url'),
    path('vacancies/cat/<str:speciality_id>/', speciality_view, name='speciality_url'),
    path('companies/<int:company_id>/', company_view, name='company_url'),
    path('vacancies/<int:vacancy_id>/', vacancy_view, name='vacancy_url'),
]


handler404 = custom_handler404
handler500 = custom_handler500


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
