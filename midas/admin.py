from django.contrib import admin

from .models import Account
from .models import AccountHolder
from .models import AccountType
from .models import Affiliation
from .models import Annotation
from. models import BudgetLimit
from .models import Category
from .models import Currency
from .models import Group
from .models import MonthlyBalance
from .models import MovementMethod
from .models import MovementType
from .models import MovementBy
from .models import Movement
from .models import Person
from .models import Subcategory


admin.site.register(Account)
admin.site.register(AccountHolder)
admin.site.register(AccountType)
admin.site.register(Affiliation)
admin.site.register(Annotation)
admin.site.register(BudgetLimit)
admin.site.register(Category)
admin.site.register(Currency)
admin.site.register(Group)
admin.site.register(MonthlyBalance)
admin.site.register(MovementMethod)
admin.site.register(MovementType)
admin.site.register(MovementBy)
admin.site.register(Movement)
admin.site.register(Person)
admin.site.register(Subcategory)
