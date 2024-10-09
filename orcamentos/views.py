from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Orcamento, Cliente, ProdutoServico, OrcamentoItem
from .forms import OrcamentoForm, OrcamentoItemFormSet

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.db.models import Q


def index(request):
    return render(request, "orcamentos/index.html")


@login_required
def lista_orcamentos(request):
    query = request.GET.get("q")
    if query:
        orcamentos = Orcamento.objects.filter(
            Q(titulo__icontains=query) | Q(cliente__nome__icontains=query)
        )
    else:
        orcamentos = Orcamento.objects.all()
    return render(
        request,
        "orcamentos/lista_orcamentos.html",
        {"orcamentos": orcamentos, "query": query},
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
    orcamento = get_object_or_404(Orcamento, id=pk)

    total = sum(
        item.quantidade * item.produto_servico.preco
        for item in orcamento.orcamentoitem_set.all()
    )

    return render(
        request,
        "orcamentos/detalhe_orcamento.html",
        {"orcamento": orcamento, "total": total},
    )


def gerar_pdf_orcamento(request, pk):
    orcamento = get_object_or_404(Orcamento, pk=pk)
    template = get_template("orcamentos/pdf_orcamento.html")
    html = template.render({"orcamento": orcamento})

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = (
        f'attachment; filename="orcamento_{orcamento.id}.pdf"'
    )

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Erro ao gerar PDF", status=400)
    return response
