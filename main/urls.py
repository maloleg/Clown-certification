from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('Stepan_Bazrov', views.Stepan_Bazrov),
    path('Nikita_Kinelovsky', views.Nikita_Kinelovsky),
    path('Alexander_Petrov', views.Alexander_Petrov),
    path('Oleg_Malyshev', views.Oleg_Malyshev),
    path('Rodion_Pronin', views.Rodion_Pronin),
    path('..', views.index),
]
