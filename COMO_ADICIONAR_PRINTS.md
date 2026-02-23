# 📸 GUIA - COMO ADICIONAR PRINTS DE DEPOIMENTOS

## 🎯 Local dos Arquivos

Coloque seus prints de depoimentos em:
```
static/images/depoimentos/
```

## 📛 Nomes dos Arquivos

Os prints devem ter EXATAMENTE estes nomes:

✅ **depoimento1.jpg** (ou .png)
✅ **depoimento2.jpg** (ou .png)  
✅ **depoimento3.jpg** (ou .png)

**IMPORTANTE:** Use exatamente esses nomes! O site vai procurar por eles.


## 📐 Especificações dos Prints

### Formato Recomendado:
- **Proporção:** 16:9 (horizontal)
- **Resolução:** 1920x1080 pixels (Full HD)
- **Alternativa:** 1280x720 pixels (HD)
- **Mínimo:** 960x540 pixels

### Formatos Aceitos:
- ✅ **JPG** (recomendado)
- ✅ **PNG** (mantém qualidade)
- ✅ **WEBP** (menor tamanho)

### Tamanho do Arquivo:
- **Ideal:** 200-500 KB
- **Máximo:** 1 MB


## 📱 Como Tirar Screenshots Perfeitos

### No Instagram (Recomendado):

1. **Abra o post com o depoimento**
2. **Tire screenshot:**
   - **Android:** Botão Power + Volume Baixo
   - **iPhone:** Botão Lateral + Volume Alto
   - **PC:** Windows + Shift + S

3. **Edite o print:**
   - Corte as bordas desnecessárias
   - Mantenha apenas o conteúdo relevante
   - Certifique-se que o texto está legível

### No WhatsApp:

1. **Abra a conversa com o depoimento**
2. **Tire screenshot da mensagem**
3. **Edite:**
   - Corte para ficar focado na mensagem
   - Oculte informações pessoais se necessário
   - Mantenha proporção 16:9


## ✂️ Como Editar os Prints

### Ferramentas Online Grátis:

1. **Canva** - https://www.canva.com/
   - Crie um design 1920x1080
   - Importe seu screenshot
   - Ajuste e baixe

2. **Photopea** - https://www.photopea.com/
   - Editor tipo Photoshop gratuito
   - Redimensione para 1920x1080
   - Exporte como JPG

3. **ILoveIMG** - https://www.iloveimg.com/pt/redimensionar-imagem
   - Upload da imagem
   - Redimensione para 1920x1080
   - Baixe

### No Celular:

**Android:**
- Google Fotos (editar > cortar)
- Snapseed (app gratuito)

**iPhone:**
- Fotos (editar > cortar)
- Canva (app)


## 🎨 Dicas para Bons Prints

### ✅ Faça:
- Use prints de depoimentos reais
- Certifique-se que o texto está legível
- Mantenha boa qualidade
- Oculte dados sensíveis
- Use prints recentes

### ❌ Evite:
- Prints borrados ou pixelados
- Texto muito pequeno
- Imagens escuras demais
- Informações pessoais visíveis
- Screenshots com notificações


## 🔄 Passo a Passo Completo

### 1. Prepare os Prints:
```
1. Tire screenshots dos depoimentos
2. Edite e corte se necessário
3. Salve em boa qualidade
4. Renomeie para: depoimento1.jpg, depoimento2.jpg, depoimento3.jpg
```

### 2. Adicione ao Site:
```
1. Abra a pasta: static/images/depoimentos/
2. Cole os 3 arquivos
3. Substitua os arquivos existentes se houver
4. Atualize a página do site (F5)
```

### 3. Verifique:
```
1. Acesse: http://localhost:8000/
2. Role até a seção "O que Nossas Clientes Dizem"
3. Confira se os prints aparecem
4. Veja se estão com boa qualidade
```


## 🖼️ Estrutura de Pastas

```
static/
└── images/
    └── depoimentos/
        ├── depoimento1.jpg  ← Primeiro print
        ├── depoimento2.jpg  ← Segundo print
        └── depoimento3.jpg  ← Terceiro print
```


## 💡 Exemplo de Bons Depoimentos

**Instagram:**
- Posts onde clientes marcaram o perfil
- Comentários positivos
- Stories salvos nos destaques
- Avaliações com fotos

**WhatsApp:**
- Mensagens de agradecimento
- Fotos do resultado
- Elogios ao atendimento
- Recomendações


## 🎯 Checklist Final

Antes de adicionar os prints, verifique:

- [ ] São 3 prints no total
- [ ] Nomes: depoimento1.jpg, depoimento2.jpg, depoimento3.jpg
- [ ] Formato: 16:9 (horizontal)
- [ ] Resolução mínima: 960x540
- [ ] Texto legível e claro
- [ ] Boa qualidade de imagem
- [ ] Dados sensíveis ocultos
- [ ] Formato JPG ou PNG
- [ ] Tamanho menor que 1MB cada


## 🔍 Resolução de Problemas

### Print não aparece?
1. Verifique o nome do arquivo (exato!)
2. Confirme que está na pasta correta
3. Atualize a página (Ctrl + F5)
4. Verifique o formato (.jpg ou .png)

### Print está distorcido?
1. Verifique a proporção (deve ser 16:9)
2. Use dimensões recomendadas: 1920x1080
3. Não estique a imagem

### Print está muito pesado?
1. Use compressor: https://tinypng.com/
2. Reduza qualidade para 80-85%
3. Converta para JPG se estiver em PNG


## 📱 Sugestão de Workflow

### Método Rápido:
1. Tire 3 screenshots no celular
2. Envie para o PC via WhatsApp Web
3. Salve as imagens
4. Use ILoveIMG para redimensionar todas de uma vez
5. Renomeie e cole na pasta

### Método Profissional:
1. Tire screenshots
2. Edite no Canva (modelo 1920x1080)
3. Adicione moldura ou filtro sutil se quiser
4. Baixe em alta qualidade
5. Cole na pasta do site


## 🎨 Personalização Extra (Opcional)

Se quiser adicionar MAIS depoimentos:

1. Adicione mais imagens: depoimento4.jpg, depoimento5.jpg...
2. Edite o arquivo: `templates/home.html`
3. Copie um bloco de testimonial-card e ajuste o número

```html
<div class="testimonial-card">
    <div class="testimonial-image-wrapper">
        <img src="{% static 'images/depoimentos/depoimento4.jpg' %}" alt="Depoimento 4" class="testimonial-screenshot">
    </div>
</div>
```


## 🌟 Dica Final

**SEMPRE PEÇA PERMISSÃO** às clientes antes de usar seus depoimentos publicamente!

Uma mensagem simples:
> "Oi! Adorei seu feedback! Posso usar como depoimento no meu site? 😊"


---

🎨 Qualquer dúvida, consulte o README.md ou COMANDOS.md!
