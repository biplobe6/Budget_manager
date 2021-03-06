from django.conf.urls import url
from . import views

app_name = "v1"

urlpatterns = [
    url(r'^budget$', views.budget.get, name="budget"),
    url(r'^budget/calc$', views.budget.calc, name="budget_calc"),
    url(r'^budget/(?P<id>\d+)$', views.budget.Details.as_view(), name="budget_details"),
    url(r'^balance$', views.balance.get, name="balance"),
    url(r'^balance/calc$', views.balance.calculate, name="balance_calc"),
    url("^income$", views.income.get, name="list_income"),
    url("^income/add$", views.income.Add.as_view(), name="add_income"),
    url("^income/(?P<id>\d+)$", views.income.Details.as_view(), name="edit_income"),
    url("^income/type$", views.incometype.List.as_view(), name="list_income_type"),
    url("^income/type/add$", views.incometype.Add.as_view(), name="add_income_type"),
    url("^income/type/(?P<id>\d+)$", views.incometype.Details.as_view(), name="details_income_type"),
    url("^expense$", views.expense.get, name="list_expense"),
    url("^expense/add$", views.expense.Add.as_view(), name="add_expense"),
    url("^expense/(?P<id>\d+)$", views.expense.Details.as_view(), name="edit_expense"),
    url("^expense/type$", views.expensetype.List.as_view(), name="list_expense_type"),
    url("^expense/type/add$", views.expensetype.Add.as_view(), name="add_expense_type"),
    url("^expense/type/(?P<id>\d+)$", views.expensetype.Details.as_view(), name="details_expense_type")
]
