from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "orcamentos"

urlpatterns = [
    path("", views.index, name="index"),
    path("orcamentos/", views.lista_orcamentos, name="lista_orcamentos"),
    path("orcamentos/criar/", views.criar_orcamento, name="criar_orcamento"),
    path("orcamentos/<int:pk>/", views.detalhe_orcamento, name="detalhe_orcamento"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
