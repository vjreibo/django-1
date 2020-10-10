from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.index, name="index"),
    path('topics/', views.topics, name="topics"),
    path('topic/<int:topic_id>/', views.topic, name="topic"),
    path('new_topic/', views.new_topic, name="new_topic"),
    path('topic/<int:topic_id>/new_entry', views.new_entry, name="new_entry"),
    path('edit_entry/<int:entry_id>', views.edit_entry, name="edit_entry"),
]