from api import models
from rest_framework.response import Response
from rest_framework import serializers, decorators, generics
from datetime import date


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Budget
        fields = [
            "id",
            "type",
            "month_id",
            "amount"
        ]


def extract_date(request):
    today = date.today()
    year = int(request.GET.get("y", today.year))
    month = int(request.GET.get("m", today.month))
    return year, month, int("{}{}".format(
        year if year < today.year else today.year,
        month if month < today.month else today.month
    ))


@decorators.api_view(["GET"])
def get(request):
    year, month, month_id = extract_date(request)
    query_set = models.Budget.objects.filter(month_id=month_id)
    serializer = BudgetSerializer(query_set, many=True)
    return Response(serializer.data)


@decorators.api_view(["GET"])
def calc(request):
    year, month, month_id = extract_date(request)
    query_set = []
    for expense_type in models.ExpenseType.objects.all():
        budget = models.Budget.objects.filter(type=expense_type).last()
        if budget is None:
            budget = models.Budget(
                type=expense_type,
                month_id=month_id
            )
            budget.save()
        query_set.append(budget)
    serializer = BudgetSerializer(query_set, many=True)
    return Response(serializer.data)


class Details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BudgetSerializer
    queryset = models.Budget.objects.all()
    lookup_field = "id"


