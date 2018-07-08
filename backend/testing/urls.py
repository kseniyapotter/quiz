from django.urls import path
from .api import views


urlpatterns = [
    # ex: /tests/
    path('tests', views.testList), 
    # ex: /5/
    path('<int:test_id>/', views.test),
    # ex: /result/2/
    path('result/<int:test_id>/', views.result),
]