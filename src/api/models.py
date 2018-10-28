from django.db import models
from django.db.utils import OperationalError
from django.http import JsonResponse
from datetime import date


class IncomeType(models.Model):
    type = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.type)


class Income(models.Model):
    type = models.ForeignKey(IncomeType, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    amount = models.FloatField()

    def __str__(self):
        return str("type: {}, amount: {}, date: {}".format(self.type, self.amount, self.date))


class ExpenseType(models.Model):
    type = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.type)


class Expense(models.Model):
    type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    amount = models.FloatField()

    def __str__(self):
        return str("type: {}, amount: {}, date: {}".format(self.type, self.amount, self.date))


class BalanceDB(models.Model):
    amount = models.FloatField(default=0)

    def __str__(self):
        return str("Balance: {}".format(self.amount))


class Balance:
    def __init__(self):
        try:
            self.model = BalanceDB
            self.expense_model = Expense
            self.income_model = Income
            self.object = self.get_object()
        except OperationalError:
            pass

    def get_object(self):
        try:
            return self.model.objects.get(id=1)
        except models.ObjectDoesNotExist:
            balance_obj = self.model()
            balance_obj.save()
            return balance_obj

    def calculate_amount(self):
        income = self.income_model.objects.aggregate(income=models.Sum("amount"))["income"]
        expense = self.expense_model.objects.aggregate(expense=models.Sum("amount"))["expense"]
        income = 0 if income is None else income
        expense = 0 if expense is None else expense
        self.object.amount = income - expense
        self.object.save()

    def get(self):
        return self.object.amount

    def set(self, value):
        self.object.amount += value
        self.object.save()
        return self.object.amount

    @property
    def response(self):
        return JsonResponse({
            "amount": self.get()
        })


class Budget(models.Model):
    type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    month_id = models.IntegerField()
    amount = models.FloatField(default=0)

    def __str__(self):
        return str("type: {}, month id: {}, amount: {}".format(self.type, self.month_id, self.amount))

    class Meta:
        unique_together = ("type", "month_id")
