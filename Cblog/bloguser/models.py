from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.


class BlogUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, *args, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            password = password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class BlogUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]

    objects = BlogUserManager()

    

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin or super().has_perm(perm, obj)


class RegularBlogUser(BlogUser):
    """Regular user with limited permissions: can create and edit own posts."""

    class Meta:
        proxy = True
        permissions = [
            ("can_create_posts","Can create blog posts"),
            ("can_edit_own_post", "Can edit own blog posts"),
            ("can_delete_own_post", "Can delete own blog posts")
        ]

    def save(self, *args, **kwargs):
        self.is_staff = False
        self.is_admin = False
        super().save(*args, **kwargs)

    def assign_regular_permissions(self):
        """Assign regular user permissions: create and edit own posts."""
        from django.contrib.auth.models import Permission
        from django.contrib.contenttypes.models import ContentType
        from blog.models import BlogPost
        ct = ContentType.objects.get_for_model(BlogPost)

        # Assign custom permissions
        perms_to_add = [
            Permission.objects.get(content_type=ct, codename='add_blogpost'),
            Permission.objects.get(
                content_type=ct, codename='change_blogpost'),
        ]

        # Try to get custom permissions if they exist
        try:
            perms_to_add.append(
                Permission.objects.get(codename='can_create_post')
            )
            perms_to_add.append(
                Permission.objects.get(codename='can_edit_own_post')
            )
        except Permission.DoesNotExist:
            pass

        self.user_permissions.set(perms_to_add)


class AdminBlogUser(BlogUser):
    """Admin user with full permissions: can manage users and all blog posts."""

    class Meta:
        proxy = True
        permissions = [
            ("can_edit_any_post", "Can edit any blog post"),
            ("can_delete_any_post", "Can delete any blog post"),
            ("can_manage_users", "Can manage user accounts"),
            ("can_make_announcements","Can make announcements"),
            ("can_edit_announcemnts","Can edit announcements"),
            ("can_delete_announcements","Can delete announcements"),
        ]

    def save(self, *args, **kwargs):
        self.is_staff = True
        self.is_admin = True
        self.is_superuser = True
        super().save(*args, **kwargs)

    def assign_admin_permissions(self):
        """Assign admin user permissions: full control over all content."""
        from django.contrib.auth.models import Permission

        # Get all permissions
        all_perms = Permission.objects.all()
        self.user_permissions.set(all_perms)
        
    def assign_extra_permissions(self):
        """Assign regular user permissions: create and edit own posts."""
        from django.contrib.auth.models import Permission
        from django.contrib.contenttypes.models import ContentType
        from blog.models import Announcement,BlogPost
        ct = ContentType.objects.get_for_model(Announcement)

        # Assign custom permissions
        perms_to_add = [
            Permission.objects.get(content_type=ct, codename='add_announcement'),
            Permission.objects.get(
                content_type=ct, codename='change_announcement'),
        ]

        # Try to get custom permissions if they exist
        try:
            perms_to_add.append(
                Permission.objects.get(codename='can_create_announcement`')
            )
            perms_to_add.append(
                Permission.objects.get(codename='can_edit_own_announcement`')
            )
        except Permission.DoesNotExist:
            pass

        self.user_permissions.set(perms_to_add)