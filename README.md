# 🌸 Taty Espaço Divas

Site de beleza e bem-estar feminino desenvolvido com Django.

## 📋 Sobre o Projeto

Site institucional para o **Taty Espaço Divas**, um espaço dedicado à beleza feminina com serviços de:
- 💅 Manicure e Pedicure
- ✨ Limpeza Facial
- 💆 Drenagem Linfática
- 👁️ Design de Sobrancelhas

## ⚙️ Instalação

### Pré-requisitos
- Python 3.8 ou superior
- Django 6.0
- Pillow (para imagens)

### Passos para rodar o projeto

1. **Instalar dependências:**
```bash
pip install django pillow
```

2. **Aplicar migrações (já feitas):**
```bash
python manage.py migrate
```

3. **Criar superusuário para acessar o admin:**
```bash
python manage.py createsuperuser
```
Siga as instruções e crie um usuário administrador.

4. **Iniciar o servidor:**
```bash
python manage.py runserver
```

5. **Acessar o site:**
- Site principal: http://localhost:8000/
- Painel administrativo: http://localhost:8000/admin/

## 📄 Páginas do Site

### 1. Landing Page (/)
- Apresentação do espaço
- Serviços em destaque
- Depoimentos de clientes (screenshots 16:9 com molduras)
- Call-to-action para reservas

### 2. Trabalhos (/trabalhos/) - 🆕 NOVA!
- **Galeria profissional de trabalhos realizados**
- Grid responsivo com hover effects
- Seção de estatísticas animadas
- Links para agendamento
- Estado vazio quando não há trabalhos
- **📘 Ver [GUIA_TRABALHOS.md](GUIA_TRABALHOS.md) para instruções completas**

### 3. Contato (/contato/)
- Formulário de contato
- Informações de contato (telefone, e-mail, endereço)
- Horário de atendimento
- Mapa de localização
- Links para redes sociais

### 4. Reserve Já (/reservar/)
- Formulário de reserva de horários
- Seleção de serviço
- Escolha de data e horário
- Observações personalizadas

## 🎨 Administração

Acesse o painel admin em `/admin/` para:

### Gerenciar Serviços
1. Faça login no admin
2. Clique em "Serviços"
3. Clique em "Adicionar Serviço"
4. Preencha os campos:
   - **Nome:** Nome do serviço (ex: Manicure Completa)
   - **Descrição:** Descrição detalhada do serviço
   - **Imagem:** Faça upload de uma foto do serviço
   - **Preço:** Valor do serviço (opcional)
   - **Destaque:** Marque para aparecer na landing page
   - **Ordem:** Defina a ordem de exibição

### Gerenciar Trabalhos (Galeria) - 🆕
1. Faça login no admin
2. Clique em "Trabalhos"
3. Clique em "Adicionar Trabalho"
4. Preencha os campos:
   - **Título:** Nome do trabalho (ex: "Unhas Decoradas com Pedrarias")
   - **Descrição:** Detalhes do trabalho realizado
   - **Imagem:** Upload da foto (formato quadrado ideal: 800x800px)
   - **Serviço:** Selecione o serviço relacionado (opcional)
   - **Destaque:** ✅ Marque para aparecer na galeria
   - **Ordem:** Número para ordenação (1, 2, 3...)
5. Salve

**📖 Ver [GUIA_TRABALHOS.md](GUIA_TRABALHOS.md) para guia completo com dicas de fotografia e especificações de imagem.**

### Visualizar Contatos
- Todos os contatos enviados pelo formulário ficam salvos no admin
- Acesse "Contatos" para ver as mensagens

### Visualizar Reservas
- Todas as reservas ficam salvas no admin
- Acesse "Reservas" para gerenciar os agendamentos

## 📸 Como Adicionar Imagens

### Imagens dos Serviços

#### Método 1: Pelo Admin (Recomendado)
1. Acesse http://localhost:8000/admin/
2. Vá em "Serviços"
3. Clique em um serviço ou crie um novo
4. No campo "Imagem", clique em "Escolher arquivo"
5. Selecione a imagem do serviço
6. Marque "Destaque" se quiser que apareça na home
7. Salve

#### Método 2: Manualmente
1. Coloque as imagens na pasta `media/servicos/`
2. As imagens devem estar em formato JPG, PNG ou WEBP
3. Recomenda-se imagens quadradas (ex: 800x800px)

---

### Imagens dos Trabalhos (Galeria) - 🆕

#### Pelo Admin (Único método)
1. Acesse http://localhost:8000/admin/
2. Vá em "Trabalhos"
3. Clique em "Adicionar Trabalho"
4. No campo "Imagem", clique em "Escolher arquivo"
5. Selecione a foto do trabalho
6. Preencha título e descrição
7. Marque "Destaque" para aparecer na galeria
8. Defina a ordem de exibição
9. Salve

