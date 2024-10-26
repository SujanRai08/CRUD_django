from django.urls import path
from .views import Home,ProductDetail

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('<int:id>/',ProductDetail.as_view(),name='detail'),

]
