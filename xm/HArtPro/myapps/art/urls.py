from django.conf.urls import url, include

from art import views


urlpatterns = [
    url(r'^show/(\d+?)/', views.show),
]


