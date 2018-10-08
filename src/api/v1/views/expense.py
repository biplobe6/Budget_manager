from rest_framework import generics, serializers
from api import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import date


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = [
            "id",
            'type',
            "date",
            "amount"
        ]


@api_view(["GET"])
def get(request):
    today = date.today()
    year = int(request.GET.get("y", today.year))
    month = int(request.GET.get("m", today.month))
    day = request.GET.get("d", None)
    full = request.GET.get("full", None)

    filter_list = {
        "date__year__gte": year,
        "date__year__lte": year,
        "date__month__gte": month,
        "date__month__lte": month
    } if full is None else {}
    if day is not None:
        day = int(day)
        filter_list["date__day__gte"] = day
        filter_list["date__day__lte"] = day

    queryset = models.Expense.objects.filter(**filter_list)
    serializer = ExpenseSerializer(queryset, many=True)
    return Response(serializer.data)


class Add(generics.CreateAPIView):
    queryset = models.Expense.objects.all()
    serializer_class = ExpenseSerializer


class Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_field = "id"
