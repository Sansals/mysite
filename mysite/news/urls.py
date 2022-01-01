from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create/', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),#отслеживание динамического параметра
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),#обновление записей БД
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),#удаление записей
]