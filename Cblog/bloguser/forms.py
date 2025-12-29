from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordResetForm,
    PasswordChangeForm,
)
from .models import RegularBlogUser


class BlogUserRegistrationForm(UserCreationForm):
    """Registration form that extends Django's built-in UserCreationForm
    and adds the extra fields from `BlogUser` plus simple Tailwind styling."""

    class Meta:
        model = RegularBlogUser
        fields = ("username", "email", "first_name",
                  "last_name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        input_classes = (
            "w-full px-4 py-2 border border-gray-300 rounded-md bg-white "
            "text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        )

        for name, field in self.fields.items():
            field.label_suffix = ""
            if hasattr(field.widget, "attrs"):
                field.widget.attrs.update({"class": input_classes})
                field.widget.attrs.setdefault(
                    "placeholder", name.replace("_", " ").title())

    def save(self, commit=True):
        user = super().save(commit=False)
        # copy additional fields onto the user instance
        user.email = self.cleaned_data.get("email", "")
        user.first_name = self.cleaned_data.get("first_name", "")
        user.last_name = self.cleaned_data.get("last_name", "")
        if commit:
            user.save()
        return user


class BlogUserAuthenticationForm(AuthenticationForm):
    model = RegularBlogUser
    fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        input_classes = (
            "w-full px-4 py-2 border border-gray-300 rounded-md bg-white "
            "text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        )
        label_classes = "block text-sm font-medium text-gray-700 mb-1"

        # update widget attributes
        if 'username' in self.fields:
            self.fields['username'].widget.attrs.update({
                'class': input_classes,
                'placeholder': 'Username',
                'autocomplete': 'username',
            })
            self.fields['username'].label = 'Username'

        if 'password' in self.fields:
            self.fields['password'].widget.attrs.update({
                'class': input_classes,
                'placeholder': 'Password',
                'autocomplete': 'current-password',
            })
            self.fields['password'].label = 'Password'


class BlogUserPasswordChangeForm(PasswordChangeForm):
    """PasswordChangeForm that adds Tailwind classes to widgets."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        input_classes = (
            "w-full px-4 py-2 border border-gray-300 rounded-md bg-white "
            "text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        )

        if 'old_password' in self.fields:
            self.fields['old_password'].widget.attrs.update({
                'class': input_classes,
                'placeholder': 'Current password',
                'autocomplete': 'current-password',
            })
            self.fields['old_password'].label = 'Current password'

        if 'new_password1' in self.fields:
            self.fields['new_password1'].widget.attrs.update({
                'class': input_classes,
                'placeholder': 'New password',
                'autocomplete': 'new-password',
            })
            self.fields['new_password1'].label = 'New password'

        if 'new_password2' in self.fields:
            self.fields['new_password2'].widget.attrs.update({
                'class': input_classes,
                'placeholder': 'Confirm new password',
                'autocomplete': 'new-password',
            })
            self.fields['new_password2'].label = 'Confirm new password'


class PublicPasswordChangeForm(forms.Form):
    """Public password change form for users without authentication.
    Requires username and new password only."""

    username = forms.CharField(
        max_length=150,
        required=True,
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md bg-white text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Your username',
            'autocomplete': 'username',
        })
    )
    new_password = forms.CharField(
        required=True,
        label="New Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md bg-white text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Enter new password',
            'autocomplete': 'new-password',
        })
    )
    confirm_password = forms.CharField(
        required=True,
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md bg-white text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Confirm new password',
            'autocomplete': 'new-password',
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        username = cleaned_data.get('username')

        # Verify username exists
        if username and not BlogUser.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Username not found. Please check and try again."
            )

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError(
                "Passwords do not match. Please try again."
            )
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
