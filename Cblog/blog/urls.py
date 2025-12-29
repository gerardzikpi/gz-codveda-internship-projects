from django.urls import path, include
from . import views

app_name="blog"

urlpatterns = [
    path("", views.BlogPostListView.as_view(), name="posts"),
    path("announcements/",views.AnnouncementListView.as_view(), name="announcements"),
    path("detail/<int:pk>/", views.BlogPostDetailView.as_view(), name="detail"),
    path("create/", views.BlogPostCreateView.as_view(), name="create"),
    path("delete/<int:pk>/", views.BlogPostDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", views.BlogPostUpdateView.as_view(), name="update"),
]
