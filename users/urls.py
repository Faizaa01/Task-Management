from users.views import *
from django.urls import path  
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('sign-in/', CustomLoginView.as_view(), name='sign_in'),
    path('sign-out/', LogoutView.as_view(), name='sign_out'),
    # path('sign_in/', sign_in, name='sign_in'), 
    # path('sign_out/', sign_out, name='sign_out'),
    path('activate/<int:user_id>/<str:token>/', activate_user),

    path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('admin/<int:user_id>/assign-role/', assign_role, name='assign-role'),
    path('admin/create-group/', create_group, name='create-group'),
    path('admin/group-list/', group_list, name='group-list'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),

    path('password-change/', ChangePassword.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/confirm/<uidb64>/<token>/',CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
