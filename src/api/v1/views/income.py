from datetime import datetime, date
from django.http import JsonResponse
from api import models
from lib.djangocommon import get_object_or_none


def calculate_total_income(year, month):
    queryset = models.Income.objects.filter(
        date__year__lte=year,
        date__year__gte=year,
        date__month__lte=month,
        date__month__gte=month,
    )
    return sum([income.amount for income in queryset])


def get(request):
    today = datetime.now()
    year = request.GET.get("y", today.year)
    month = request.GET.get("m", today.month)
    return JsonResponse({
        "amount": calculate_total_income(year, month)
    })


def add(request):
    today = datetime.now()
    amount = request.GET.get("amount", 0)
    income_type_id = request.GET.get("t", "")
    year = int(request.GET.get("y", today.year))
    month = int(request.GET.get("m", today.month))
    day = int(request.GET.get("d", today.day))

    def result():
        return JsonResponse({"amount": calculate_total_income(year, month)})
    if amount == 0 or income_type_id == "":
        return result()
    income_date = date(year, month, day)
    income_type = get_object_or_none(models.IncomeType, id=income_type_id)
    if income_type is None:
        return result()

    models.Income(
        type=income_type,
        date=income_date,
        amount=amount
    ).save()
    return result()
