from django.http import HttpRequest
from django.shortcuts import redirect, render
from app.service_provider import app_service_provider
from app.dto.basic_dto import *


def create_basic(request):
    context = {
        'title': 'Create Basic'
    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("index")
    return render(request, 'basic/create.html', context)


def __get_attribute_from_request(request: HttpRequest):
    create_basic_dto = CreateBasicDto()
    create_basic_dto.basic_name = request.POST['basic_name']
    return create_basic_dto


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            basic = __get_attribute_from_request(request)
            app_service_provider.basic_management_service().create_basic(basic)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e


def edit_basic(request, basic_id: int):
    basic = app_service_provider.basic_management_service().basic_details(basic_id)
    context = {
        'title': 'Edit Basic',
        'basic': basic
    }
    __edit_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("index")
    return render(request, 'basic/edit.html', context)


def __get_edit_attribute_from_request(request: HttpRequest):
    edit_basic_dto = EditBasicDto()
    edit_basic_dto.basic_name = request.POST['basic_name']
    return edit_basic_dto


def __edit_if_post_method(request, context):
    if request.method == 'POST':
        try:
            basic = __get_edit_attribute_from_request(request)
            app_service_provider.basic_management_service().edit_basic(
                basic)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e


def list_basic(request):
    basics = app_service_provider.basic_management_service().list_basic()
    context = {
        'tittle': 'List of Basics',
        'basics': basics
    }
    return render(request, 'basic/List.html', context)


def basic_details(request, basic_id: int):
    basic = app_service_provider.basic_management_service().basic_details(basic_id)
    context = {
        'tittle': 'Basic Details',
        'basic': basic
    }
    return render(request, 'basic/details.html', context)
