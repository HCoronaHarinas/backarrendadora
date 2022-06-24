from django.urls import path

from core.reports.views import *

app_name = 'reports'


urlpatterns = [
    path('account/<int:pk>/', ReportAccount.as_view(), name='report_list'),
]