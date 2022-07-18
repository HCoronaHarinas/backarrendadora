from django.template.loader import get_template
from django.urls import reverse_lazy

from config.wsgi import *
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, TemplateView
from weasyprint import HTML, CSS

from config import settings
from core.arrendadora.models import Register, Unidad
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
                    search = Register.objects.filter(date_update__range=[start_date, end_date],
                                                     owner_id=self.kwargs.get('pk'), )
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


class ReportPdf(TemplateView):

    def post(self, request, *args, **kwargs):
        print(request.POST)  # de esta forma se ven los datos que se envían en el formulario de HTML
        return super(self.__class__, request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            start_date = '2022-01-31'
            end_date = '2022-06-16'
            template = get_template('ticket.html')
            context = {
                "name": "Hector Hugo Corona Garcia",
                "object_list": Register.objects.filter(date_update__range=[start_date, end_date], owner_id=1, )
            }
            html = template.render(context)
            css_url = os.path.join(settings.BASE_DIR, 'static/css/pdf.css')
            pdf = HTML(string=html).write_pdf(stylesheets=[CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('reports:report_list'))
