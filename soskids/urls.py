from django.urls import path
from . import views

# URLConf Module (URL Configurations) Rememner to import into main config ventureinsight_prj/urls.py
urlpatterns = [
    path('', views.home),
    path('signup/', views.signup),
    path('login/', views.login),
    path('profile/', views.profile),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout),
    path('lesson/', views.lesson),
    path('quiz/', views.quiz)
]
