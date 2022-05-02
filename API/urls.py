from django.urls import path
from . import views


urlpatterns = [
    path('', views.apilinks, name="apilinks"),
    path('todo-list/', views.TodoList, name="Todo-list"),
    path('todo-details/<str:pk>/',views.TodoDetail, name="Todo-Details"),
    path('todo-update/<str:pk>/',views.TodoUpdate, name="Todo-Update" ),
    path('todo-create/', views.TodoCreate, name="Todo-Create"),
    path('todo-delete/<str:pk>/', views.TodoDelete, name="Todo-Delete")
  ]