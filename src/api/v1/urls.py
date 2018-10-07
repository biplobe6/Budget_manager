from django.conf.urls import url
from . import views

app_name = "v1"

urlpatterns = [
    url(r'^income/get', views.income.get_total, name="get_income"),
    url(r'^hello', views.hello.index, name="hello")
]
