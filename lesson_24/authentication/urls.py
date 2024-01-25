from django.urls import path
from .views import Main_sait, Sign_up, Sing_in

urlpatterns = [
    path('', Main_sait.as_view()),
    path('sign_up/', Sign_up.as_view()),
    path('sign_in/', Sing_in.as_view())
]
