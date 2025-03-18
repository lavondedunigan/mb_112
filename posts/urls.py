from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostListview.as_view(), name="List"),  
    path("<int:pk>/", views.PostDetailview.as_view(), name="detail"),  
    path("new/", views.PostCreateview.as_view(), name="new"),  
         
]