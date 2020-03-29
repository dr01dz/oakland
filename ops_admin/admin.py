from django.contrib import admin
from .models import Order, Retailer, Supplier, Concession, ConcessionNote, SmallOrder

admin.site.register(Order)
admin.site.register(Retailer)
admin.site.register(Supplier)
admin.site.register(Concession)
admin.site.register(ConcessionNote)
admin.site.register(SmallOrder)
