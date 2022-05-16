from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView

from core.arrendadora.forms import *
from core.arrendadora.models import *


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

class RegisterListView(ListView):
    model = Register
    template_name = 'registro/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {

        }
        try:
            data = Register.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tabla de amortización'
        context['unidad'] = Unidad.objects.all()
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
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_data':
                pass
            else:
                data['error']= 'ah ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

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
        context['title'] = 'Registro de Cargos/  s'
        context['resultado'] = Register.objects.all()
        return context


