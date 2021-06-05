from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('articles/page/<int:page_num>/', views.get_article_list, name='article_list'),
    path('article/<int:article_id>/', views.get_article, name='get_article'),
    path('article/compose/', views.compose_article, name='compose_article'),
    path('article/edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('article/delete/<int:article_id>/', views.delete_article, name='delete_article'),
    path('article/send/<int:article_id>/', views.send_article, name='send_article'),
]
