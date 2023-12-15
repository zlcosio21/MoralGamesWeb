from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog import views

urlpatterns = [

    path('', views.blog, name="blog"),

]

urlpatterns += staticfiles_urlpatterns()