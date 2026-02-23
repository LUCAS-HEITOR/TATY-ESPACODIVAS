from django.db import models

# Create your models here.

class Servico(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Serviço')
    descricao = models.TextField(verbose_name='Descrição')
    imagem = models.ImageField(upload_to='servicos/', verbose_name='Imagem')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço', null=True, blank=True)
    destaque = models.BooleanField(default=False, verbose_name='Mostrar na Landing Page')
    ordem = models.IntegerField(default=0, verbose_name='Ordem de Exibição')
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['ordem', 'nome']
    
    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-mail')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    mensagem = models.TextField(verbose_name='Mensagem')
    data_envio = models.DateTimeField(auto_now_add=True, verbose_name='Data de Envio')
    
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['-data_envio']
    
    def __str__(self):
        return f'{self.nome} - {self.email}'


class Reserva(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    email = models.EmailField(verbose_name='E-mail')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, verbose_name='Serviço')
    data_desejada = models.DateField(verbose_name='Data Desejada')
    horario = models.TimeField(verbose_name='Horário')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data da Reserva')
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['-data_criacao']
    
    def __str__(self):
        return f'{self.nome} - {self.servico.nome} - {self.data_desejada}'


class Trabalho(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    imagem = models.ImageField(upload_to='trabalhos/', verbose_name='Imagem')
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Serviço Relacionado')
    destaque = models.BooleanField(default=True, verbose_name='Mostrar na Galeria')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Publicação')
    ordem = models.IntegerField(default=0, verbose_name='Ordem de Exibição')
    
    class Meta:
        verbose_name = 'Trabalho'
        verbose_name_plural = 'Trabalhos'
        ordering = ['-ordem', '-data_criacao']
    
    def __str__(self):
        return self.titulo