#### Especificações das Fotos de Trabalhos:
- **Formato ideal:** Quadrado (1:1)
- **Tamanho recomendado:** 800x800px ou 1200x1200px
- **Tipos aceitos:** JPG, PNG, WEBP
- **Peso máximo:** 1 MB por imagem
- **Qualidade:** Alta resolução
- **Pasta:** `media/trabalhos/`

**💡 Dica:** Use fotos com boa iluminação, fundo limpo e foco nos detalhes do trabalho.

**📘 Ver [GUIA_TRABALHOS.md](GUIA_TRABALHOS.md) para dicas profissionais de fotografia.**

---

### Depoimentos (Screenshots)
1. Tire screenshots de avaliações/comentários de clientes no Instagram
2. Salve as imagens em formato **16:9** (1920x1080px ideal)
3. Coloque na pasta `static/images/depoimentos/`
4. Nomeie como: `depoimento1.jpg`, `depoimento2.jpg`, `depoimento3.jpg`

## 🎨 Personalização

### Cores
Edite o arquivo `static/css/style.css` e modifique as variáveis CSS no início:
```css
:root {
    --primary-color: #e91e63;  /* Rosa principal */
    --secondary-color: #9c27b0;  /* Roxo */
    --accent-color: #ff4081;  /* Rosa accent */
}
```

### Informações de Contato
Edite os templates em `templates/`:
- `templates/base.html` - Footer com informações gerais
- `templates/contato.html` - Página de contato completa
- **Altere:** telefones, e-mails, endereço, links das redes sociais

### Mapa
No arquivo `templates/contato.html`, procure por `<iframe>` e substitua pelo embed do Google Maps do seu endereço real.

## 📱 Responsividade

O site é totalmente responsivo e se adapta a:
- 💻 Desktop
- 📱 Tablets
- 📱 Smartphones

## 🚀 Funcionalidades

- ✅ Design moderno com gradientes e animações
- ✅ 4 páginas completas (Home, Trabalhos, Contato, Reservar)
- ✅ **Galeria profissional de trabalhos com hover effects** 🆕
- ✅ **Depoimentos em formato de screenshots com molduras 16:9** 🆕
- ✅ Formulários de contato e reserva funcionais
- ✅ Sistema de mensagens para feedback ao usuário
- ✅ Área administrativa completa (4 modelos)
- ✅ Upload de imagens dos serviços e trabalhos
- ✅ Sistema de destaque de serviços e trabalhos
- ✅ **Grid responsivo com 1-4 colunas automáticas**
- ✅ **Seção de estatísticas animadas**
- ✅ Validação de formulários
- ✅ Formatação automática de telefone
- ✅ Bloqueio de reservas aos domingos
- ✅ Animações suaves ao scroll
- ✅ Menu mobile responsivo
- ✅ Links para Instagram e WhatsApp integrados

## 📦 Estrutura do Projeto

```
KAUA/
├── taty_espacodivas/          # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── website/                    # App principal
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── 0002_trabalho.py    # 🆕 Migração do modelo Trabalho
│   ├── admin.py               # Configuração do admin
│   ├── models.py              # Modelos: Servico, Trabalho, Contato, Reserva
│   ├── views.py               # Views das páginas
│   └── urls.py                # URLs do app
├── templates/                  # Templates HTML
│   ├── base.html              # Template base
│   ├── home.html              # Landing page
│   ├── trabalhos.html         # 🆕 Galeria de trabalhos
│   ├── contato.html           # Página de contato
│   └── reservar.html          # Página de reservas
├── static/                     # Arquivos estáticos
│   ├── css/
│   │   └── style.css          # CSS principal (1644 linhas)
│   ├── js/
│   │   └── script.js          # JavaScript
│   └── images/
│       └── depoimentos/       # Screenshots de avaliações (16:9)
├── media/                      # Arquivos de mídia (uploads)
│   ├── servicos/              # Imagens dos serviços
│   └── trabalhos/             # 🆕 Fotos dos trabalhos (galeria)
├── manage.py                   # Script de gerenciamento
├── db.sqlite3                 # Banco de dados
├── README.md                  # Este arquivo
├── GUIA_TRABALHOS.md          # 🆕 Guia completo da galeria
└── PAGINA_TRABALHOS.txt       # 🆕 Documentação técnica
```

## 🎯 Próximos Passos

1. **Criar superusuário:**
   ```bash
   python manage.py createsuperuser
   ```

2. **Adicionar serviços:**
   - Acesse o admin em http://localhost:8000/admin/
   - Cadastre os serviços com imagens

3. **Adicionar trabalhos à galeria:** 🆕
   - No admin, vá em "Trabalhos"
   - Adicione pelo menos 6-9 fotos de trabalhos realizados
   - Use fotos quadradas de boa qualidade
   - **Ver [GUIA_TRABALHOS.md](GUIA_TRABALHOS.md) para instruções detalhadas**

