from django.urls import path
from .views import MainNews, SortedView, Signup, SignIn


urlpatterns = [
    path('', MainNews.as_view(), name='main'),
    path('name_sorting/', SortedView.as_view()),
    path('signup/', Signup.as_view()),
    path('signin/', SignIn.as_view(), name='signin'),
]
