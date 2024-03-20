from django.urls import path, include
from . import views

app_name = 'blog' #app ka naam specify karne se better rahega else agar do apps hote in same urls.py toh django first app ko le leta

urlpatterns = [
    path('',views.all_blogs, name = 'all_blogs' ),
    path('<int:blog_id>/',views.detail, name = 'detail' ),
]