from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Dog(models.Model):

    namb = models.CharField(max_length=35, verbose_name='номер договора', **NULLABLE)
    name = models.CharField(max_length=50, verbose_name='ФИО/Наименование', unique=True)
    fase = models.CharField(max_length=50, verbose_name='физ./юрлицо')
    status = models.CharField(max_length=50, verbose_name='Статус')
    id_adress = models.CharField(max_length=150, verbose_name='id адреса')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'


class Adres(models.Model):
    sity = models.CharField(max_length=35, verbose_name='Город')
    strit = models.CharField(max_length=50, verbose_name='Улица')
    hom_nambe = models.CharField(max_length=50, verbose_name='Номер дома')
    hom = models.CharField(max_length=50, verbose_name='Номер квартиры', **NULLABLE)

    def __str__(self):
        return f'{self.sity} {self.strit} {self.hom_nambe} {self.hom}'

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Prase(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тариф наименование')
    cost = models.IntegerField(max_length=10, verbose_name='Стоимость')
    data_n = models.DateField(max_length=20, verbose_name='Дата начала действия', **NULLABLE)
    data_f = models.DateField(max_length=20, verbose_name='Дата окончания действия', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.cost} {self.data_n} {self.data_f}'

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'


class Many(models.Model):
    man = models.IntegerField(max_length=10, verbose_name='Сумма')
    data_op = models.DateField(max_length=20, verbose_name='Дата начала действия', **NULLABLE)

    @property
    def __int__(self):
        return f'{self.man} {self.data_op} '

    class Meta:
        verbose_name = 'Приход денежных средств'
        verbose_name_plural = 'Приходы денежных средств'
