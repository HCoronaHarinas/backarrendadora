from django.urls import path

from core.reports.views import *

app_name = 'reports'


urlpatterns = [
    path('account/<int:pk>/', ReportAccount.as_view(), name='report_list'),
    path('pdf/', ReportPdf.as_view(), name='report_pdf'),
]