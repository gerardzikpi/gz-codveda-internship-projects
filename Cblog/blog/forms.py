from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from bloguser.models import RegularBlogUser
from .models import BlogPost,Announcement


class BlogPostCreationForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'status',]  
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full m-2 px-4 py-2 border border-gray-300 rounded-md bg-white text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter post title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full m-2 px-4 py-2 border border-gray-300 rounded-md bg-white text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Write your blog post content here...',
                'rows': 8,
            }),
            'status': forms.Select(attrs={
                'class': 'w-full m-2 px-4 py-2 border border-gray-300 rounded-md bg-white text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            # 'written_by': forms.Select(attrs={
            #     'class': 'w-full m-2 px-4 py-2 border border-gray-300 rounded-md bg-white text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
            # }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label_classes = "block text-sm font-medium text-gray-700 mb-2"

        for field_name, field in self.fields.items():
            field.label_suffix = ''
            if hasattr(field.widget, 'attrs'):
                # Add label styling
                self.fields[field_name].widget.attrs.update({
                    'data-form-field': field_name
                })

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class AnnouncementModelForm(ModelForm):
    model = Announcement
    fields = ["title","content"]
    widgets = {
        "title":forms.TextInput({
            "class":"w-full m-2 px-4 py-2 border border-gray-300 rounded-md bg-white text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder":"Type title here..."
        }),
        "content":forms.TextInput({
            "class":"w-full m-2 px-4 py-2 border border-gray-300 rounded-md bg-white text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder":"Type content here..."
        })
    }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)