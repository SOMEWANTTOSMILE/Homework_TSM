from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brand_logo', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class CarModel(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.brand}'


class Car(models.Model):
    vin = models.CharField(max_length=255, unique=True)
    car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.car_brand}, {self.car_model}, {self.vin}'


class User(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
