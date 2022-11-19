from django.urls import path
from .views import ListaPessoaView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView
from . import views

urlpatterns = [ 
    path('', ListaPessoaView.as_view(), name='Pessoa.index'),

    path('novo/', PessoaCreateView.as_view(), name='Pessoa.novo'),

    path('<int:pk>/editar', PessoaUpdateView.as_view(), name='Pessoa.editar'),

    path('<int:pk>/deletar', PessoaDeleteView.as_view(), name='Pessoa.deletar'),

    path('<int:pk_pessoa>/contatos',
        views.contatos, name='Pessoa.contatos'),
    path('<int:pk_pessoa>/contato/novo/',
        views.contato_novo, name='contato.novo'),
    path('<int:pk_pessoa>/contato/<int:pk>/editar',
        views.contato_editar, name='contato.editar'),
    path('<int:pk_pessoa>/contato/<int:pk>/remover',
        views.contato_remover, name='contato.remover'),
]
