from django.test import TestCase

# Create your tests here.

import numpy_financial as npf
from config.wsgi import *

from core.arrendadora.models import *

# unidad = Unidad.objects.get(pk=1)
# monto_prestamo = unidad.valor
# saldo_in = monto_prestamo
# sobre_tasa = unidad.tasa / 100
# tiie = unidad.tiie/100
# tasa_mensual =( (sobre_tasa + tiie)/12)
# fecha = unidad.date_create.month
# intereses = 0
# capital = 0
# plazo = unidad.plazo

# valor total o factura
# pv = unidad.valor
# Tasa de interes
# interes = (sobre_tasa + tiie)
# pago_fijo = round(npf.pmt(interes/12, plazo, -unidad.valor),2)


# fecha = datetime.now()
# print(f"Fecha:{fecha.hour}:{fecha.minute}   {fecha.day}/{fecha.month}/{fecha.year}");
# print(fecha.strftime("%H:%M %d/%b/%Y"))
# print(pago_fijo)


# for item in range(0,plazo):
#  saldo_in = saldo_in - capital
# intereses = saldo_in * tasa_mensual
#  capital = pago_fijo - intereses
#  print(f"${saldo_in:,.2f}")

# print(f"${intereses:,.2f}")


#capital = 10

#saldo_in = capital

#abonos = 10
#cargos = 0

#Saldo_actualizado= saldo_in

#id = 5

#for item in range(0,id):
   # saldo_in = saldo_in + abonos - cargos
    #print(saldo_in)


#name = Owner.objects.get(pk=6)
#name.capital = 100
#name.save()

#print(name.capital)
owner = Owner.objects.get(id=1)
capital = owner.capital

cargos = Register.objects.filter(owner_id=1, tipo_id=1)
abonos = Register.objects.filter(owner_id=1, tipo_id=2)

car_total = 0
abn_total = 0

for e in cargos:
    car_total = car_total + e.importe

for e in abonos:
    abn_total = abn_total - e.importe

print(abn_total)
print(car_total)

capital = capital + abn_total + car_total

print(capital)



