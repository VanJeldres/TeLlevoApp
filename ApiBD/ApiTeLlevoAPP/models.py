from django.db import models

#    create_at = models.DateField(auto_now_add=True) #guarda producto con la fecha actual
#    update_at = models.DateField(auto_now=True)

class Carrera(models.Model):
    id_carrera = models.IntegerField(primary_key=True)
    carrera = models.CharField(max_length=40)

    def __str__(self):
        return self.carrera

    class Meta:
        db_table = 'db_carrera'

class Estado(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=40)

    def __str__(self):
        return self.estado

    class Meta:
        db_table = 'db_estado'



class Sede(models.Model):
    id_sede = models.IntegerField(primary_key=True)
    sede = models.CharField(max_length=40)

    def __str__(self):
        return self.sede

    class Meta:
        db_table = 'db_sede'


class TipoPago(models.Model):
    id_tipo_pago = models.IntegerField(primary_key=True)
    tipo_pago = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo_pago

    class Meta:
        db_table = 'db_tipo_pago'

class Pasajero(models.Model):
    id_pasajero = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    appaterno = models.CharField(max_length=40)
    apmaterno = models.CharField(max_length=40)
    rut = models.CharField(max_length=14)
    fech_nacimiento = models.DateField()
    correo = models.CharField(max_length=50)
    numero_celular = models.CharField(max_length=15)
    calificacion = models.IntegerField()  
    password=models.CharField(max_length=20)
    id_sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_pasajero)

    class Meta:
        db_table = 'db_pasajero'


class Clase_licencia (models.Model):
    id_clase_licencia = models.IntegerField(primary_key=True)
    clase_licencia = models.CharField(max_length=20)

    def __str__(self):
        return self.clase_licencia

    class Meta:
        db_table = 'db_clase_licencia'

class Conductor (models.Model):
    id_conductor = models.IntegerField(primary_key=True)
    num_licencia = models.CharField(max_length=14)
    id_clase_licencia = models.ForeignKey(Clase_licencia, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_conductor)

    class Meta:
        db_table = 'db_conductor'


class Color (models.Model):
    id_color = models.IntegerField(primary_key=True)
    color = models.CharField(max_length=15)

    def __str__(self):
        return self.color

    class Meta:
        db_table = 'db_color'


class Vehiculo(models.Model):
    id_vehiculo = models.IntegerField(primary_key=True)
    modelo_vehiculo = models.CharField(max_length=40)
    patente = models.CharField(max_length=40)
    id_color =  models.ForeignKey(Color, on_delete=models.CASCADE)
    id_conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_vehiculo)
    class Meta:
        db_table = 'db_vehiculo'


class Viaje(models.Model):
    id_viaje = models.IntegerField(primary_key=True)
    origen = models.CharField(max_length=40)
    destino = models.CharField(max_length=40)
    fech_viaje = models.DateField()
    hora_inicio = models.TimeField()
    capacidad = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=40)
    id_conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_viaje)

    class Meta:
        db_table = 'db_viaje'


class Pago (models.Model):
    id_pago = models.IntegerField(primary_key=True)
    fech_pago = models.DateField(models.DateField(auto_now_add=True))
    monto = models.IntegerField()
    id_viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    id_pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    id_conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_pago)

    class Meta:
        db_table = 'db_pago'


class Historial (models.Model):
    id_historial =models.IntegerField(primary_key=True)
    id_viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    id_pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    id_conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    monto = models.IntegerField()
    origen = models.CharField(max_length=40)
    destino = models.CharField(max_length=40)
    fech_viaje = models.DateField()

    def __str__(self):
        return str(self.id_historial)
    

    class Meta:
        db_table = 'db_historial'

class Lobby_Viaje (models.Model):
    id_lobby_viaje =models.IntegerField(primary_key=True)
    id_viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    id_pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.id_viaje)
    

    class Meta:
        db_table = 'db_lobby_viaje'



#### CHAT


class Mensaje (models.Model):
    id_mensaje =models.IntegerField(primary_key=True)
    mensaje = models.CharField(max_length=200)
    fech_mensaje = models.DateField(models.DateField(auto_now_add=True))
    id_enviador= models.IntegerField()
    id_receptor = models.IntegerField()

    def __str__(self):
        return str(self.id_mensaje)
    

    class Meta:
        db_table = 'db_mensaje'

