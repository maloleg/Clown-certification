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
    path('Alexander_Volkov', views.Alexander_Volkov),
    path('Akhmed_Khakhaev', views.Akhmed_Khakhaev),
    path('Alexey_Ischenko', views.Alexey_Ischenko),
    path('Kirill_Shvetsov', views.Kirill_Shvetsov),
    path('Vova_Bukin', views.Vova_Bukin),
    path('Daniil_Dobrin', views.Daniil_Dobrin),
    path('Danil_Kadochnikov', views.Danil_Kadochnikov),
    path('Maks_Agafonov', views.Maks_Agafonov),
    path('Rodion_Fedotov', views.Rodion_Fedotov),

    path('..', views.index),
]
