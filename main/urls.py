from django.urls import path
from .views import index,shorten,redirect_hash,detail

urlpatterns = [
    path('', index, name='index'),
    path('shorten/', shorten, name='shorten_post'),
    path('shorten/<int:pk>',detail,name='shortendetail'),
    path('h/<str:url_hash>/', redirect_hash, name='redirect'),
]