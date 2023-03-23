from django.db import models

# Create your models here.

#* Device Base
class DevType(models.Model):
    dev_type = models.CharField(max_length=20, verbose_name='Tipos de Dispositivo')

    def __str__(self) -> str:
        return self.dev_type
    
    class Meta:
        verbose_name = 'Tipo de Dispositivo'
        verbose_name_plural = 'Tipos de Dispositivos'
        db_table = 'TipoDispositivo'
        ordering = ['id']
        

class Brand(models.Model):
    dev_type = models.ForeignKey(DevType, on_delete=models.CASCADE, related_name='brands_model')
    brand = models.CharField(max_length=20, verbose_name='Marca')

    def __str__(self) -> str:
        return self.brand
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        db_table = 'MarcaDispositivo'
        ordering = ['id']

class Model(models.Model):
    dev_type = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models_dev_type')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models_brand')
    model = models.CharField(max_length=20, verbose_name='Modelo')
    img = models.ImageField(upload_to='DevImages/%Y/%m/%d')

    def __str__(self) -> str:
        return self.model
    
    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
        db_table = 'ModeloDispositivo'
        ordering = ['id']

#* Internet access & Ips

class IAccess(models.Model):
    internet_access = models.CharField(max_length=20, verbose_name="Tipo de Acceso a Internet")

    def __str__(self) -> str:
        return self.internet_access
    
    class Meta:
        verbose_name = 'Acceso a Internet'
        verbose_name_plural = 'Tipos de Acceso a Internet'
        db_table = 'Internet'
        ordering = ['id']

class Ip(models.Model):
    i_access = models.ForeignKey(IAccess, on_delete=models.CASCADE, related_name='i_access')
    ip = models.CharField(max_length=15, verbose_name='Ip')

    def __str__(self) -> str:
        return self.ip
    
    class Meta:
        verbose_name = 'Ip'
        verbose_name_plural = 'Ips'
        db_table = 'Ip'
        ordering = ['id']

#* Techs

class Techs(models.Model):
    name = models.CharField(max_length=45, verbose_name='Nombre del Tecnico')
    last_name = models.CharField(max_length=45, verbose_name='Apellido del Tecnico')

    def __str__(self) -> str:
        return self.last_name
    
    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'
        db_table = 'Tecnicos'
        ordering = ['id']

#* Device Status

class DevStatus(models.Model):
    status = models.CharField(max_length=25, verbose_name='Estado del Dispositivo')
    function_status = models.CharField(max_length=25, verbose_name='Estado Funcional del Dispositivo')

    def __str__(self) -> str:
        return self.status
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        db_table = 'EstadosDispositivos'
        ordering = ['id']

#* Offices

class Province(models.Model):
    province = models.CharField(max_length=45, verbose_name='Provincia')

    def __str__(self) -> str:
        return self.province
    
    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        db_table = 'Provincias'
        ordering = ['id']

class Locality(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='locality_province')
    locality = models.CharField(max_length=45, verbose_name='Localidad')

    def __str__(self) -> str:
        return self.locality
    
    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        db_table = 'Localidades'
        ordering = ['id']

class Address(models.Model):
    province = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name='address_province')
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name='address_locality')
    zip_code = models.CharField(max_length=7, verbose_name='Codigo Postal')
    neightbordhood = models.CharField(max_length=45, verbose_name='Barrio')
    address = models.CharField(max_length=100, verbose_name='Direccion')
    floor = models.CharField(max_length=4, null=True, blank=True, verbose_name='Piso')

    def __str__(self) -> str:
        return self.address

    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'
        db_table = 'Domicilio'
        ordering = ['id']

class Office(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_neme='office_address')
    floor = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='office_floor')
    office = models.CharField(max_length=45, verbose_name='Oficina')

    def __str__(self) -> str:
        return self.office
    
    class Meta:
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'
        db_table = 'Oficina'
        ordering = ['id']

#* Devices

class Devices(models.Model):
    device = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='devices_device_type')
    brand = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='devices_brand')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='devices_model')
    img = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='devices_img')
    has_ip = models.BooleanField()
    ip = models.ForeignKey(Ip, on_delete=models.CASCADE, related_name='devices_ip')
    i_access = models.ForeignKey(Ip, on_delete=models.CASCADE, related_name='devices_i_access')
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='devices_office')
    last_review = models.DateField()
    tech = models.ForeignKey(Techs, on_delete=models.CASCADE, related_name='devices_tech')
    maintenment = models.TextField()
    status = models.ForeignKey(DevStatus, on_delete=models.CASCADE, related_name='devices_status')
    pendings_repairs = models.CharField(max_length=45, verbose_name='Reparaciones Pendientes')
    func_status = models.ForeignKey(DevStatus, on_delete=models.CASCADE, related_name='devices_functional_status')

#* Device Users

class DevUsers(models.Model):
    dev_user_name = models.CharField(max_length=45, verbose_name='Nombre del Usuario de Dispositivo')
    dev_user_last_name = models.CharField(max_length=45, verbose_name='Apellido del Usuario de Dispositivo')
    cuil = models.CharField(max_length=11, verbose_name='CUIL')
    device = models.ForeignKey(Devices, on_delete=models.CASCADE, related_name='dev_user_devices')
    msg_account = models.CharField(max_length=15, verbose_name='Nombre de Usuario de Mensajeria')
    msg_password = models.CharField(max_length=16, verbose_name='Contraseña Mensajeria')
    username = models.CharField(max_length=6, verbose_name='Nombre de Usuario')
    typical_password = models.BooleanField()
    password = models.CharField(max_length=25, verbose_name='Contraseña')
    