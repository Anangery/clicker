from django.urls import path
from clickersite import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path("time/<speaker>", views.time, name="time"),
]
urlpatterns += staticfiles_urlpatterns()