from datetime import datetime
from django.http import JsonResponse
from api import models


def get_total(request):
    today = datetime.now()
    year = request.GET.get("y", today.year)
    month = request.GET.get("m", today.month)
    queryset = models.Income.objects.filter(
        date__year__lte=year,
        date__year__gte=year,
        date__month__lte=month,
        date__month__gte=month,
    )
    return JsonResponse({
        "total": sum([income.amount for income in queryset])
    })
