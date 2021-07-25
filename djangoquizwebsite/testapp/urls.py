from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage, name='home'),
    path('quiz/',views.pythonquizpage, name='pythonquiz'),
    path('login/',views.loginuser, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logoutuser, name='logout'),
    path('addQues/', views.addQues,name='addQues'),
    path('scores/', views.viewScores,name='scores'),
]
