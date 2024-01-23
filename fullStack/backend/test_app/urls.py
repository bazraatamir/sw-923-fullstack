from django.urls import path
from . views import UserRegister,LoginView,CategoryView,ProductView,ProductImagesView

urlpatterns=[
    path("register",UserRegister.as_view() ),
    path("login",LoginView.as_view() ),
    path('category',CategoryView.as_view()),
    path('product',ProductView.as_view()),
    path('images',ProductImagesView.as_view())


]