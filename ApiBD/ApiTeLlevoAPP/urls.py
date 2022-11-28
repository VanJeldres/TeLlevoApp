
from django.contrib import admin
from django.urls import re_path as path
from ApiTeLlevoAPP import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path(r'admin/', admin.site.urls),
    
    ##Carrera 1        
    path(r'^api/carrera/$',csrf_exempt(views.CarreraViewSet.as_view())),
    path(r'^api/carrera/(?P<id_carrera>.+)/$',views.CarreraSearchSet.as_view()),
    ##Estado 2
    path(r'^api/estado/$',csrf_exempt(views.EstadoViewSet.as_view())),
    path(r'^api/estado/(?P<id_estado>.+)/$',views.EstadoSearchSet.as_view()),
    ## Sede 3
    path(r'^api/sede/$',csrf_exempt(views.SedeViewSet.as_view())),
    path(r'^api/sede/(?P<id_sede>.+)/$',views.SedeSearchSet.as_view()),
    ##TipoPago 4
    path(r'^api/tipoPago/$',csrf_exempt(views.TipoPagoViewSet.as_view())),
    path(r'^api/tipoPago/(?P<id_tipo_pago>.+)/$',views.TipoPagoSearchSet.as_view()),
    ##Pasajero 5
    path(r'^api/pasajero/$',csrf_exempt(views.PasajeroViewSet.as_view())),
    path(r'^api/pasajero/(?P<id_pasajero>.+)/$',views.PasajeroSearchSet.as_view()),
    ###Clase_licencia 6
    path(r'^api/clase_licencia/$',csrf_exempt(views.Clase_licenciaViewSet.as_view())),
    path(r'^api/clase_licencia/(?P<id_clase_licencia>.+)/$',views.Clase_licenciaSearchSet.as_view()),
    ###Conductor 7
    path(r'^api/conductor/$',csrf_exempt(views.ConductorViewSet.as_view())),
    path(r'^api/conductor/(?P<id_conductor>.+)/$',views.ConductorSearchSet.as_view()),
    ##Color 8
    path(r'^api/color/$',csrf_exempt(views.ColorViewSet.as_view())),
    path(r'^api/color/(?P<id_color>.+)/$',views.ColorSearchSet.as_view()),
    ##Vehiculo 9
    path(r'^api/vehiculo/$',csrf_exempt(views.VehiculoViewSet.as_view())),
    path(r'^api/vehiculo/(?P<id_vehiculo>.+)/$',views.VehiculoSearchSet.as_view()),
    ##Viaje 10
    path(r'^api/viaje/$',csrf_exempt(views.ViajeViewSet.as_view())),
    path(r'^api/viaje/(?P<id_viaje>.+)/$',views.ViajeSearchSet.as_view()),
    path(r'^viaje/include/(?P<id_conductor>.+)/$',views.ViajeInclude.as_view()),
    path(r'^viaje/exclude/(?P<id_conductor>.+)/$',views.ViajeExclude.as_view()),
    ##Pago 11
    path(r'^api/pago/$',csrf_exempt(views.PagoViewSet.as_view())),
    path(r'^api/pago/(?P<id_pago>.+)/$',views.PagoSearchSet.as_view()),
    ##Historial 12
    path(r'^api/historial/$',csrf_exempt(views.HistorialViewSet.as_view())),
    path(r'^api/historial/(?P<id_historial>.+)/$',views.HistorialSearchSet.as_view()),
    ##Lobby_Viaje 13
    path(r'^api/Lobby_Viaje/$',csrf_exempt(views.Lobby_ViajeViewSet.as_view())),
    path(r'^api/Lobby_Viaje/(?P<id_viaje>.+)/$',views.Lobby_ViajeSearchSet.as_view()),
    ##Mensaje 14
    path(r'^api/Mensaje/$',csrf_exempt(views.MensajeViewSet.as_view())),
    path(r'^api/Mensaje/(?P<id_mensaje>.+)/$',views.MensajeSearchSet.as_view()),
]
