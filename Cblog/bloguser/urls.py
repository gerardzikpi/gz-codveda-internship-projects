from django.urls import path
from . import views

app_name = "bloguser"

urlpatterns = [
    path("login/", views.BlogUserLoginView.as_view(), name="login"),
    path("logout/", views.BlogUserLogoutView.as_view(), name="logout"),
    path("register/", views.BlogUserRegistrationView.as_view(), name="register"),
    path("profile/<int:pk>/", views.BlogUserProfileView.as_view(), name="profile"),
    path("profile/edit/", views.BlogUserUpdateView.as_view(), name="edit_profile"),
    path("password/change/", views.PublicPasswordChangeView.as_view(),
         name="password_change"),
    path("password/reset/", views.BlogUserPasswordResetView.as_view(),
         name="reset_password"),
    path("password/reset/done",views.BlogUserPasswordResetDoneView.as_view(),name="reset_password_done"), 
    path("password/reset/confirm/<uidb64>/<token>/", views.BlogUserPasswordResetDoneView.as_view(),
         name="reset_password_confirm"), 
    path("password/reset/complete/",views.BlogUserPasswordResetCompleteView.as_view(),name="reset_password_complete"), 
]
