from django.urls import path
from app.views.Student import view

urlpatterns = [
    path('edit_student/<int:student_id>', view.edit_student, name='edit_student'),
    path('student_details/<int:student_id>', view.student_details, name='student_details'),
    path('list_student', view.list_students, name='list_students'),
    path("complets_application", view.register_student, name="register_student")
]