from django.urls import path

from core.erp.views.category.views import *

app_name = 'erp'


urlpatterns = [
    path('categoria/list/', CategoryListView.as_view(), name='category_list'),
    path('categoria/add/', CategoryCreateView.as_view(), name='category_create'),
    path('categoria/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('categoria/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('categoria/form/', CategoryFormView.as_view(), name='category_form'),
]