from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create-view/', views.create_view),
    path('list-view/', views.list_view),
    path('<id>', views.detail_view),
    path('update-view/<id>/', views.update_view),
    path('<id>/delete/', views.delete_view),


]
