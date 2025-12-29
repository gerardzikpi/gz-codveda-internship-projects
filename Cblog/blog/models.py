from django.db import models
from bloguser.models import AdminBlogUser,BlogUser

# Create your models here.
STATUS_CHOICES = [
    ("DRAFT", "Draft"),
    ("PUBLISHED", "Published")
]


class BlogPost(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    written_by = models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Announcement(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    author = models.ForeignKey(AdminBlogUser,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural ="Announcements"