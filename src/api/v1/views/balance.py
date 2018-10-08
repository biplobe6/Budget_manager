from api import models
from django.db.models import signals
from lib.djangocommon import get_object_or_none


def get(request):
    return balance.response


def calculate(request):
    balance.calculate_amount()
    return balance.response


def expense_deleted(**kwargs):
    expense = kwargs['instance']
    balance.set(expense.amount)


def income_deleted(**kwargs):
    income = kwargs['instance']
    balance.set(-income.amount)


def expense_added(**kwargs):
    expense = kwargs['instance']
    old_expense = get_object_or_none(models.Expense, id=expense.id)
    if old_expense is None:
        balance.set(-expense.amount)
    else:
        balance.set(old_expense.amount - expense.amount)


def income_added(**kwargs):
    income = kwargs['instance']
    old_income = get_object_or_none(models.Income, id=income.id)
    if old_income is None:
        balance.set(income.amount)
    else:
        balance.set(income.amount - old_income.amount)


balance = models.Balance()
signals.post_delete.connect(expense_deleted, models.Expense)
signals.post_delete.connect(income_deleted, models.Income)

signals.pre_save.connect(expense_added, models.Expense)
signals.pre_save.connect(income_added, models.Income)
