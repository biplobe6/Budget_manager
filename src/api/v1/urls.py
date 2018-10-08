from django.conf.urls import url
from . import views

app_name = "v1"

urlpatterns = [
    url("^income_type$", views.incometype.List.as_view(), name="list_income_type"),
    url("^income_type/add$", views.incometype.Add.as_view(), name="add_income_type"),
    url("^income_type/(?P<id>\d+)$", views.incometype.Details.as_view(), name="details_income_type"),
    url(r'^hello', views.hello.index, name="hello")
]
