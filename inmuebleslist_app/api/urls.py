from django.urls import path
from inmuebleslist_app.api.views import EdificacionesListAV,EdificacionDetalleAV,EmpresaAV

urlpatterns = [
    path('list/',EdificacionesListAV.as_view(),name='edificaciones-list'),
    path('<int:pk>',EdificacionDetalleAV.as_view(),name='edificacion-detalle'),
    
    path('empresas/',EmpresaAV.as_view(),name='empresa-list'),
]
