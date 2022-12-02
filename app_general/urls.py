from django.urls import path
from . import views
# MAP LIST URL 
# path('',views.nameView,name=stringName)
urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
]