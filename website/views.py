from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Servico, Contato, Reserva, Trabalho

# Create your views here.

def home(request):
    """Landing page com serviços em destaque"""
    servicos = Servico.objects.filter(destaque=True)
    context = {
        'servicos': servicos
    }
    return render(request, 'home.html', context)


def trabalhos(request):
    """Galeria de trabalhos realizados"""
    trabalhos = Trabalho.objects.filter(destaque=True)
    context = {
        'trabalhos': trabalhos
    }
    return render(request, 'trabalhos.html', context)


def contato(request):
    """Página de contato"""
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        mensagem = request.POST.get('mensagem')
        
        Contato.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            mensagem=mensagem
        )
        
        messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato em breve.')
        return redirect('contato')
    
    return render(request, 'contato.html')


def reservar(request):
    """Página de reservas"""
    servicos = Servico.objects.all()
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        servico_id = request.POST.get('servico')
        data_desejada = request.POST.get('data_desejada')
        horario = request.POST.get('horario')
        observacoes = request.POST.get('observacoes')
        
        servico = Servico.objects.get(id=servico_id)
        
        Reserva.objects.create(
            nome=nome,
            telefone=telefone,
            email=email,
            servico=servico,
            data_desejada=data_desejada,
            horario=horario,
            observacoes=observacoes
        )
        
        messages.success(request, 'Reserva realizada com sucesso! Entraremos em contato para confirmação.')
        return redirect('reservar')
    
    context = {
        'servicos': servicos
    }
    return render(request, 'reservar.html', context)
