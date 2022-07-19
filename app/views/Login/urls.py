from django.urls import path
from app.views.Login import view

urlpatterns = [
    path('login_get', view.login_get, name='login_get'),
    path("login_post", view.login_post, name="login_post"),
    path('', view.log_out, name='logout')
]