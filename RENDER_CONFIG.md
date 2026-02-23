# ⚡ CONFIGURAÇÃO RENDER - COPIE E COLE

## 🚀 PASSO A PASSO VISUAL

### 1. Delete o serviço atual no Render (se houver)

### 2. New + → Web Service

### 3. Conecte o repositório: LUCAS-HEITOR/TATY-ESPACODIVAS

### 4. Preencha EXATAMENTE assim:

---

#### 📝 Name (Nome do serviço):
```
taty-espacodivas
```

---

#### 🌍 Region (Região):
```
Oregon (US West)
```
(Ou qualquer outra, tanto faz)

---

#### 🌿 Branch:
```
main
```

---

#### 🐍 Environment (Ambiente):
```
Python 3
```

---

#### 🔨 Build Command (Comando de build):
**⚠️ ATENÇÃO: Copie APENAS esta linha abaixo:**

```
pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
```

---

#### ▶️ Start Command (Comando de iniciar):
**⚠️ ATENÇÃO: Copie APENAS esta linha abaixo:**

```
gunicorn taty_espacodivas.wsgi
```

---

#### 💰 Instance Type:
```
Free
```

---

### 5. 🔧 Environment Variables (Variáveis de Ambiente)

Clique em **"Advanced"** → Role até **"Environment Variables"** → Adicione 3 variáveis:

#### Variável 1:
```
Key: SECRET_KEY
Value: b7(1ezmj5g&&(ev+y)xi40k&8fi#_dopcw3vp+63d3w*-%$ntb
```

#### Variável 2:
```
Key: DEBUG
Value: False
```

#### Variável 3:
```
Key: ALLOWED_HOSTS
Value: .onrender.com
```

---

### 6. 🚀 Create Web Service

Aguarde 5-10 minutos para o build terminar.

---

## 📋 RESUMO DO QUE COPIAR:

### Build Command (APENAS ISSO):
```
pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
```

### Start Command (APENAS ISSO):
```
gunicorn taty_espacodivas.wsgi
```

### Variáveis (3 no total):
```
SECRET_KEY = b7(1ezmj5g&&(ev+y)xi40k&8fi#_dopcw3vp+63d3w*-%$ntb
DEBUG = False
ALLOWED_HOSTS = .onrender.com
```

---

## ✅ Depois do Deploy:

1. Acesse o Shell do Render
2. Digite: `python manage.py createsuperuser`
3. Crie usuário e senha
4. Acesse: `https://taty-espacodivas.onrender.com/admin/`
5. Adicione os trabalhos e serviços

---

**💜 Pronto! Seu site estará no ar!**
