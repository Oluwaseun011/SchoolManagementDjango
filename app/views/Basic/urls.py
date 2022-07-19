from django.urls import path
from app.views.Basic import view

urlpatterns = [
    path('create_basic', view.create_basic, name='create_basic'),
    path('edit_basic/<int:basic_id>', view.edit_basic, name='edit_basic'),
    path('list_basic', view.list_basic, name='list_basic'),
    path('basic_details/<int:basic_id>', view.basic_details, name='basic_details')

]
