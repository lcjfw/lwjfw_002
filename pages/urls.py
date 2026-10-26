from django.urls import path
from . import views
app_name='pages'
urlpatterns=[path('',views.cla,name='cla'),path('cla/',views.cla),path('index.html',views.cla),path('personal.html',views.cla),path('courses/',views.courses,name='courses'),path('courses.html',views.courses),path('focus/',views.focus,name='focus'),path('focus.html',views.focus),path('api/schedule/',views.api,name='api')]
