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


class Accounts(models.Model):
    account_id = models.AutoField(primary_key=True)
    holder_id = models.ForeignKey(AccountHolders, on_delete=models.CASCADE)
    current_balance = models.FloatField(verbose_name='current balance')
    last_balance_update = models.DateTimeField(verbose_name='last balance update')
    account_name = models.CharField(max_length=255, verbose_name='account name')


class Affiliations(models.Model):
    affiliation_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)


class MonthlyBalances(models.Model):
    balance_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    balance = models.FloatField(verbose_name='balance')
    month = models.DateField(verbose_name='month')


class Subcategories(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='subcategory name')


class Budget(models.Model):
    limit_id = models.AutoField(primary_key=True)
    subcategory_id = models.ForeignKey(Subcategories, on_delete=models.CASCADE)
    month_limit = models.FloatField(default=0.0, verbose_name='month limit')


class Movements(models.Model):
    movement_id = models.AutoField(primary_key=True)
    type = models.ForeignKey(MovementType, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategories, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currencies, on_delete=models.CASCADE)
    movement_method = models.ForeignKey(MovementMethods, on_delete=models.CASCADE)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    value = models.FloatField(verbose_name='movement value')


class Annotations(models.Model):
    annotation_id = models.AutoField(primary_key=True)
    movement = models.ForeignKey(Movements, on_delete=models.CASCADE)
    annotation_text = models.CharField(max_length=255, verbose_name='annotation text')
    annotation_datetime = models.DateTimeField(verbose_name='annotation date and time')


class MovementBy(models.Model):
    bridge_id = models.AutoField(primary_key=True)
    movement = models.ForeignKey(Movements, on_delete=models.CASCADE)
    affiliation = models.ForeignKey(Affiliations, on_delete=models.CASCADE)
