from django.urls import path

from core.arrendadora.views import *

app_name = 'arrendadora'


urlpatterns = [
    path('owner/list/', OwnerListView.as_view(), name='propietario_lista'),
    path('owner/add/', OwnerCreateView.as_view(), name='propietario_crear'),
    path('owner/edit/<int:pk>/', OwnerUpdateView.as_view(), name='propietario_edit'),
    path('owner/delete/<int:pk>/', OwnerDeleteView.as_view(), name='propietario_delete'),
    path('unidad/list/', UnidadListView.as_view(), name='unidad_list'),
    path('unidad/add/', UnidadCreateView.as_view(), name='unidad_create'),
    path('unidad/edit/<int:pk>/', UnidadUpdateView.as_view(), name='unidad_edit'),
    path('unidad/delete/<int:pk>/', UnidadDeleteView.as_view(), name='unidad_delete'),
    path('conceptos/list/', ConceptosListView.as_view(), name='conceptos_list'),
    path('conceptos/add/', ConceptosCreateView.as_view(), name='conceptos_add'),
    path('conceptos/edit/<int:pk>/', ConceptosUpdateView.as_view(), name='conceptos_edit'),
    path('conceptos/delete/<int:pk>/', ConceptosDeleteView.as_view(), name='conceptos_delete'),
    # Registro de Cargos y Abonos
    path('registro/list/', RegisterListView.as_view(), name='registro_list'),
    path('registro/add/', RegisterCreateView.as_view(), name='registro_add'),
    path('registro/detail/<int:pk>/',EstadoCuenta.as_view() , name='estado_cuenta'),
    #Factura
    path('test/', TestView.as_view(), name='test'),
    path('unidad/view/<int:pk>/', Factura.as_view(), name='factura'),
    path('unidad/pdf/<int:pk>/', FacturaPdfView.as_view(), name='factura_pdf'),
  #  path('unidad/usuario/<int:pk>/', filtrado_list, name='unidad filtrado'),

]