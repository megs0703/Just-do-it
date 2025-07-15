from django.urls import path # type: ignore
from insta_grocery import views 
urlpatterns = [
    path("", views.home, name="home")
]