from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import AppLoginFrom, AppChangePassForm, MyPasswordResetForm, AppPassResetConfirmForm

# Create your views here.
# def index(request):
#     return render(request, 'account/home.html'

class MyLoginView(LoginView):
    template_name = 'account/home.html'
    authentication_form = AppLoginFrom

class MyLogoutView(LogoutView):
    template_name = 'account/logout.html'


class MyPasswordChangeView(PasswordChangeView):
    form_class = AppChangePassForm
    template_name = 'account/passwordChange.html'
    success_url = '/changePassDone/'


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'


class MySetPasswordView(PasswordResetView):
    form_class = MyPasswordResetForm
    template_name = 'account/set_password.html'

class MySetPasswordDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class MySetPasswordResetConView(PasswordResetConfirmView):
    form_class = AppPassResetConfirmForm
    template_name = 'account/password_reset_confirm.html'

class MySetPassComplete(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'
    
