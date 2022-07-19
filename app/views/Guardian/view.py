from django.http import HttpRequest
from django.shortcuts import redirect, render
from app.service_provider import app_service_provider
from app.dto.GuardianDto import *


def create_or_get_guardian(request):
    try:
        guardian = __get_guardian_attribute_from_request(request)
        registered_guardian = app_service_provider.guardian_management_service().guardian_details(email=guardian.guardian_email)
        if registered_guardian is not None:
            guardian_id = registered_guardian.id
            return guardian_id
        else:
            guardian_id = app_service_provider.guardian_management_service().register_guardian(guardian)
            return guardian_id
    except Exception as e:
        raise e


def __get_guardian_attribute_from_request(request: HttpRequest):
    register_guardian_dto = RegisterGuardianDto()
    register_guardian_dto.guardian_first_name = request.POST['guardian_first_name']
    register_guardian_dto.guardian_last_name = request.POST['guardian_last_name']
    register_guardian_dto.guardian_email = request.POST['guardian_email']
    register_guardian_dto.phone_number = request.POST['phone_number']
    register_guardian_dto.address = request.POST['address']
    return register_guardian_dto


def edit_guardian(request, guardian_id: int):
    guardian = app_service_provider.guardian_management_service().guardian_details_by_user_id(guardian_id)
    context = {
        'title': 'Edit Guardian',
        'guardian': guardian
    }
    __edit_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("index")
    return render(request, 'guardian/edit.html', context)


def __get_edit_attribute_from_request(request: HttpRequest):
    edit_guardian_dto = EditGuardianDto()
    edit_guardian_dto.username = request.POST['username']
    edit_guardian_dto.first_name = request.POST['first_name']
    edit_guardian_dto.last_name = request.POST['last_name']
    edit_guardian_dto.email = request.POST['email']
    edit_guardian_dto.password = request.POST['password']
    edit_guardian_dto.confirm_password = request.POST['confirm_password']
    edit_guardian_dto.date_of_birth = request.POST['date_of_birth']
    edit_guardian_dto.phone_number = request.POST['phone_number']
    edit_guardian_dto.qualification = request.POST['qualification']
    edit_guardian_dto.gender = request.POST['gender']
    return edit_guardian_dto


def __edit_if_post_method(request, context):
    if request.method == 'POST':
        try:
            guardian = __get_edit_attribute_from_request(request)
            app_service_provider.guardian_management_service().edit_guardian(
                guardian)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e


def list_guardians(request):
    guardians = app_service_provider.guardian_management_service().list_guardians()
    context = {
        'tittle': 'List of Guardians',
        'guardians': guardians
    }
    return render(request, 'guardian/List.html', context)


def guardian_details(request, guardian_id: int):
    guardian = app_service_provider.guardian_management_service().guardian_details_by_user_id(guardian_id)
    context = {
        'tittle': 'Guardian Details',
        'guardian': guardian
    }
    return render(request, 'guardian/details.html', context)


def __check_if_student_record_available(request):
    student = request.POST.get("first_name")
    if student == "":
        return False
    else:
        return True
