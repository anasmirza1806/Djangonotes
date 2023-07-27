from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('dubai/',views.dubai,name='dubai'),
    path('india/',views.india,name='india'),
    path('australia/',views.australia,name='australia'),
    path('america/',views.america,name='america'),


]

