
from django.urls import path,include
from some_app import views


urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.sign_up,name="signup"),
    path('signin/',views.sign_in,name="signin"),
    path('signout/',views.sign_out,name="signout"),
    path('userbio/',views.user_bio,name="userbio"),
    path('upload/',views.upload,name="upload"),
]