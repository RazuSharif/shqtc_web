from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('home/', views.index, name='home'),
    path('register/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('saveUser/', views.saveUser, name='saveUser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('index/',views.HomePage,name='index'),
    path('logout/',views.LogoutPage,name='logout'),
    path('userupdate/',views.userUpdate,name='userupdate'),
    path('updateinfo/',views.updatewon,name='updatewon'),
    path('updateeachuser/', views.updateeachuser, name='updateeachuser'),
    path('userupdateadmin/',views.userupdateadmin,name='userupdateadmin'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('saveproduct/',views.saveproduct,name='saveproduct'),
    path('productupdate/<int:item>',views.productupdate,name='productupdate'),
    path('viewproduct/<int:item>',views.viewproduct,name='viewproduct'),
    path('updateproduct/',views.updateproduct,name='updateproduct'),
    path('about/',views.about,name='about'),
    path('price/',views.price,name='price'),
    path('addnotice/',views.addnotice,name='addnotice'),
    path('savenotice/',views.savenotice,name='savenotice'),
    path('notice/',views.notice,name='notices'),
    path('services/',views.services,name='services'),
]