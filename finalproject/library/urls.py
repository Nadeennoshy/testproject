from django.urls import path
from library.views import index,login_view,register,admin,student,addbooks
urlpatterns = [ 
    path('',index,name="index"),
    path('login/',login_view,name="login_view"),
    path('register/',register,name="register"),  
    path('adminpage/',admin, name='adminpage'),
    path('student/',student, name='student'),
    path('addbooks/',addbooks,name='addbooks'),
]