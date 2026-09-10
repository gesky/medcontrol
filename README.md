# MedControl — Site institucional (multi-página) + Painel administrativo

Site em HTML/CSS/JS puro, sem build step, sem dependências (exceto Firebase,
usado pelo painel administrativo, pelo formulário de contato, pelo blog e
pelo catálogo).

## Estrutura de pastas

Todas as imagens (logos, fotos, favicon) ficam centralizadas na pasta `imagens/`.
Os demais arquivos (HTML, CSS, JS, PDF) continuam soltos na raiz.

```
├── imagens/
│   ├── logo.svg / logo-branco.svg
│   ├── favicon.ico
│   ├── hero-bg.jpg / hero-nurse.webp
│   ├── phm-medcontrol-1.webp / phm-medcontrol-2.webp
│   ├── embalagens.webp / indicadores.webp / suporte.webp / sterifast.webp
├── js/
│   └── firebase-config.js
├── *.html (páginas do site + admin.html + bulk-import-catalogo.html)
├── styles.css / script.js
├── catalogo-medcontrol.pdf
├── firestore.rules
└── gen_site.py
```

## Páginas do site público

- `index.html` — Home
- `catalogo.html` — **Visualizador de catálogo folheável**, com efeito de "livro" (arrastar
  com mouse/touch). Usa **imagens pré-renderizadas em WebP** (`imagens/catalogo/pagina-01.webp`
  a `pagina-20.webp`) em vez de renderizar o PDF ao vivo no navegador — muito mais nítido e
  leve. Fundo branco na área do visualizador; o título/subtítulo no topo da página continuam
  com fundo azul. O PDF original (`catalogo-medcontrol.pdf`) continua no site só para o link
  "Baixar catálogo em PDF". Logo abaixo do visualizador, uma seção clonada da home ("Tudo que
  sua central de esterilização precisa..."), com fundo vermelho
- `sobre.html` — Institucional (história + como trabalhamos + diferenciais)
- `linhas.html` — Produtos (5 linhas, nesta ordem: Equipamentos em comodato → Sistema
  Sterifast → Embalagens para esterilização → Indicadores e controle de processo →
  Suporte técnico e capacitação). O card "Catálogo completo" no fim da página leva
  direto para `catalogo.html`
- `phm-medcontrol.html` — Página dedicada ao PHM MedControl
- `contato.html` — Contato (formulário funcional, grava lead no Firestore)
- `blog.html` — Listagem do blog, dinâmica (Firestore)
- `artigo.html` — Template dinâmico de artigo (`?id=`)
- `termos-de-uso.html` / `politica-de-privacidade.html` — páginas legais padrão,
  linkadas no rodapé de todas as páginas
- `sorteio.html` — página de cadastro para o sorteio da Sobecc (campanha, não está no menu
  principal — acesso por link direto/QR code)

Menu (nesta ordem): **Catálogo, Produtos, Sobre, Blog, Contato**.

A página e a seção de **Depoimentos foram removidas** do site (não existe mais
`depoimentos.html`, nem no menu, nem no rodapé, nem teaser na home).

**Importante:** o grid de "produtos em destaque" (que buscava produtos cadastrados no admin,
coleção `catalog` do Firestore) foi removido de `catalogo.html`, substituído pela seção
vermelha clonada da home. A aba **Catálogo** do painel administrativo (`admin.html`) continua
funcionando normalmente para cadastro — só não tem mais onde aparecer no site público no
momento. Se quiser voltar a exibir esses produtos em algum lugar, é só avisar.

### Header

- **Desktop:** logo + menu horizontal + botão "Falar com Especialista" (WhatsApp)
- **Mobile:** logo + botão hambúrguer (o botão de WhatsApp fica escondido no header
  mobile pra não brigar de espaço com o menu). Ao abrir o menu, aparecem os links de
  navegação + um botão "Falar no WhatsApp" no final

### Hero da home

Botão principal do hero agora é **"Conheça nossos produtos"**, levando para `linhas.html`
(antes ia direto pro WhatsApp).

## Painel administrativo (`admin.html`)

Abas (nesta ordem — Sorteio Sobecc é a primeira, e já abre ativa ao entrar no painel):

- **Sorteio Sobecc** (nova) — lista de cadastros recebidos pelo formulário público `sorteio.html`,
  com botão para sortear aleatoriamente 1 ou mais ganhadores (você escolhe a quantidade a cada
  sorteio), exportar CSV, e "Zerar sorteio" pra reiniciar do zero se precisar sortear de novo
  entre todo mundo
- **Artigos** — publicar, editar, arquivar, excluir artigos do blog
- ~~**Catálogo**~~ — desativado temporariamente (comentado no código, não excluído — ver nota
  mais abaixo)
- **Mensagens** — leads recebidos pelo formulário de contato
- **Usuários & permissões** (só admin) — criar, editar, remover usuários

O painel inteiro foi revisado para funcionar bem no celular: abas com rolagem horizontal,
tabelas com scroll lateral (em vez de espremer as colunas), modais em tela cheia no mobile,
e o cabeçalho simplificado (esconde o e-mail em telas pequenas pra não ficar apertado).

### Sorteio Sobecc — como funciona

- Página pública `sorteio.html` (não está no menu principal do site — é uma campanha à parte,
  pensada pra ser acessada via link direto ou QR code no estande). Campos básicos: nome,
  e-mail, telefone/WhatsApp e instituição (opcional) — dá pra ajustar os campos depois
- Os cadastros vão para a coleção `sorteio_participantes` no Firestore
- No painel, o campo "Quantos ganhadores" permite sortear 1 ou vários de uma vez — o sorteio
  não repete quem já ganhou antes, a menos que você clique em "Zerar sorteio"
- Os ganhadores ficam marcados com o status "Ganhador" na tabela, e aparecem destacados no
  topo do painel até você zerar

### Catálogo — como funciona

- Cada produto é **um item genérico**: não existe campo fixo por tipo de produto — dá pra
  cadastrar qualquer coisa (equipamento, insumo, acessório) com os mesmos campos
- A "descrição completa" e as "especificações adicionais" só aparecem no pop-up que abre
  ao clicar no card — o card em si mostra só título, categoria e resumo curto
- O grid público mostra 4 produtos por linha (2 no mobile, 3 no tablet) e pagina de 8 em 8
- Assim como os artigos, a primeira vez que a consulta rodar no site publicado, o Firestore
  provavelmente vai pedir pra criar um **índice composto** (status + createdAt) — é só clicar
  no link que aparece no erro do console e criar, uma vez só
- `bulk-import-catalogo.html` — ferramenta à parte pra importar vários produtos de uma vez
  (feita a partir do catálogo em PDF); só funciona logado como admin/editor

## Arquivos de suporte

- `styles.css` — todos os estilos do site público
- `script.js` — atualiza o ano no rodapé + controla o menu hambúrguer do mobile
- `imagens/` — todas as imagens do site (ver "Estrutura de pastas" acima)
- `js/firebase-config.js` — configuração do Firebase (chaves do projeto `medcontrol-e07c2`)
- `firestore.rules` — regras de segurança (inclui `users`, `articles`, `leads` e `catalog`)
- `gen_site.py` — script Python que gera todas as páginas do site público (não inclui o

  `admin.html`, mantido à parte)

## Testar localmente

```bash
python3 -m http.server 8000
```

## Deploy no GitHub Pages

1. Subir todos os arquivos (exceto `gen_site.py`) na raiz do repo, branch `main`
2. Settings → Pages → Source: `main` / `/ (root)`
3. Publicar as regras atualizadas de `firestore.rules` no Firebase Console

## Editar conteúdo do site público

- Cada página é um arquivo `.html` independente
- Pra mudar header/footer/botão do WhatsApp em todas as páginas de uma vez: editar
  `gen_site.py` e rodar `python3 gen_site.py` de novo

## Pendências / observações

- **`imagens/sterifast.webp` ainda não existe** — a página de Produtos já referencia esse
  arquivo no bloco do Sistema Sterifast; é só colocar a imagem com esse nome exato dentro
  da pasta `imagens/` que ela aparece automaticamente, sem precisar mexer em código

- **Visualizador de catálogo (`catalogo.html`):** as páginas do PDF foram pré-renderizadas
  uma vez (em alta resolução, 1400×1923px) e salvas como WebP em `imagens/catalogo/`. O
  visualizador só carrega essas imagens prontas e usa a biblioteca **StPageFlip** (via CDN)
  pra cuidar da experiência de "livro". Isso ficou bem mais leve (~2,3MB pras 20 páginas, contra
  9MB do PDF original) e muito mais nítido do que renderizar o PDF ao vivo no navegador de cada
  visitante — que era o que causava a qualidade baixa na versão anterior.

  **Pra atualizar o catálogo** (trocar conteúdo/adicionar páginas), é preciso re-renderizar as
  imagens a partir do PDF novo. Um jeito simples, com Python + PyMuPDF:
  ```python
  import fitz  # pip install pymupdf
  doc = fitz.open("catalogo-medcontrol-novo.pdf")
  target_width = 1400
  zoom = target_width / doc[0].rect.width
  mat = fitz.Matrix(zoom, zoom)
  for i, page in enumerate(doc, start=1):
      pix = page.get_pixmap(matrix=mat, alpha=False)
      pix.pil_save(f"imagens/catalogo/pagina-{i:02d}.webp", format="WEBP", quality=82)
  ```
  Depois, se o número de páginas mudou, atualize `CATALOG_PAGE_COUNT` em `gen_site.py` (linha
  perto do `FLIPBOOK_SCRIPTS_TEMPLATE`) e rode `python3 gen_site.py` de novo. Se quiser, me
  manda o PDF novo que eu faço essa parte.

- `blog.html`/`artigo.html`/`catalogo.html` podem pedir criação de índice composto no
  Firestore na primeira consulta — normal, resolve uma vez só clicando no link do erro
- Placeholders `[logo]`, `[vídeo]`, `[mapa]` ainda pendentes de mídia real