4. **Adicionar depoimentos:**
   - Tire screenshots de avaliações de clientes
   - Salve em formato 16:9 (1920x1080px)
   - Coloque em `static/images/depoimentos/`
   - Nomeie como: depoimento1.jpg, depoimento2.jpg, depoimento3.jpg

5. **Personalizar informações:**
   - Altere telefones e endereços nos templates
   - Atualize links das redes sociais
   - Configure o mapa do Google Maps

6. **Iniciar servidor:**
   ```bash
   python manage.py runserver
   ```

7. **Testar o site:**
   - Home: http://localhost:8000/
   - Galeria: http://localhost:8000/trabalhos/
   - Contato: http://localhost:8000/contato/
   - Reservar: http://localhost:8000/reservar/

## 💡 Dicas

- **Imagens de Serviços:** Use imagens de boa qualidade e com boa iluminação
- **Imagens de Trabalhos:** Fotos quadradas (1:1), fundo limpo, foco nos detalhes 🆕
- **Depoimentos:** Screenshots 16:9 de avaliações reais do Instagram 🆕
- **SEO:** Adicione descrições detalhadas nos serviços e trabalhos
- **Backup:** Faça backup regular do banco de dados (db.sqlite3)
- **Redes Sociais:** Mantenha os links atualizados no template base
- **Galeria:** Adicione pelo menos 6-9 trabalhos para a galeria ficar completa 🆕

## 🌐 Redes Sociais

- **Instagram:** [@taty.espaco_divas](https://www.instagram.com/taty.espaco_divas/)
- **WhatsApp:** [(93) 9210-4344](https://wa.me/5593992104344)
- **Localização:** Itaituba - PA

## 🔗 Links Úteis

- **Home:** http://localhost:8000/
- **Galeria de Trabalhos:** http://localhost:8000/trabalhos/ 🆕
- **Contato:** http://localhost:8000/contato/
- **Reservar:** http://localhost:8000/reservar/
- **Admin:** http://localhost:8000/admin/
- **Adicionar Trabalho:** http://localhost:8000/admin/website/trabalho/add/ 🆕

## 📚 Documentação Adicional

- **[GUIA_TRABALHOS.md](GUIA_TRABALHOS.md)** - 🆕 Guia completo da galeria de trabalhos com:
  - Como adicionar fotos
  - Especificações de imagem
  - Dicas de fotografia
  - Layout responsivo
  - Personalização avançada
  - FAQ completo

- **[PAGINA_TRABALHOS.txt](PAGINA_TRABALHOS.txt)** - 🆕 Documentação técnica da implementação

## 📞 Suporte

Para dúvidas ou problemas, verifique:
- Os logs do servidor no terminal
- O console do navegador (F12) para erros de JavaScript
- Os erros do Django no terminal

## 🌟 Features do Design

- Gradientes vibrantes rosa e roxo
- Animações suaves ao scroll
- Efeitos hover nos cards e galeria
- **Overlay com gradient nas fotos da galeria** 🆕
- **Grid automático responsivo (auto-fill minmax)** 🆕
- **Seção de estatísticas com contadores animados** 🆕
- Ícones Font Awesome
- Fontes Google: Playfair Display e Poppins
- Sombras suaves e modernas
- Layout responsivo com Grid CSS
- Menu mobile funcional
- Botões com efeitos 3D
- Formulários estilizados
- **Depoimentos com molduras decorativas** 🆕
- **Estado vazio na galeria quando não há trabalhos** 🆕

## 🆕 Última Atualização - Página de Trabalhos

### O que foi adicionado:
1. ✅ Modelo `Trabalho` no banco de dados
2. ✅ Página `/trabalhos/` com galeria profissional
3. ✅ Link "Trabalhos" no menu de navegação
4. ✅ Upload de fotos via admin com preview
5. ✅ Grid responsivo (1-4 colunas conforme tela)
6. ✅ Hover effects com overlay e zoom
7. ✅ Seção de estatísticas animadas
8. ✅ Estado vazio elegante
9. ✅ Pasta `media/trabalhos/` para uploads
10. ✅ Admin completo com filtros e busca
11. ✅ Removido decoração de imagem desnecessária da home
12. ✅ Depoimentos convertidos para formato de screenshots 16:9

### Como usar:
1. Acesse o admin
2. Vá em "Trabalhos"
3. Adicione fotos dos trabalhos realizados
4. Visualize em http://localhost:8000/trabalhos/

**📘 Ver [GUIA_TRABALHOS.md](GUIA_TRABALHOS.md) para guia completo!**

---

Desenvolvido com 💜 para o Taty Espaço Divas
