from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jira_query/', views.jira_query, name='jira_query'),
]
