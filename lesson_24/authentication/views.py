from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Users
from .auth_functions import hide_mail


class Main_sait(View):
    user_list = Users.objects.all()

    def get(self, request):
        user_count = len(self.user_list)
        private_mail = hide_mail()
        return render(request, 'main.html', context={"count": user_count, "user": private_mail})


class Sign_up(View):
    def get(self, request):
        return render(request, 'sign_up.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        for user in Users.objects.all():
            if user.user_email == email:
                return render(request, 'sign_up.html',
                              {'error_message': 'User already exists!'})
        if repeat_password != password:
            return render(request, 'sign_up.html',
                          {'error_message': 'repeat password and password are different!'})
        else:
            if password == repeat_password:
                user = Users(user_email=email, user_password=password)
                user.save()
                return render(request, 'sign_up.html', {'error_message': 'User successful'
                                                                         ' created!'})


class Sing_in(View):

    message = None
    user_found = False

    def get(self, request):
        return render(request, 'sign_in.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        for user in Users.objects.all():
            if user.user_email == email and user.user_password == password:
                self.message = 'Success!'
                return render(request, 'sign_in.html', {'message': self.message})
            if not self.user_found:
                self.message = 'Invalid email or password!'
        return render(request, 'sign_in.html', {'message': self.message})

