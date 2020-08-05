from django.urls import path, re_path

from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.PublicationDetailView.as_view(), name='publication-detail'),
]
