from django.db import models


class MovementMethod(models.Model):
    name = models.CharField(primary_key=True, max_length=255)


class MovementType(models.Model):
    SIGN_OPTIONS = (
        (1, 'Credit'),
        (-1, 'Debit'),
    )
    name = models.CharField(primary_key=True, max_length=255)
    description = models.CharField(max_length=255, verbose_name='movement type description')
    sign = models.IntegerField(default=1, choices=SIGN_OPTIONS)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='category name')


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, verbose_name='first name')
    last_name = models.CharField(max_length=255, verbose_name='last name')


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='group name')


class AccountHolder(models.Model):
    holder_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='account holder name')
    code = models.CharField(max_length=3, verbose_name='account holder code')


class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    iso_code = models.CharField(max_length=3, verbose_name='ISO 4217 code')
    symbol = models.CharField(max_length=255, verbose_name='currency symbol')
    name = models.CharField(max_length=255, verbose_name='currency name')


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    holder = models.ForeignKey(AccountHolder, on_delete=models.CASCADE)
    current_balance = models.FloatField(verbose_name='current balance')
    last_updated = models.DateTimeField(verbose_name='last balance update')
    name = models.CharField(max_length=255, verbose_name='account name')
    # TODO: add account data (number, type, etc)


class Affiliation(models.Model):
    affiliation_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class MonthlyBalance(models.Model):
    balance_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    balance = models.FloatField(verbose_name='balance')
    month = models.DateField(verbose_name='month')


class Subcategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='subcategory name')


class BudgetLimit(models.Model):
    limit_id = models.AutoField(primary_key=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    month_limit = models.FloatField(default=0.0, verbose_name='month limit')


class Movement(models.Model):
    movement_id = models.AutoField(primary_key=True)
    type = models.ForeignKey(MovementType, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    movement_method = models.ForeignKey(MovementMethod, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    value = models.FloatField(verbose_name='movement value')


class Annotation(models.Model):
    annotation_id = models.AutoField(primary_key=True)
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name='annotation text')
    note_datetime = models.DateTimeField(verbose_name='annotation date and time')


class MovementBy(models.Model):
    bridge_id = models.AutoField(primary_key=True)
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Movement by's"
