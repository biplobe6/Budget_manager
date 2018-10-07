from django.db import models


class IncomeType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return str(self.type)


class Income(models.Model):
    type = models.ForeignKey(IncomeType)
    date = models.DateField(auto_now_add=True, blank=True)
    amount = models.FloatField()

    def __str__(self):
        return str("type: {}, amount: {}, date: {}".format(self.type, self.amount, self.date))
