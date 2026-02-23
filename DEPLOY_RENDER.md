# 🚀 DEPLOY NO RENDER - GUIA COMPLETO

## 📋 Passo a Passo

### 1️⃣ Preparação (JÁ FEITO ✅)
- ✅ Requirements.txt atualizado
- ✅ Build.sh criado
- ✅ Settings.py configurado para produção
- ✅ Whitenoise para arquivos estáticos
- ✅ Suporte a PostgreSQL
- ✅ Variáveis de ambiente configuradas

---

### 2️⃣ Fazer Commit das Mudanças

```bash
git add .
git commit -m "Configuração para produção no Render"
git push origin main
```

---

### 3️⃣ Criar Conta no Render

1. Acesse: https://render.com/
2. Clique em **"Get Started for Free"**
3. Faça login com GitHub

---

### 4️⃣ Criar Novo Web Service

1. No dashboard, clique em **"New +"** → **"Web Service"**
2. Conecte seu repositório GitHub: **LUCAS-HEITOR/TATY-ESPACODIVAS**
3. Clique em **"Connect"**

---

### 5️⃣ Configurar o Serviço

**Configurações básicas:**
- **Name:** `taty-espacodivas`
- **Environment:** `Python 3`
- **Region:** `Oregon (US West)` ou mais próximo
- **Branch:** `main`
- **Build Command:** `bash build.sh`
- **Start Command:** `gunicorn taty_espacodivas.wsgi`

**Instance Type:**
- Selecione: **Free** (gratuito)

---

### 6️⃣ Criar Banco de Dados PostgreSQL

1. Na mesma página, clique em **"Add Database"**
2. Ou depois: **"New +"** → **"PostgreSQL"**
3. Configurações:
   - **Name:** `taty-espacodivas-db`
   - **Database:** `taty_espacodivas`
   - **User:** `taty_user`
   - **Plan:** **Free**
4. Clique em **"Create Database"**

---

### 7️⃣ Configurar Variáveis de Ambiente

No Web Service, vá em **"Environment"** e adicione:

```bash
# Obrigatórias
SECRET_KEY=copie-o-secret-key-gerado-automaticamente-ou-gere-um-novo
DEBUG=False
ALLOWED_HOSTS=.onrender.com
DATABASE_URL=vai-ser-preenchido-automaticamente-pelo-render

# Opcionais (se tiver)
PYTHON_VERSION=3.12.0
```

**Como gerar SECRET_KEY:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

### 8️⃣ Conectar Banco de Dados

1. Vá em **"Environment"** no Web Service
2. Adicione nova variável:
   - **Key:** `DATABASE_URL`
   - **Value:** Clique em **"Add from Database"** → Selecione seu banco PostgreSQL

---

### 9️⃣ Deploy!

1. Clique em **"Create Web Service"** (ou "Deploy")
2. Aguarde o build (5-10 minutos na primeira vez)
3. Acompanhe os logs para verificar se está tudo ok

---

### 🔟 Criar Superusuário

Após o deploy bem-sucedido:

1. Vá em **"Shell"** no painel do Render
2. Execute:
```bash
python manage.py createsuperuser
```
3. Preencha usuário, email e senha

**OU** use o console local conectado ao banco:
```bash
export DATABASE_URL="postgresql://..."  # copie do Render
python manage.py createsuperuser
```

---

## 🌐 Acessar o Site

Seu site estará em:
```
https://taty-espacodivas.onrender.com
```

Admin:
```
https://taty-espacodivas.onrender.com/admin/
```

---

## ⚠️ IMPORTANTE

### Arquivos Estáticos
- O Whitenoise serve os arquivos CSS/JS automaticamente ✅
- Não precisa configurar nada extra

### Arquivos de Mídia (Uploads)
- ⚠️ Render **NÃO** persiste uploads no plano gratuito
- A cada deploy, as imagens são perdidas
- **Solução:** Use serviço externo como:
  - **Cloudinary** (recomendado, free tier bom)
  - **AWS S3**
  - **Backblaze B2**

### Banco de Dados
- PostgreSQL persiste os dados ✅
- Mas os trabalhos/serviços precisam ser cadastrados novamente
- Ou faça backup/restore do banco SQLite local

---

## 🐛 Troubleshooting

### Build Falhou
- Verifique os logs
- Certifique-se que o `build.sh` tem permissão de execução:
  ```bash
  git update-index --chmod=+x build.sh
  git add build.sh
  git commit -m "Add execute permission to build.sh"
  git push
  ```

### Site não carrega
- Verifique `ALLOWED_HOSTS` inclui `.onrender.com`
- Verifique `DEBUG=False`
- Veja os logs no painel do Render

### CSS não carrega
- Execute `python manage.py collectstatic` (já está no build.sh)
- Verifique se Whitenoise está nos MIDDLEWARE

### Imagens não aparecem
- No plano free do Render, uploads não persistem
- Use Cloudinary para imagens

---

## 📊 Limites do Plano Free

- ✅ 750 horas/mês grátis
- ⚠️ Site "dorme" após 15 min sem uso
- ⚠️ Demora ~30s para "acordar" na primeira visita
- ❌ Uploads não persistem (filesystem efêmero)
- ✅ PostgreSQL: 90 dias de inatividade antes de deletar

---

## 🚀 Alternativas se o Free não servir

- **Railway:** $5/mês, melhor performance
- **Heroku:** $5-7/mês, mais estável
- **DigitalOcean App Platform:** $5/mês
- **PythonAnywhere:** Grátis, melhor para iniciantes

---

## 📚 Links Úteis

- **Render Docs:** https://render.com/docs/deploy-django
- **Django Deployment:** https://docs.djangoproject.com/en/stable/howto/deployment/
- **Whitenoise:** http://whitenoise.evans.io/

---

**💜 Boa sorte com o deploy!**
