from django.http import HttpRequest, request

from config.wsgi import *
from django.template.loader import get_template
from weasyprint import HTML, CSS
from config import settings
from core.arrendadora.models import Register


def printTicket():
    start_date = '2022-03-30'
    end_date= '2022-05-31'
    template = get_template("ticket.html")
    context = {
        "name":"Hector Hugo Corona Garcia",
        "object_list": Register.objects.filter(date_update__range=[start_date, end_date], owner_id=1,)
    }
    html_template = template.render(context)
    css_url = os.path.join(settings.BASE_DIR,'static/css/pdf.css')
    HTML(string=html_template).write_pdf(target="ticket.pdf",stylesheets=[CSS(css_url)])

def printTicketTotal():
    start_date = '2022-01-31'
    end_date= '2022-06-16'
    template = get_template("all.html")
    prueba = Register.objects.filter(date_update__range=[start_date, end_date])
    print(prueba.count())
    context = {
        "name":"Hector Hugo Corona Garcia",
        "object_list": Register.objects.filter(date_update__range=[start_date, end_date])
    }
    html_template = template.render(context)
    css_url = os.path.join(settings.BASE_DIR,'static/css/pdf.css')
    HTML(string=html_template).write_pdf(target="all.pdf",stylesheets=[CSS(css_url)])


printTicketTotal()

printTicket()



