# 📸 GUIA - PÁGINA DE TRABALHOS/PORTFÓLIO

## 🎉 O que foi criado?

Uma **galeria linda e profissional** para mostrar seus trabalhos realizados!

### Acesse agora:
🌐 **http://localhost:8000/trabalhos/**

---

## ✅ Mudanças Realizadas

### 1. **Removido:**
- ❌ Div `image-decoration` (decoração de imagem)
- ❌ Seções CSS relacionadas ao `about-image`
- ❌ Elemento visual desnecessário da home

### 2. **Criado:**
- ✅ Modelo `Trabalho` no banco de dados
- ✅ Página `/trabalhos/` com galeria
- ✅ Menu "Trabalhos" na navegação
- ✅ Estilos CSS modernos com hover effects
- ✅ Layout responsivo para mobile
- ✅ Seção de estatísticas animadas
- ✅ Pasta `media/trabalhos/` para imagens

---

## 📸 Como Adicionar Trabalhos

### Passo a Passo:

#### 1. Acesse o Admin
```
http://localhost:8000/admin/
```

#### 2. Faça Login
Use suas credenciais de superusuário

#### 3. Vá em "Trabalhos"
No menu lateral, clique em **"Trabalhos"**

#### 4. Adicione Novo Trabalho
Clique no botão **"Adicionar Trabalho"**

#### 5. Preencha os Campos:

| Campo | Descrição | Exemplo | Obrigatório |
|-------|-----------|---------|-------------|
| **Título** | Nome do trabalho | "Unhas Decoradas com Pedrarias" | ✅ Sim |
| **Descrição** | Detalhes do trabalho | "Unha em gel com nail art exclusiva" | ❌ Não |
| **Imagem** | Foto do trabalho | Upload de arquivo JPG/PNG | ✅ Sim |
| **Serviço** | Serviço relacionado | Manicure & Pedicure | ❌ Não |
| **Destaque** | Mostrar na galeria | ✅ Marcado | ✅ Sim |
| **Ordem** | Ordem de exibição | 1, 2, 3... | ✅ Sim |

#### 6. Salve
Clique em **"Salvar"**

---

## 📐 Especificações das Imagens

### Formato Ideal:
```
┌─────────────┐
│             │
│    1:1      │  ← QUADRADO
│             │
└─────────────┘
```

### Detalhes Técnicos:
- **Proporção:** 1:1 (quadrada)
- **Tamanho:** 800x800 pixels (ideal) ou 1200x1200 pixels
- **Formato:** JPG, PNG ou WEBP
- **Peso:** Até 1 MB por imagem
- **Qualidade:** Alta resolução

### Onde Ficam:
As imagens são salvas automaticamente em:
```
media/trabalhos/
```

---

## 🎨 Funcionalidades da Galeria

### Visual:
- ✅ Grid responsivo (2-4 colunas dependendo da tela)
- ✅ Imagens quadradas uniformes
- ✅ Efeito hover com overlay gradient
- ✅ Zoom suave na imagem ao passar mouse
- ✅ Informações aparecem no hover

### Informações Exibidas:
- 📝 Título do trabalho
- 📄 Descrição (resumo)
- 🏷️ Tag do serviço (se vinculado)

### Extras:
- 📊 Seção de estatísticas com contadores animados
- 🎯 CTA (Botões de ação para reservar ou WhatsApp)
- 📱 100% responsivo (mobile, tablet, desktop)

---

## 💡 Dicas para Fotos Incríveis

### ✅ O que FAZER:

1. **Iluminação**
   - Use luz natural (próximo a janela)
   - Evite sombras fortes
   - Luz uniforme no trabalho

2. **Foco**
   - Foco nítido nos detalhes
   - Mostre a qualidade do trabalho
   - Destaque os diferenciais

3. **Composição**
   - Centralize o trabalho
   - Fundo limpo e neutro
   - Evite elementos dispersantes

4. **Qualidade**
   - Fotos em alta resolução
   - Sem filtros exagerados
   - Cores fiéis ao resultado real

### ❌ O que EVITAR:

- ❌ Fotos borradas ou tremidas
- ❌ Iluminação muito escura
- ❌ Fundos bagunçados
- ❌ Fotos muito pequenas/pixeladas
- ❌ Marcas d'água de outros apps

---

## 📱 Layout Responsivo

### Desktop (>992px):
```
┌───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │
├───┼───┼───┼───┤
│ 5 │ 6 │ 7 │ 8 │
└───┴───┴───┴───┘
```
4 colunas

### Tablet (768px-992px):
```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
└───┴───┴───┘
```
3 colunas

### Mobile (<768px):
```
┌───────┐
│   1   │
├───────┤
│   2   │
├───────┤
│   3   │
└───────┘
```
1 coluna

---

## 📊 Seção de Estatísticas

A página inclui uma seção com estatísticas animadas:

### Dados Exibidos:
1. **Trabalhos Realizados** 
   - Contado automaticamente do banco
   - Ícone: ❤️

2. **Clientes Satisfeitas**
   - Número fixo (edite no template)
   - Ícone: 😊

3. **Avaliação Média**
   - Mostrar 5 estrelas
   - Ícone: ⭐

