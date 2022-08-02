from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('about/', about),
    path('contact/', contact),
    path('index-2', index2),
    path('blog-single/<slug:slug>/', blog_single),

]
