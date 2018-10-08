from rest_framework import generics
from rest_framework import serializers
from api import models


class IncomeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IncomeType
        fields = [
            "id",
            "type"
        ]


class List(generics.ListAPIView):
    queryset = models.IncomeType.objects.all()
    serializer_class = IncomeTypeSerializer


class Add(generics.CreateAPIView):
    queryset = models.IncomeType.objects.all()
    serializer_class = IncomeTypeSerializer


class Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.IncomeType.objects.all()
    serializer_class = IncomeTypeSerializer
    lookup_field = "id"
