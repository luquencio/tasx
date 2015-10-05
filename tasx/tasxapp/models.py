from django.db import models

# Create your models here.

class Client(models.Model):
    username = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20)
    home_phone = models.CharField(max_length = 20)

class Report(models.Model):
    STATUS_CHOICES = (
    ('R', 'Reportado'),
    ('PP', 'Esperando Primer pago'),
    ('P', 'Servicio en Proceso'),
    ('SP', 'Esperando Segundo Pago'),
    ('C', 'Completado'),
    )
    CATEGORY_CHOICES = (
    ('EB', 'Ebanisteria'),
    ('PL', 'Plomeria'),
    ('EL', 'Electricidad'),
    )
    date =  models.DateTimeField(auto_now_add=True)
    title =  models.CharField(max_length = 50)
    status = models.CharField(max_length = 5, choices=STATUS_CHOICES)
    descr =  models.TextField()
    category = models.CharField(max_length = 5 , choices=CATEGORY_CHOICES)
    photo = models.ImageField(upload_to="media/reports", blank=True, null=True)
    client = models.ForeignKey(Client)
    schedule = models.CharField(max_length = 50)

class Employee(models.Model):
    username = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    rating = models.IntegerField()

class ReportResult(models.Model):
    report = models.ForeignKey(Report)
    employee = models.ForeignKey(Employee)

class Payment(models.Model):
    report = models.ForeignKey(Report)
    client = models.ForeignKey(Client)
    employee = models.ForeignKey(Employee)
    cost = models.IntegerField()
    date = models.DateTimeField()

class Comments(models.Model):
    comment = models.TextField()
    rate = models.IntegerField()
    user = models.ForeignKey(Client)


## Model Methods here

def publish(self):
    self.save()
