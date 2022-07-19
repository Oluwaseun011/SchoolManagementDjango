import random
from datetime import date

from django.http import HttpRequest
from django.shortcuts import redirect, render
from app.service_provider import app_service_provider
from app.dto.student_dto import *
from app.dto.application_dto import EditApplicationDto


def register_student(request):
    try:
        guardian_id = create_or_get_guardian(request)
        student = __get_attribute_from_request(request)
        student.guardian_id = guardian_id
        student.admin_no = __get_admin_no(request)
        student.date_created = date.today()
        student_id = app_service_provider.student_management_service().register_student(student)
        link_student_to_application(request, student_id)
        context = {
            "message": "successful"
        }
        return render(request, "index.html", context)
    except Exception as e:
        raise e


def __get_attribute_from_request(request: HttpRequest):
    register_student_dto = RegisterStudentDto()
    register_student_dto.basic_id = request.POST['basic_id']
    register_student_dto.admin_year = request.POST['admin_year']
    return register_student_dto


def __register_if_post_method(request, context):
    if request.method == 'POST':
        try:
            student = __get_attribute_from_request(request)
            student.admin_number = __get_admin_no(request)
            app_service_provider.student_management_service().register_student(student)
            context['message'] = 'successful, login to complete application'
        except Exception as e:
            context['saved'] = False
            raise e


def __get_admin_no(request):
    year = __get_attribute_from_request(request)
    tag = 'PK'
    admission_year = year.admin_year
    number = str(random.randint(1000, 9999))
    admin_no = tag + '/' + admission_year + '/' + number
    return admin_no


def edit_student(request, student_id: int):
    student = app_service_provider.student_management_service().student_details_by_user_id(student_id)
    context = {
        'title': 'Edit student',
        'student': student
    }
    __edit_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("index")
    return render(request, 'student/edit.html', context)


def __get_edit_attribute_from_request(request: HttpRequest):
    edit_student_dto = EditStudentDto()
    edit_student_dto.first_name = request.POST['first_name']
    edit_student_dto.last_name = request.POST['last_name']
    edit_student_dto.admission_year = request.POST['admission_year']
    edit_student_dto.date_of_birth = request.POST['date_of_birth']
    edit_student_dto.gender = request.POST['gender']
    return edit_student_dto


def __edit_if_post_method(request, context):
    if request.method == 'POST':
        try:
            student = __get_edit_attribute_from_request(request)
            app_service_provider.student_management_service().edit_student(
                student)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e


def list_students(request):
    student = app_service_provider.student_management_service().list_students()
    context = {
        'tittle': 'List of students',
        'students': student
    }
    return render(request, 'student/List.html', context)


def student_details(request, student_id: int):
    student = app_service_provider.student_management_service().student_details_by_user_id(student_id)
    context = {
        'tittle': 'student Details',
        'student': student
    }
    return render(request, 'student/Details.html', context)


def link_student_to_application(request, student_id: int):
    application = EditApplication()
    application.application_status = "pending"
    application.student_id = student_id
    app_service_provider.application_management_service().edit_application(application, user_id=request.user.id)
