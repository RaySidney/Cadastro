from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pessoa
from .forms import PessoaForm

class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('bnome') or None
        filtro_data = self.request.GET.get('bdata') or None

        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)
        
        if filtro_data:
            queryset = queryset.filter(data_nascimento__contains=filtro_data)
        
       
        return queryset 

class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'
    
class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'

class PessoaDeleteView(DeleteView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'
