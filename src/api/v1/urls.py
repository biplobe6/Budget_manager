from django.conf.urls import url
from . import views

app_name = "v1"

urlpatterns = [
    url("^income$", views.income.get, name="list_income"),
    url("^income/add$", views.income.Add.as_view(), name="add_income"),
    url("^income/(?P<id>\d+)$", views.income.Details.as_view(), name="edit_income"),
    url("^income/type$", views.incometype.List.as_view(), name="list_income_type"),
    url("^income/type/add$", views.incometype.Add.as_view(), name="add_income_type"),
    url("^income/type/(?P<id>\d+)$", views.incometype.Details.as_view(), name="details_income_type")
]
