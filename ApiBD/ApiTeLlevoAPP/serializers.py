from .models import *
from rest_framework import serializers
from django.db.models import fields

class CarreraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields=['id_carrera','carrera'] 


class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields=['id_estado','estado'] 

class SedeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields=['id_sede','sede'] 

class TipoPagoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoPago
        fields=['id_tipo_pago','tipo_pago'] 

class PasajeroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields=['id_pasajero','nombre','appaterno','apmaterno','rut','fech_nacimiento','correo','numero_celular','calificacion','password','id_sede','id_carrera'] 

class Clase_licenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clase_licencia
        fields=['id_clase_licencia','clase_licencia'] 

class ConductorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields=['id_conductor','num_licencia','id_clase_licencia'] 

class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields=['id_color','color'] 

class VehiculoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields=['id_vehiculo','modelo_vehiculo','patente','id_color','id_conductor'] 

class ViajeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields=['id_viaje','origen','destino','fech_viaje','hora_inicio','capacidad','precio','descripcion','id_conductor'] 

class PagoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields=['id_pago','fech_pago','monto','id_viaje','id_pasajero','id_conductor'] 
    
class HistorialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Historial
        fields=['id_historial','id_viaje','nombre','id_pasajero','id_conductor','monto','origen','destino','fech_viaje'] 

class Lobby_ViajeSerializers (serializers.ModelSerializer):
    class Meta:
        model = Lobby_Viaje
        fields=['id_lobby_viaje','id_viaje', 'id_pasajero']

class MensajeSerializers (serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields=['id_mensaje','mensaje', 'fech_mensaje','id_enviador','id_receptor']







 