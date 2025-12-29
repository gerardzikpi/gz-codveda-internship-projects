from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.views.generic import CreateView, DetailView, UpdateView, FormView, TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BlogUser
from .forms import BlogUserRegistrationForm,BlogUserAuthenticationForm,PublicPasswordChangeForm


class BlogUserRegistrationView(CreateView):
    model = BlogUser
    form_class = BlogUserRegistrationForm
    context_object_name = "user"
    template_name = "registration/registration.html"
    success_url = reverse_lazy("blog:posts")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data.get("password1"))
        user.save()
        login(self.request, user)
        messages.success(self.request, "Account created successfully.")
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("bloguser:profile", kwargs={"pk": self.request.user.pk})


class BlogUserLoginView(LoginView):
    form_class = BlogUserAuthenticationForm
    template_name = "registration/login.html"
    next_page = reverse_lazy("blog:posts")


class BlogUserLogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect("blog:posts")


class BlogUserProfileView(LoginRequiredMixin, DetailView):
    model = BlogUser
    template_name = "accounts/profile.html"
    context_object_name = "user"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"id": self.request.user.id})


class BlogUserUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogUser
    fields = ["username", "first_name", "last_name", "email"]
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user


class PublicPasswordChangeView(FormView):
    """Public password change view without authentication.
    Users only need to provide their username and new password."""

    form_class = PublicPasswordChangeForm
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("bloguser:login")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        new_password = form.cleaned_data.get("new_password")

        try:
            user = BlogUser.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(
                self.request,
                "Password changed successfully! You can now log in with your new password."
            )
        except BlogUser.DoesNotExist:
            form.add_error("username", "User not found.")
            return self.form_invalid(form)

        return super().form_valid(form)


class BlogUserPasswordResetView(PasswordResetView):
    template_name = "registration/passwordreset/password_reset.html"
    email_template_name = "registration/passwordreset/password_reset_email.html"
    subject_template_name = "registration/passwordreset/password_reset_subject.txt"
    from_email = "admin@codvedablog.com"

    def form_valid(self, form):
        send_mail(
            "Password Reset",
            f"{email_template_name}",
            DEFAULT_FROM_EMAIL,
            [form.instance.email]
        )
        # return super().form_valid(form)
INTERNAL_RESET_SESSION_TOKEN = "_password_reset_token"

class BlogUserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/passwordreset/userpassword_reset_done.html"

class BlogUserConfirmPasswordReset(PasswordResetConfirmView):
    template_name = "registration/passwordreset/password_reset_confirm.html"

   
class BlogUserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "registration/passwordreset/password_reset_complete.html"

