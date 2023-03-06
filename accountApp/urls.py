from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', views.MyLoginView.as_view(), name="login"),
    path('portal/', login_required(TemplateView.as_view(template_name='account/portal.html')), name="portal"),
    path('logout/', login_required(views.MyLogoutView.as_view()), name="logout"),
    path('changePass/', login_required(views.MyPasswordChangeView.as_view()), name="changePass"),
    path('changePassDone/', login_required(views.MyPasswordChangeDoneView.as_view()), name="password_change_done"),
    path('password_reset/', views.MySetPasswordView.as_view(), name="password_reset"),
    path('password_reset/done/', views.MySetPasswordDoneView.as_view(), name="password_reset_done"),
    path('password_reset_complete/', views.MySetPassComplete.as_view(), name="password_reset_complete"),
    path("password_reset_confirm/<uidb64>/<token>/",views.MySetPasswordResetConView.as_view(),name="password_reset_confirm"),

]