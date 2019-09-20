from django.urls import path
from . import views

app_name = 'eithers'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:question_pk>/', views.detail, name='detail'),
    path('<int:question_pk>/comments_create/', views.comments_create, name='comments_create'),
    path('<int:answer_pk>/<int:question_pk>/comments_delete/', views.comments_delete, name='comments_delete'),

]