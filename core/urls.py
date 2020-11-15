from django.urls import path
from . import views
app_name = 'core'


urlpatterns = [
    path('', views.MovieList.as_view(),name='MovieList'),
    path('movie/<int:pk>/', views.DetailMovie.as_view(), name='MovieDetail'),
]
