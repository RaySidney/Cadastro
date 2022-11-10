from django.urls import path
from .views import ListaPessoaView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView


urlpatterns = [ 
    path('', ListaPessoaView.as_view(), name='Pessoa.index'),
    path('novo/', PessoaCreateView.as_view(), name='Pessoa.novo'),
    path('editar/<int:pk>', PessoaUpdateView.as_view(), name='Pessoa.editar'),
    path('deletar/<int:pk>', PessoaDeleteView.as_view(), name='Pessoa.deletar')
]