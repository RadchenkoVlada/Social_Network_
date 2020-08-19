from django.urls import path
from .views import PostView


app_name = "app"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('app/', PostView.as_view()),
    path('posts/<int:pk>', PostView.as_view())
]
