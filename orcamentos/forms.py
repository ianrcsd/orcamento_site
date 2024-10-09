from django import forms
from .models import Orcamento, OrcamentoItem


class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ["cliente", "titulo"]


from django.forms import inlineformset_factory

OrcamentoItemFormSet = inlineformset_factory(
    Orcamento,
    OrcamentoItem,
    fields=("produto_servico", "quantidade"),
    extra=1,
    can_delete=True,
)
