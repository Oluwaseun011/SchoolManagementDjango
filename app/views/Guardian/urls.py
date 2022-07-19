from django.urls import path
from app.views.Guardian import view

urlpatterns = [
    path('edit_guardian/<int:guardian_id>', view.edit_guardian, name='edit_guardian'),
    path('list_guardian', view.list_guardians, name='list_guardians'),
    path('guardian_details/<int:guardian_id>', view.guardian_details, name='guardian_details'),

]