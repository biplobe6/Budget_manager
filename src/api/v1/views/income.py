from rest_framework import generics, serializers, viewsets
from api import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import date


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Income
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

    queryset = models.Income.objects.filter(**filter_list)
    serializer = IncomeSerializer(queryset, many=True)
    return Response(serializer.data)


class Add(generics.CreateAPIView):
    queryset = models.Income.objects.all()
    serializer_class = IncomeSerializer


class Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Income.objects.all()
    serializer_class = IncomeSerializer
    lookup_field = "id"
