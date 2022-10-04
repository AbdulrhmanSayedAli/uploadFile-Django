from django.urls import path
from .views import Image

urlpatterns = [
    path('upload/', Image.as_view()),
]
