from django.forms import *

from core.arrendadora.models import *


class OwnerForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
       # for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
         #   form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Owner
        fields = '__all__'
        labels = {
            'name': 'Nombre*',
            'state': 'Estado',
            'number': 'Numero Exterior*',
            'interior': 'Numero Interior'
        }


class UnidadForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
       # for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
         #   form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Unidad
        fields = '__all__'
        labels = {
            'name': 'Nombre*',
            'year':'Año'
        }


class ConceptosForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
       # for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
         #   form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Conceptos
        fields = '__all__'
        labels = {
            'name': 'Concepto',
        }


class RegisterForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # for form in self.visible_fields():
    #    form.field.widget.attrs['class'] = 'form-control'
    #   form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Register
        fields = '__all__'
        labels = {
            'name': 'Nombre*',
            'year': 'Año'
        }

class TestForm(Form):
    tipo = ModelChoiceField(queryset=Tipo.objects.all(), widget=Select(attrs={
        'class': 'form-control select2'
    }))

    concepto = ModelChoiceField(queryset=Conceptos.objects.none(), widget=Select(attrs={
        'class': 'form-control select2'
    }))
