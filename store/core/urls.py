from django.urls import path
from django.contrib.auth import views as auth_view
from core.views import index, register_user, categoryList


urlpatterns = [
    path('', index, name='index'),

    path('accounts/login/', auth_view.LoginView.as_view(
        template_name='core/registration/login.html'), name='login'),

    path('accounts/logout/', auth_view.LogoutView.as_view(
        template_name='core/registration/logged_out.html'), name='logout'),

    path('accounts/password_reset/', auth_view.PasswordResetView.as_view(
        template_name="core/registration/password_reset_form.html"), name='password_reset'),

    path('accounts/password_reset_done/', auth_view.PasswordResetDoneView.as_view(
        template_name='core/registration/password_reset_done.html'), name='password_reset_done'),

    path('accounts/password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='core/registration/password_reset_confirm.html'), name='password_reset_confirm'),

    path('accounts/password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='core/registration/password_reset_complete.html'), name='password_reset_complete'),

    path('accounts/register_user/', register_user, name='register_user'),



    path('<path:path>', categoryList, name='categoryList'),
]
