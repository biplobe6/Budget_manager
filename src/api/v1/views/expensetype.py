from rest_framework import generics
from rest_framework import serializers
from api import models


class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExpenseType
        fields = [
            "id",
            "type"
        ]


class List(generics.ListAPIView):
    queryset = models.ExpenseType.objects.all()
    serializer_class = ExpenseTypeSerializer


class Add(generics.CreateAPIView):
    queryset = models.ExpenseType.objects.all()
    serializer_class = ExpenseTypeSerializer


class Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ExpenseType.objects.all()
    serializer_class = ExpenseTypeSerializer
    lookup_field = "id"
