from django.db import models


class MovementMethods(models.Model):
    name = models.CharField(primary_key=True, max_length=255)


class MovementType(models.Model):
    SIGN_OPTIONS = (
        (1, 'Credit'),
        (-1, 'Debit'),
    )
    name = models.CharField(primary_key=True, max_length=255)
    description = models.CharField(max_length=255, verbose_name='movement type description')
    sign = models.IntegerField(default=1, choices=SIGN_OPTIONS)


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='category name')


class People(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, verbose_name='first name')
    last_name = models.CharField(max_length=255, verbose_name='last name')


class Groups(models.Model):
    group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='group name')


class AccountHolders(models.Model):
    holder_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='account holder name')
    code = models.CharField(max_length=3, verbose_name='account holder code')


class Currencies(models.Model):
    currency_id = models.AutoField(primary_key=True)
    iso_code = models.CharField(max_length=3, verbose_name='ISO 4217 code')
    symbol = models.CharField(max_length=255, verbose_name='currency symbol')
    name = models.CharField(max_length=255, verbose_name='currency name')
