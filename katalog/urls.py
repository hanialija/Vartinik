from django.urls import path
from katalog import views

urlpatterns = [
    # profesoret/
   path('katalog/', views.katalog),
   path('', views.katalog),
   path('regjistro', views.regjistro , name='regjistro'),
   path('fshi/<int:id>/', views.fshi , name='fshi'),
   path('edit/<int:id>/', views.edit , name='edit')
  
]