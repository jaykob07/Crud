from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('eliminar/editar/<int:id>', views.editar, name='editar'),
    path('libros/crear/<int:id>/', views.detalle_pdf, name='detalle_pdf'),
    # path('', views.empecemos, name='empecemos'),
    
]