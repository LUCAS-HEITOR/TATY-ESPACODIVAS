# ⚡ COMANDOS ÚTEIS - TATY ESPAÇO DIVAS

## 🚀 Iniciar o Projeto

### 1. Criar superusuário (FAÇA ISSO PRIMEIRO!)
```bash
python manage.py createsuperuser
```

### 2. Iniciar servidor
```bash
python manage.py runserver
```

### 3. Acessar o site
- Site: http://localhost:8000/
- Admin: http://localhost:8000/admin/


## 🔄 Comandos de Banco de Dados

### Criar migrações (após alterar models.py)
```bash
python manage.py makemigrations
```

### Aplicar migrações
```bash
python manage.py migrate
```

### Ver SQL das migrações
```bash
python manage.py sqlmigrate website 0001
```


## 🛠️ Comandos de Desenvolvimento

### Verificar problemas do projeto
```bash
python manage.py check
```

### Coletar arquivos estáticos (para produção)
```bash
python manage.py collectstatic
```

### Abrir shell do Django
```bash
python manage.py shell
```


## 📦 Gerenciamento de Dados

### Criar dados de exemplo via shell
```bash
python manage.py shell
```

Depois no shell Python:
```python
from website.models import Servico

# Criar um serviço de exemplo
Servico.objects.create(
    nome='Manicure Completa',
    descricao='Cuidado completo para suas unhas',
    preco=50.00,
    destaque=True,
    ordem=1
)

# Ver todos os serviços
Servico.objects.all()

# Sair do shell
exit()
```

### Backup do banco de dados
```bash
# Windows PowerShell
Copy-Item db.sqlite3 -Destination db.sqlite3.backup

# Ou simplesmente copie o arquivo manualmente
```

### Restaurar backup
```bash
# Windows PowerShell
Copy-Item db.sqlite3.backup -Destination db.sqlite3
```


## 🧹 Limpeza

### Limpar cache do Python
```bash
# Windows PowerShell
Get-ChildItem -Path . -Include __pycache__ -Recurse -Force | Remove-Item -Force -Recurse
```


## 📝 Logs e Debug

### Ver logs em tempo real
O servidor já mostra os logs. Para mais detalhes:

Em settings.py, adicione:
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
```


## 🔐 Segurança (Para Produção)

### Gerar nova SECRET_KEY
```bash
python manage.py shell
```

No shell:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```

Copie a chave gerada e substitua no settings.py


## 📊 Estatísticas

### Contar registros
```bash
python manage.py shell
```

No shell:
```python
from website.models import Servico, Contato, Reserva

print(f"Serviços: {Servico.objects.count()}")
print(f"Contatos: {Contato.objects.count()}")
print(f"Reservas: {Reserva.objects.count()}")

exit()
```


## 🌐 Para Deploy (Futuro)

### Instalar dependências de produção
```bash
pip install gunicorn
pip install whitenoise
```

### Configurações para produção
Em settings.py:
```python
DEBUG = False
ALLOWED_HOSTS = ['seudominio.com', 'www.seudominio.com']
```


## 🆘 Problemas Comuns

### Erro: port is already in use
```bash
# Matar processo na porta 8000
# Windows PowerShell
Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess | Stop-Process -Force

# Ou use outra porta
python manage.py runserver 8001
```

### Erro: No module named 'PIL'
```bash
pip install Pillow
```

### Erro: Migrate não funciona
```bash
# Deletar migrações antigas (cuidado!)
Remove-Item website\migrations\0*.py

# Recriar
python manage.py makemigrations
python manage.py migrate
```


## 📚 Comandos Python/Pip

### Ver pacotes instalados
```bash
pip list
```

### Instalar de requirements.txt
```bash
pip install -r requirements.txt
```

### Atualizar pip
```bash
python -m pip install --upgrade pip
```

### Criar ambiente virtual (recomendado)
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```


## 🎨 Desenvolvimento Front-end

### Arquivos para editar:

**CSS:**
```
static/css/style.css
```

**JavaScript:**
```
static/js/script.js
```

**Templates:**
```
templates/base.html
templates/home.html
templates/contato.html
templates/reservar.html
```


## 💾 Atalhos Úteis

### Parar servidor
```
Ctrl + C
```

### Limpar terminal
```
cls
```

### Ver histórico de comandos
```
history
```


---

🚀 **DICA PRO:** Mantenha sempre um backup do `db.sqlite3` antes de fazer alterações importantes!
