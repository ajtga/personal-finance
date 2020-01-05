from django.db import models


class MovementMethod(models.Model):
    METHODS = (
        ('debit card', 'Debit Card'),
        ('account debit', 'Account Debit'),
        ('credit card', 'Credit Card'),
        ('transfer', 'Transfer'),
        ('cash', 'Cash'),
    )
    name = models.CharField(primary_key=True, max_length=15, choices=METHODS)


class MovementType(models.Model):
    TYPES = (
        ('payment', 'Payment'),
        ('salary', 'Salary'),
        ('withdraw', 'Withdraw'),
        ('loan', 'Loan')
    )
    SIGNS = (
        (1, 'Credit'),
        (-1, 'Debit'),
    )

    name = models.CharField(primary_key=True, max_length=10, choices=TYPES)
    description = models.CharField(max_length=255, verbose_name='movement type description')
    sign = models.IntegerField(default=1, choices=SIGNS)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='category name')


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, verbose_name='first name')
    last_name = models.CharField(max_length=255, verbose_name='last name')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='group name')

    def __str__(self):
        return f'{self.name}'


class AccountHolder(models.Model):
    holder_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='account holder name')
    code = models.CharField(max_length=3, verbose_name='account holder code')

    def __str__(self):
        return f'{self.name} - {self.code}'


class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    iso_code = models.CharField(max_length=3, verbose_name='ISO 4217 code')
    symbol = models.CharField(max_length=255, verbose_name='currency symbol')
    name = models.CharField(max_length=255, verbose_name='currency name')


class AccountType(models.Model):
    TYPES = (
        ('checking', 'Checking account'),
        ('savings', 'Savings account'),
        ('payments', 'Payments account'),
    )
    name = models.CharField(primary_key=True, max_length=10, choices=TYPES)


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    holder = models.ForeignKey(AccountHolder, on_delete=models.CASCADE)  # TODO: certain holders only offer payments account type, create a form to validate this
    current_balance = models.FloatField(verbose_name='current balance')
    last_updated = models.DateTimeField(verbose_name='last balance update')
    name = models.CharField(max_length=255, verbose_name='account name')
    number = models.CharField(max_length=11, verbose_name='account number')
    agency_number = models.CharField(max_length=5, verbose_name='account agency number')
    type = models.ForeignKey(AccountType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - R$ {self.current_balance}'


class Affiliation(models.Model):
    affiliation_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.person.first_name} from {self.group.name}'


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
    is_movement_lead = models.BooleanField(default=True, verbose_name='is the affiliate leading this movement?')

    class Meta:
        verbose_name_plural = "Movement by's"