4. **Anos de Experiência**
   - Tempo de carreira
   - Ícone: 🏆

### Como Editar:
Abra `templates/trabalhos.html` e procure por:
```html
<div class="stat-number" data-target="100">0</div>
```
Altere o número `100` para o valor desejado.

---

## 🎯 Estado Vazio (Quando não há trabalhos)

Quando não há trabalhos cadastrados, a página exibe:

- 🖼️ Ícone grande de galeria
- 💬 Mensagem amigável
- 🔗 Botão para ver os serviços
- 🎨 Design atraente

**Isso garante uma boa experiência mesmo sem conteúdo!**

---

## 🔄 Fluxo de Uso

### Para o Administrador:
```
1. Login no Admin
   ↓
2. Adicionar Trabalho
   ↓
3. Upload da Foto
   ↓
4. Preencher Dados
   ↓
5. Salvar
   ↓
6. Trabalho aparece na galeria
```

### Para o Visitante:
```
1. Acessa o site
   ↓
2. Clica em "Trabalhos"
   ↓
3. Vê a galeria
   ↓
4. Passa mouse nas fotos (hover)
   ↓
5. Vê detalhes do trabalho
   ↓
6. Clica em "Fazer Reserva"
```

---

## 🛠️ Arquivos Criados/Modificados

### Novos Arquivos:
```
templates/trabalhos.html        ← Template da galeria
media/trabalhos/                ← Pasta de imagens
website/migrations/0002_*.py    ← Migração do modelo
PAGINA_TRABALHOS.txt            ← Este guia (texto)
GUIA_TRABALHOS.md               ← Este guia (markdown)
```

### Arquivos Modificados:
```
website/models.py               ← Modelo Trabalho adicionado
website/views.py                ← View trabalhos criada
website/urls.py                 ← Rota adicionada
website/admin.py                ← Admin configurado
templates/base.html             ← Menu atualizado
templates/home.html             ← Decoração removida
static/css/style.css            ← Estilos da galeria
```

---

## 💻 Comandos Úteis

### Ver trabalhos no shell:
```bash
python manage.py shell
```

No shell Python:
```python
from website.models import Trabalho

# Ver todos os trabalhos
Trabalho.objects.all()

# Contar trabalhos
Trabalho.objects.count()

# Criar trabalho (sem imagem)
Trabalho.objects.create(
    titulo='Teste',
    descricao='Descrição',
    ordem=1
)

# Sair
exit()
```

### Refazer migrações (se necessário):
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🎨 Personalização Avançada

### Alterar Cores da Galeria:
Edite `static/css/style.css`:
```css
.portfolio-overlay {
    background: var(--gradient-overlay);
    /* Altere para outras cores se quiser */
}
```

### Alterar Proporção das Imagens:
```css
.portfolio-image {
    padding-top: 100%; /* 1:1 (quadrado) */
    /* 56.25% = 16:9 (horizontal) */
    /* 75% = 4:3 */
    /* 133.33% = 3:4 (vertical) */
}
```

### Mudar Número de Colunas:
```css
.portfolio-grid {
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    /* Altere 350px para mudar tamanho mínimo */
}
```

---

## 📈 Otimização de Imagens

### Ferramentas Online:
1. **TinyPNG** - https://tinypng.com/
2. **Squoosh** - https://squoosh.app/
3. **ImageOptim** - https://imageoptim.com/

### Processo:
1. Tire a foto em alta qualidade
2. Corte para formato quadrado
3. Redimensione para 800x800 ou 1200x1200
4. Comprima para reduzir tamanho
5. Faça upload no admin

---

## 🔗 Links Rápidos

| Descrição | URL |
|-----------|-----|
| Galeria de Trabalhos | http://localhost:8000/trabalhos/ |
| Admin - Trabalhos | http://localhost:8000/admin/website/trabalho/ |
| Adicionar Trabalho | http://localhost:8000/admin/website/trabalho/add/ |
| Home | http://localhost:8000/ |

---

## ❓ FAQ - Perguntas Frequentes

### P: Posso adicionar mais de 3 trabalhos?
**R:** Sim! Adicione quantos quiser. A galeria se ajusta automaticamente.

### P: As imagens precisam ser quadradas?
**R:** Não obrigatório, mas recomendado para melhor visualização.

### P: Posso usar fotos do celular?
**R:** Sim! Apenas certifique-se que a qualidade está boa.

### P: Como remover um trabalho?
**R:** No admin, entre em Trabalhos, selecione e delete.

### P: Posso desativar ao invés de deletar?
**R:** Sim! Desmarque "Destaque" que o trabalho não aparecerá.

### P: Como ordenar os trabalhos?
**R:** Use o campo "Ordem". Menor número aparece primeiro.

---

## 🎉 Pronto!

Agora você tem uma **galeria profissional** para mostrar seus trabalhos!

### Próximos Passos:
1. ✅ Adicione pelo menos 6-9 trabalhos
2. ✅ Use suas melhores fotos
3. ✅ Teste em mobile e desktop
4. ✅ Compartilhe o link com clientes

---

**💜 Boa sorte e sucesso com sua galeria!**
