import random

import uuid
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from app.service_provider import app_service_provider
from app.dto.application_dto import *
from app.models import Application
from django.core.files.storage import FileSystemStorage

from app.utiles.utility import render_to_pdf
from django.views.generic import View


def create_application(request):
    basic = app_service_provider.basic_management_service().get_all_for_select_list()
    context = {
        'basic': basic
    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['message']:
        return redirect("application_slip", request.POST["email"])
    return render(request, 'application/create_application.html', context)


def __get_attribute_from_request(request: HttpRequest):
    create_application_dto = CreateApplicationDto()
    create_application_dto.basic_id = request.POST['basic']
    create_application_dto.first_name = request.POST['first_name']
    create_application_dto.last_name = request.POST['last_name']
    create_application_dto.email = request.POST['email']
    create_application_dto.passport = __save_image(request)
    return create_application_dto


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            application = __get_attribute_from_request(request)
            application.status = "pending"
            application.application_score = 0
            application.application_no = __get_application_number
            app_service_provider.application_management_service().create_application(application)
            context['message'] = 'successful'
        except Exception as e:
            context['saved'] = False
            raise e


def __save_image(request):
    image = request.FILES['passport']
    fs = FileSystemStorage()
    filename = fs.save(image.name, image)
    file = fs.url(filename)
    return file


def __get_application_number():
    code = "HDS"
    year_of_application = str(datetime.date.year)
    number = str(uuid.uuid4()).replace("-", "").upper()[0:5]
    application_number = code + year_of_application + number
    return application_number


def edit_application(request):
    context = {

    }
    __edit_if_post_method(request, context)
    if request.method == 'POST' and context['message']:
        return redirect("index")
    return render(request, '', context)


def __edit_attribute_from_request(request: HttpRequest):
    edit_application_dto = EditApplicationDto()
    edit_application_dto.first_name = request.POST['first_name']
    edit_application_dto.last_name = request.POST['last_name']
    edit_application_dto.email = request.POST['email']
    return edit_application_dto


def __edit_if_post_method(request, context):
    if request.method == 'POST':
        try:
            application = __edit_attribute_from_request(request)
            application.status = "pending"
            app_service_provider.application_management_service().edit_application(application.id)
            context['message'] = 'edit successful'
        except Exception as e:
            context['saved'] = False
            raise e


def list_applications(request):
    applications = app_service_provider.application_management_service().list_applications()
    context = {
        'tittle': 'List of applications',
        'applications': applications
    }
    return render(request, 'application/list_application.html', context)


def approve_application(request, id: int, application_id: str):
    application = EditApplicationDto()
    application.application_status = "Approved"
    application.student_id = id
    app_service_provider.application_management_service().edit_application(application_id=application_id,
                                                                           model=application)
    context = {
        "message": "successful"
    }
    return render(request, "index.html", context)


def pre_application(request):
    context = {

    }
    return render(request, 'application/pre_application.html', context)


def application_slip(request, email: str):
    applicant = app_service_provider.application_management_service().get_application(email=email)
    context = {
        'applicant': applicant
    }
    pdf = render_to_pdf('exam_slip.html', context)

    # rendering the template
    return HttpResponse(pdf, content_type='application/pdf')
