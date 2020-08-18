from django.urls import path
from . import views


app_name = 'tests'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:test_id>/', views.detail, name='detail'),
]

'''
urlpatterns = [
    # ex: /tests/
    path('', views.index, name='index'),
    # ex: /tests/5/
    path('<int:test_id>/', views.detail, name='detail'),
]
'''
