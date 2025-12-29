from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BlogUser,AdminBlogUser,RegularBlogUser

# Register your models here.


class BlogUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name",
                    "last_name", "is_admin", "is_staff")
    search_fields = ("email", "username", "first_name", "last_name")
    readonly_fields = ("id", "date_joined")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(BlogUser, BlogUserAdmin)
admin.site.register(AdminBlogUser)
admin.site.register(RegularBlogUser)