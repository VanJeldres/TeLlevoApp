from django.contrib import admin
from .models import *
# Register your models here.


class CarreraAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_carrera','carrera']
        search_fields = ['id_carrera']

class EstadoAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_estado','estado'] 
        search_fields = ['id_estado']

class SedeAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_sede','sede']
        search_fields = ['id_sede']

class TipoPagoAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_tipo_pago','tipo_pago'] 
        search_fields = ['id_tipo_pago']

class PasajeroAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_pasajero','nombre','appaterno','apmaterno','rut','fech_nacimiento','correo','numero_celular','calificacion','password','id_sede','id_carrera'] 
        search_fields = ['id_pasajero']

class Clase_licenciaAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_clase_licencia','clase_licencia'] 
        search_fields = ['id_clase_licencia']

class ConductorAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_conductor','num_licencia','id_clase_licencia'] 
        search_fields = ['id_conductor']

class ColorAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_color','color'] 
        search_fields = ['id_color']

class VehiculoAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_vehiculo','modelo_vehiculo','patente','id_color'] 
        search_fields = ['id_vehiculo']

class ViajeAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_viaje','origen','destino','fech_viaje','hora_inicio','capacidad','precio','descripcion','id_conductor'] 
        search_fields = ['id_viaje']

class PagoAdmin(admin.ModelAdmin):
    class Meta:
 
        list_display=['id_pago','fech_pago','monto','id_viaje','id_pasajero','id_conductor'] 
        search_fields = ['id_pago']

class HistorialAdmin(admin.ModelAdmin):
    class Meta: 
        list_display=['id_historial','id_viaje','nombre','id_pasajero','id_conductor','monto','origen','destino','fech_viaje'] 
        search_fields = ['id_historial']

class Lobby_ViajeAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_lobby_viaje','id_viaje', 'id_pasajero']
        search_fields = ['id_viaje']

class MensajeAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_mensaje','mensaje', 'fech_mensaje','id_enviador','id_receptor']
        search_fields = ['id_mensaje']



admin.site.register(Carrera,CarreraAdmin)
admin.site.register(Sede,SedeAdmin)
admin.site.register(Estado,EstadoAdmin)
admin.site.register(TipoPago,TipoPagoAdmin)
admin.site.register(Pasajero,PasajeroAdmin)
admin.site.register(Clase_licencia,Clase_licenciaAdmin)
admin.site.register(Conductor,ConductorAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(Viaje,ViajeAdmin)
admin.site.register(Pago,PagoAdmin)
admin.site.register(Historial,HistorialAdmin)
admin.site.register(Lobby_Viaje,Lobby_ViajeAdmin)
admin.site.register(Mensaje,MensajeAdmin)

