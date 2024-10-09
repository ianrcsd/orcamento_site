from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Orcamento, Cliente, ProdutoServico, OrcamentoItem
from .forms import OrcamentoForm, OrcamentoItemFormSet


def index(request):
    return render(request, "orcamentos/index.html")


@login_required
def lista_orcamentos(request):
    orcamentos = Orcamento.objects.all()
    return render(
        request, "orcamentos/lista_orcamentos.html", {"orcamentos": orcamentos}
    )


@login_required
def criar_orcamento(request):
    if request.method == "POST":
        form = OrcamentoForm(request.POST)
        formset = OrcamentoItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            orcamento = form.save()
            formset.instance = orcamento
            formset.save()
            return redirect("orcamentos:lista_orcamentos")
    else:
        form = OrcamentoForm()
        formset = OrcamentoItemFormSet()
    return render(
        request, "orcamentos/criar_orcamento.html", {"form": form, "formset": formset}
    )


@login_required
def detalhe_orcamento(request, pk):
    orcamento = get_object_or_404(Orcamento, pk=pk)
    return render(
        request, "orcamentos/detalhe_orcamento.html", {"orcamento": orcamento}
    )
