from django.urls import path
from . import views	# from current directory import views

urlpatterns = [
    path('', views.home, name = 'lrc-home'),
    path('about/', views.about, name = 'lrc-about'),
    path('dashboard/', views.admin, name = 'lrc-admin'),
    path('unauthorized/', views.unauthorized_page, name = 'lrc-unauthorized'),
]
