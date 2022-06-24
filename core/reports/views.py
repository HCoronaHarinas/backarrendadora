from django.http import JsonResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from core.arrendadora.models import Register
from core.reports.forms import *


class ReportAccount(DetailView):
    template_name = 'report.html'
    model = Register

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                if start_date and end_date:
                    search = Register.objects.filter(date_update__range=[start_date, end_date],owner_id=self.kwargs.get('pk'),)
                    for s in search:
                        data.append([
                            s.fecha.strftime('%d-%m-%y'),
                            s.concepto.name,
                            s.referencia,
                            format(s.importe, '.2f'),
                            format(s.importe, '.2f'),

                        ])
            else:
                data['error'] = 'Ha ocurrido un error'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Estado de cuenta'
        context['form'] = ReportForm()

        return context
