from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", home, name="home"),
    path("admin-view/", admin_view, name="admin_view"),
    path("why/", why_view, name="why"),
    path("final/", final_view, name="final"),
    path("user/", user_view, name="user_view"),
    

]


