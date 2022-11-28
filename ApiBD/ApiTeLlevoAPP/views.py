from django.shortcuts import render
#from html5lib import serialize
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.
##Carrera 1
class CarreraViewSet(generics.ListCreateAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializers

class CarreraSearchSet(generics.ListCreateAPIView):
    serializer_class = CarreraSerializers
    def get_queryset(self):
        id = self.kwargs['id_carrera']
        return Carrera.objects.filter(id_carrera=id)
##Estado 2
class EstadoViewSet(generics.ListCreateAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializers

class EstadoSearchSet(generics.ListCreateAPIView):
    serializer_class = EstadoSerializers
    def get_queryset(self):
        id = self.kwargs['id_estado']
        return Estado.objects.filter(id_estado=id)
## Sede 3
class SedeViewSet(generics.ListCreateAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializers

class SedeSearchSet(generics.ListCreateAPIView):
    serializer_class = SedeSerializers
    def get_queryset(self):
        id = self.kwargs['id_sede']
        return Sede.objects.filter(id_sede=id)
##TipoPago 4
class TipoPagoViewSet(generics.ListCreateAPIView):
    queryset = TipoPago.objects.all()
    serializer_class = TipoPagoSerializers

class TipoPagoSearchSet(generics.ListCreateAPIView):
    serializer_class = TipoPagoSerializers
    def get_queryset(self):
        id = self.kwargs['id_tipo_pago']
        return TipoPago.objects.filter(id_tipo_pago=id)
##Pasajero 5

class PasajeroViewSet(generics.ListCreateAPIView):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializers

class PasajeroSearchSet(generics.ListCreateAPIView):
    serializer_class = PasajeroSerializers
    def get_queryset(self):
        id = self.kwargs['id_pasajero']
        return Pasajero.objects.filter(id_pasajero=id)
###Clase_licencia 6
class Clase_licenciaViewSet(generics.ListCreateAPIView):
    queryset = Clase_licencia.objects.all()
    serializer_class = Clase_licenciaSerializers

class Clase_licenciaSearchSet(generics.ListCreateAPIView):
    serializer_class = Clase_licenciaSerializers
    def get_queryset(self):
        id = self.kwargs['id_clase_licencia']
        return Clase_licencia.objects.filter(id_clase_licencia=id)

###Conductor 7
class ConductorViewSet(generics.ListCreateAPIView):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializers

class ConductorSearchSet(generics.ListCreateAPIView):
    serializer_class = ConductorSerializers
    def get_queryset(self):
        id = self.kwargs['id_conductor']
        return Conductor.objects.filter(id_conductor=id)
##Color 8
class ColorViewSet(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializers

class ColorSearchSet(generics.ListCreateAPIView):
    serializer_class = ColorSerializers
    def get_queryset(self):
        id = self.kwargs['id_color']
        return Color.objects.filter(id_color=id)
##Vehiculo 9
class VehiculoViewSet(generics.ListCreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializers

class VehiculoSearchSet(generics.ListCreateAPIView):
    serializer_class = VehiculoSerializers
    def get_queryset(self):
        id = self.kwargs['id_vehiculo']
        return Vehiculo.objects.filter(id_vehiculo=id)
##Viaje 10
class ViajeViewSet(generics.ListCreateAPIView):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializers

class ViajeSearchSet(generics.ListCreateAPIView):
    serializer_class = ViajeSerializers
    def get_queryset(self):
        id = self.kwargs['id_viaje']
        return Viaje.objects.filter(id_viaje=id)

class ViajeInclude(generics.ListCreateAPIView):
    serializer_class = ViajeSerializers
    def get_queryset(self):
        id = self.kwargs['id_conductor']
        return Viaje.objects.filter(id_conductor=id)

class ViajeExclude(generics.ListCreateAPIView):
    serializer_class = ViajeSerializers
    def get_queryset(self):
        id = self.kwargs['id_conductor']
        return Viaje.objects.exclude(id_conductor=id)
    
##Pago 11
class PagoViewSet(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializers

class PagoSearchSet(generics.ListCreateAPIView):
    serializer_class = PagoSerializers
    def get_queryset(self):
        id = self.kwargs['id_pago']
        return Pago.objects.filter(id_pago=id)
##Historial 12
class HistorialViewSet(generics.ListCreateAPIView):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializers

class HistorialSearchSet(generics.ListCreateAPIView):
    serializer_class = HistorialSerializers
    def get_queryset(self):
        id = self.kwargs['id_historial']
        return Historial.objects.filter(id_historial=id)

## Lobby_Viaje 13

class Lobby_ViajeViewSet(generics.ListCreateAPIView):
    queryset = Lobby_Viaje.objects.all()
    serializer_class = Lobby_ViajeSerializers

class Lobby_ViajeSearchSet(generics.ListCreateAPIView):
    serializer_class = Lobby_ViajeSerializers
    def get_queryset(self):
        id = self.kwargs['id_viaje']
        return Lobby_Viaje.objects.filter(id_viaje=id)



#Mensaje 14
class MensajeViewSet(generics.ListCreateAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializers

class MensajeSearchSet(generics.ListCreateAPIView):
    serializer_class = MensajeSerializers
    def get_queryset(self):
        id = self.kwargs['id_mensaje']
        return Mensaje.objects.filter(id_mensaje=id)
