from django.db import models
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
