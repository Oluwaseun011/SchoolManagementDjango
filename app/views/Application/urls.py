from django.urls import path
from app.views.Application import view

urlpatterns = [
    path('create_application', view.create_application, name='create_application'),
    path('pre_application', view.pre_application, name='pre_application'),
    path('application_slip/<str:email>', view.application_slip, name='application_slip'),
    # path('list_application', view.list_applications, name='list_application'),
    # path('list_pending', view.list_pending_applications, name='list_pending'),
    # path('approve_application/<int:id>/<int:application_id>', view.approve_application, name='approve_application')
]
