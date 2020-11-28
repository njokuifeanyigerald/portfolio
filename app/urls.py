from django.urls import path
from .views import index,reach,work,about

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact', reach, name='reach'),
    path('work', work, name='work'),
]
