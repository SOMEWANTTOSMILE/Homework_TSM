from django.shortcuts import render, redirect
from django.views import View
from .models import News
from .forms import RegisterForm
from django.db.models import Q
from django.contrib.auth import get_user_model, login


User = get_user_model()


class MainNews(View):
    list_news = News.objects.values()

    def get(self, request):
        return render(request, "Main.html", {'news': self.list_news})


class SortedView(View):
    news = News.objects.values()

    def get(self, request):
        sorting_param = request.GET["name_sorting"]
        priority_sorting = request.GET["priority_sorting"]
        news = News.objects.order_by(f'{priority_sorting}{sorting_param}')
        return render(request, "Main.html", {'news': news})


class Signup(View):
    def get(self, request):
        form = RegisterForm
        return render(request, 'signup.html', context=({'form': form}))

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            user = User.objects.filter(Q(email=email))

        if not user and password == confirm_password:
            users = User.objects.create_user(email=email, username=username, password=password)
            users.save()
            massage = f'User successful created'

        if user:
            massage = f'This user was created '

        if password != confirm_password:
            massage = f'Invalid password'

        return render(request, 'signup.html', context={'form': form, 'massage': massage})


class SignIn(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            u_pass = user.check_password(password)

            if user and u_pass:
                login(request, user)
                return redirect('main')
            else:
                messages = f'Invalid password'
        except User.DoesNotExist:
            messages = f'A user with this email address was not found'

        return render(request, 'signin.html', context={'message': messages})
