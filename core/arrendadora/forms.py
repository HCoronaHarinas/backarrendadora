from django.forms import ModelForm

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
            'desc': 'Descripcion',
            'desc': 'Descripcion',
            'desc': 'Descripcion'
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

