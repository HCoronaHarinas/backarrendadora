from config.wsgi import *

from core.erp.models import Type

#Listado

# query = Type.objects.all()
# print(query)
# #
# # #Insercion
#
# t = Type(name='juan').save()
#
# print(t)
# #edicion

# t = Type()
# t.name = 'Accioniustra'
# t.save()
#

# t = Type.objects.get(pk=1)
# t.name = 'Ex-accionista'
# t.save()

#ELIMINACION
# t = Type.objects.get(id=1)
# t.delete()


# obj = Type.objects.all().order_by('id')
# print(obj)

# t = Type()
# t.name = 'Ingeniero'
# t.save()
# t= Type.objects.all()
#
# print(t)



obj = Type.objects.all().count()

print(obj)




