import json
from django.http import HttpRequest
from app.service_provider import app_service_provider
from app.dto.person_dto import *
from django.shortcuts import redirect, render
from app.utiles.decorators import login_required
from app.utiles.utility import hash_value


def create_user(request):
    context = {

    }
    __create_if_post_method(request, context)
    if context is not {}:
        return render(request, '', context)
    return render(request, '', context)


def __get_attribute_from_request_create(request):
    create_person_dto = CreatePersonDto()
    create_person_dto.first_name = request.POST['first_name']
    create_person_dto.last_name = request.POST['last_name']
    create_person_dto.email = request.POST['email']
    create_person_dto.password = request.POST['password']
    create_person_dto.confirm_password = request.POST['confirm_password']
    create_person_dto.telephone = request.POST['telephone']
    create_person_dto.gender = request.POST['gender']
    create_person_dto.address = request.POST['address']
    create_person_dto.date_of_birth = request.POST['date_of_birth']
    return create_person_dto


def __create_if_post_method(request, context: dict):
    if request.method == 'POST':
        user = __get_attribute_from_request_create(request)
        user.date_created = datetime.date.today()
        if user.password == user.confirm_password:
            result = app_service_provider.user_management_service().create_user(user)
            context['saved'] = result
        else:
            context['message'] = "Password dose not match"


@login_required
def edit_person(request, person_id: int):
    person: GetPersonDto = app_service_provider.person_management_service().get_person(person_id=person_id)
    context = {
        'Person': person
    }
    __edit_if_post_method(request, context, person_id)
    if request.method == 'POST':
        return redirect("list_user")
    return render(request, '', context)


def __get_attribute_form_request_edit(request):
    edit_person_dto = EditPersonDto()
    edit_person_dto.first_name = request.POST['first_name']
    edit_person_dto.last_name = request.POST['last_name']
    edit_person_dto.email = request.POST['email']
    edit_person_dto.telephone = request.POST['telephone']
    edit_person_dto.address = request.POST['address']
    edit_person_dto.gender = request.POST['gender']
    return edit_person_dto


def __edit_if_post_method(request, context: dict, person_id: int):
    if request.method == 'POST':
        person = __get_attribute_form_request_edit(request)
        result = app_service_provider.person_management_service().edit_person(person_id=person_id, model=person)
        context['saved'] = result


def login_get(request):
    next_url = request.session.get("next", '/')
    try:
        request.session.__delitem__("next")
    except KeyError:
        ...
    context = {
        'next': next_url

    }
    return render(request, '', context)


@login_required
def list_user(request):
    persons = app_service_provider.person_management_service().list_person()
    context = {
        'persons': persons
    }

    return render(request, '', context)


def login_post(request):
    context = {}
    person = LoginUserDto()
    redirect_field = request.GET['next']
    person.email = request.POST['email']
    person.password = request.POST['password']
    authenticated_user = authenticate(email=person.email, password=person.password)
    if authenticated_user:
        login(authenticated_user, request)
        return redirect(redirect_field)
    else:
        context['message'] = "email or password incorrect"
        context['next'] = redirect_field
        return render(request, '', context)


def authenticate(email: str, password: str):
    person = AuthenticateDto()
    person.password = hash_value(password)
    person.email = email
    person = app_service_provider.user_management_service().authenticate(person)
    if person:
        return person


def login(person: GetPersonDto, request: HttpRequest):
    person_data = json.dumps(person.__dict__)
    request.session.__setitem__("Person", person_data)


def logout(request: HttpRequest):
    try:
        request.session.__delitem__("Person")
    except KeyError:
        ...
    return redirect('home')


@login_required
def get_user(request, person_id: int):
    person = app_service_provider.person_management_service().get_user(person_id=person_id)
    if person:
        context = {
            'Person': person
        }
    else:
        context = {
            'message': 'Person not fount'
        }

    return render(request, '', context)
