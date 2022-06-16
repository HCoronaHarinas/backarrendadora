from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
import numpy_financial as npf
from core.arrendadora.forms import *
from core.arrendadora.models import *

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


# Create your views here.


class OwnerListView(ListView):
    model = Owner
    template_name = 'propietarios/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {

        }
        try:
            data = Owner.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Propietarios'
        return context


class OwnerCreateView(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'propietarios/create.html'
    success_url = reverse_lazy('arrendadora:propietario_lista')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevos propietarios'
        context['resultado'] = Owner.objects.all()
        return context


class OwnerUpdateView(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'propietarios/create.html'
    success_url = reverse_lazy('arrendadora:propietario_lista')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de propietarios'
        context['entity'] = 'Propietarios'
        context['list_url'] = reverse_lazy('arrendadora:propietario_lista')
        context['action'] = 'edit'
        return context


class OwnerDeleteView(DeleteView):
    model = Owner
    template_name = 'propietarios/delete.html'
    success_url = reverse_lazy('arrendadora:propietario_lista')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de propietarios'
        context['entity'] = 'Owners'
        context['list_url'] = reverse_lazy('arrendadora:propietario_lista')
        return context


# Views Unidades


class UnidadListView(ListView):
    model = Unidad
    template_name = 'unidades/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {

        }
        try:
            data = Unidad.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Unidades'
        return context


class UnidadCreateView(CreateView):
    model = Unidad
    form_class = UnidadForm
    template_name = 'unidades/create.html'
    success_url = reverse_lazy('arrendadora:unidad_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = UnidadForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Unidad'
        context['resultado'] = 'Activo'
        return context


class UnidadUpdateView(UpdateView):
    model = Unidad
    form_class = UnidadForm
    template_name = 'unidades/create.html'
    success_url = reverse_lazy('arrendadora:unidad_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Unidades'
        context['entity'] = 'Propietarios'
        context['list_url'] = reverse_lazy('arrendadora:unidad_list')
        context['action'] = 'edit'
        return context


class UnidadDeleteView(DeleteView):
    model = Unidad
    template_name = 'unidades/delete.html'
    success_url = reverse_lazy('arrendadora:unidad_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de unidades'
        context['entity'] = 'Owners'
        context['list_url'] = reverse_lazy('arrendadora:unidad_list')
        return context


# Views Conceptos


class ConceptosListView(ListView):
    model = Conceptos
    template_name = 'conceptos/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {

        }
        try:
            data = Owner.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Conceptos'
        return context


class ConceptosCreateView(CreateView):
    model = Conceptos
    form_class = ConceptosForm
    template_name = 'conceptos/create.html'
    success_url = reverse_lazy('arrendadora:conceptos_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = ConceptosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Unidad'
        context['resultado'] = 'Activo'
        return context


class ConceptosUpdateView(UpdateView):
    model = Conceptos
    form_class = ConceptosForm
    template_name = 'conceptos/create.html'
    success_url = reverse_lazy('arrendadora:conceptos_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Unidades'
        context['entity'] = 'Propietarios'
        context['list_url'] = reverse_lazy('arrendadora:conceptos_list')
        context['action'] = 'edit'
        return context


class ConceptosDeleteView(DeleteView):
    model = Conceptos
    template_name = 'conceptos/delete.html'
    success_url = reverse_lazy('arrendadora:conceptos_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de unidades'
        context['entity'] = 'Owners'
        context['list_url'] = reverse_lazy('arrendadora:conceptos_list')
        return context


class DatosEstadoCuenta:

    def __init__(self, fecha, concepto, importe, saldo,tipo):
        self.fecha = fecha
        self.concepto = concepto
        self.importe = importe
        self.saldo = saldo
        self.tipo = tipo

    def to_dict(self):
        data = {
            'fecha': self.fecha,
            'concepto': self.concepto,
            'importe': self.importe,
            'saldo': self.saldo,
            'tipo': self.tipo,
        }

        return data


class EstadoCuenta(DetailView):
    model = Register
    template_name = 'registro/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Estado de cuenta'
        context['list_url'] = reverse_lazy('arrendadora:propietario_lista')
        registro = Register.objects.filter(owner_id=self.kwargs.get('pk')).order_by('fecha')
        owner = Owner.objects.get(pk=self.kwargs.get('pk'))
        list_objetos = list()
        capital = owner.capital
        saldo_actual= capital
        for e in registro:
            if e.tipo_id == 1:
                saldo_actual = saldo_actual - e.importe
            else:
                saldo_actual = saldo_actual + e.importe
            dato_estado = DatosEstadoCuenta(fecha=e.fecha, concepto=e.concepto, importe=f"${e.importe:,.2f}", saldo=f"${saldo_actual:,.2f}", tipo = e.tipo_id)
            list_objetos.append(dato_estado)
        saldo_final = saldo_actual
        num_cargos = Register.objects.filter(owner_id=self.kwargs.get('pk'),tipo_id=1).count()
        num_abonos = Register.objects.filter(owner_id=self.kwargs.get('pk'),tipo_id=2).count()
        context['list_objetos'] = list_objetos
        context['owner'] = owner
        context['saldofin'] = f"${saldo_final:,.2f}"
        context['numabon'] =  num_abonos
        context['numcar'] =  num_cargos
        return context


class RegisterListView(ListView):
    model = Register
    template_name = 'registro/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Estado de cuenta'
        return context


class RegisterCreateView(CreateView):
    model = Register
    form_class = RegisterForm
    template_name = 'registro/create.html'
    success_url = reverse_lazy('arrendadora:registro_add')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Cargos'
        context['resultado'] = Register.objects.all()
        return context


class TestView(TemplateView):
    template_name = 'test.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_concepto_id':
                data = [{
                    'id': '',
                    'text': '--------------'
                }]
                for i in Conceptos.objects.filter(tipo_id=request.POST['id']):
                    data.append({
                        'id': i.id,
                        'text': i.name
                    })
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Aninados | Django'
        context['form'] = TestForm()
        return context


class DatosFactura:

    def __init__(self, mes, mes_num, pago_fijo, capital, intereses, saldo_in, tiie, dif, tasa, interes_real,
                 pago_mensual):
        self.mes = mes
        self.mes_num = mes_num
        self.pago_fijo = pago_fijo
        self.capital = capital
        self.intereses = intereses
        self.saldo_in = saldo_in
        self.tiie = tiie
        self.dif = dif
        self.tasa = tasa
        self.interes_real = interes_real
        self.pago_mensual = pago_mensual

    def to_dict(self):
        data = {
            'mes': self.mes,
            'mes_num': self.mes_num,
            'pago_fijo': self.pago_fijo,
            'capital': self.capital,
            'intereses': self.intereses,
            'saldo_in': self.saldo_in,
            'tiie': self.tiie,
            'dif': self.dif,
            'tasa': self.tasa,
            'interes_real': self.interes_real,
            'pago_mensual': self.pago_mensual,
        }

        return data


class Factura(DetailView):
    model = Unidad
    template_name = 'unidades/Factura.html'
    mont_list = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tabla de amortizacion'
        context['list_url'] = reverse_lazy('arrendadora:unidad_list')
        unidad = Unidad.objects.get(pk=self.kwargs.get('pk'))
        cont = 0
        list_objetos = list()

        # Nuevas variables

        monto_prestamo = unidad.valor
        saldo_in = monto_prestamo
        sobre_tasa = unidad.tasa / 100
        tiie = unidad.tiie / 100
        tasa_mensual = ((sobre_tasa + tiie) / 12)
        intereses = 0
        capital = 0
        plazo = unidad.plazo
        interes = (sobre_tasa + tiie)
        pago_fijo = round(npf.pmt(interes / 12, plazo, -unidad.valor), 2)

        for item in range(0, unidad.plazo + 1):
            saldo_in = saldo_in - capital
            dato_factura = DatosFactura(mes=unidad.date_create, mes_num=cont, pago_fijo=f"${pago_fijo:,.2f}",
                                        capital=f"${capital:,.2f}",
                                        intereses=f"${intereses:,.2f}", saldo_in=f"${saldo_in:,.2f}",
                                        tiie=f"%{unidad.tiie:,.2f}", dif=f"%{unidad.tasa:,.2f}",
                                        tasa=f"%{intereses:,.2f}",
                                        interes_real=0.02, pago_mensual=pago_fijo)
            list_objetos.append(dato_factura)
            intereses = saldo_in * tasa_mensual
            capital = pago_fijo - intereses
            cont = cont + 1
        context['list_objetos'] = list_objetos
        return context


class FacturaPdfView(View):

    def get(self, request, *args, **kwargs):
        unidad = Unidad.objects.get(pk=self.kwargs['pk'])
        cont = 0
        list_objetos = list()
        # Nuevas variables

        monto_prestamo = unidad.valor
        saldo_in = monto_prestamo
        sobre_tasa = unidad.tasa / 100
        tiie = unidad.tiie / 100
        tasa_mensual = ((sobre_tasa + tiie) / 12)
        intereses = 0
        capital = 0
        plazo = unidad.plazo
        interes = (sobre_tasa + tiie)
        pago_fijo = round(npf.pmt(interes / 12, plazo, -unidad.valor), 2)

        for item in range(0, unidad.plazo + 1):
            saldo_in = saldo_in - capital
            dato_factura = DatosFactura(mes=unidad.date_create, mes_num=cont, pago_fijo=f"${pago_fijo:,.2f}",
                                        capital=f"${capital:,.2f}",
                                        intereses=f"${intereses:,.2f}", saldo_in=f"${saldo_in:,.2f}",
                                        tiie=f"%{unidad.tiie:,.2f}", dif=f"%{unidad.tasa:,.2f}",
                                        tasa=f"%{intereses:,.2f}",
                                        interes_real=0.02, pago_mensual=pago_fijo)
            list_objetos.append(dato_factura)
            intereses = saldo_in * tasa_mensual
            capital = pago_fijo - intereses
            cont = cont + 1
            list_objetos = list_objetos

        try:
            template = get_template('unidades/prueba.html')
            context = {'object': unidad,
                       'list_objetos': list_objetos
                       }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            # if error then show some funny view
            if pisa_status.err:
                return HttpResponse('No se imprimio' + html + '</pre>')
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('arrendadora:unidad_list'))

