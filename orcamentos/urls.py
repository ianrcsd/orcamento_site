from django.urls import path
from . import views

app_name = "orcamentos"

urlpatterns = [
    path("", views.index, name="index"),
    path("orcamentos/", views.lista_orcamentos, name="lista_orcamentos"),
    path("orcamentos/criar/", views.criar_orcamento, name="criar_orcamento"),
    path("orcamentos/<int:pk>/", views.detalhe_orcamento, name="detalhe_orcamento"),
]
