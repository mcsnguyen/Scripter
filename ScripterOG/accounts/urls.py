from django.urls import path
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('about_us/', views.about_us, name='about_us'),
path('document/', views.view_document, name='view_document'),

    path('password_reset/', PasswordResetView.as_view(
            template_name='accounts/reset_password.html',
            success_url='done/',
            email_template_name='accounts/reset_password_email.html'),
         name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(
            template_name='accounts/reset_password_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
            template_name='accounts/reset_password_confirm.html',
            success_url='/'),
         name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(
            template_name='accounts/reset_password_complete.html'),
        name='password_reset_complete')

]
'''
    path('password_reset/', PasswordResetView.as_view(template_name='accounts/reset_password.html'),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
    '''