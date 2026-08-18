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
- `catalogo.html` — **Catálogo de produtos**, com duas partes:
  1. **Visualizador de PDF folheável** — renderiza `catalogo-medcontrol.pdf` página por
     página, com efeito de "livro" (arrastar com mouse/touch). Fundo branco na área do
     visualizador; o título/subtítulo no topo da página continuam com fundo azul. Pra
     atualizar o catálogo, basta substituir o arquivo `catalogo-medcontrol.pdf` por uma
     versão nova, com o mesmo nome
  2. **Grid de produtos em destaque**, dinâmico via Firestore (coleção `catalog`), pra produtos
     que você quiser cadastrar individualmente com ficha própria (pop-up com descrição completa),
     4 por linha / 8 por página, com paginação (Anterior/Próxima)
- `sobre.html` — Institucional (história + como trabalhamos + diferenciais)
- `linhas.html` — Produtos (5 linhas, nesta ordem: Equipamentos em comodato → Sistema
  Sterifast → Embalagens para esterilização → Indicadores e controle de processo →
  Suporte técnico e capacitação). O card "Catálogo completo" no fim da página leva
  direto para `catalogo.html`
- `phm-medcontrol.html` — Página dedicada ao PHM MedControl
- `contato.html` — Contato (formulário funcional, grava lead no Firestore)
- `blog.html` — Listagem do blog, dinâmica (Firestore)
- `artigo.html` — Template dinâmico de artigo (`?id=`)

Menu (nesta ordem): **Catálogo, Produtos, Sobre, Blog, Contato**.

A página e a seção de **Depoimentos foram removidas** do site (não existe mais
`depoimentos.html`, nem no menu, nem no rodapé, nem teaser na home).

### Header

- **Desktop:** logo + menu horizontal + botão "Falar com Especialista" (WhatsApp)
- **Mobile:** logo + botão hambúrguer (o botão de WhatsApp fica escondido no header
  mobile pra não brigar de espaço com o menu). Ao abrir o menu, aparecem os links de
  navegação + um botão "Falar no WhatsApp" no final

### Hero da home

Botão principal do hero agora é **"Conheça nossos produtos"**, levando para `linhas.html`
(antes ia direto pro WhatsApp).

## Painel administrativo (`admin.html`)

Abas:

- **Artigos** — publicar, editar, arquivar, excluir artigos do blog
- **Catálogo** — cadastrar, editar, arquivar, excluir produtos do catálogo público.
  Campos: título, categoria, resumo curto (card), descrição completa (pop-up), especificações
  adicionais (texto livre, um item por linha no formato `Campo: valor`), imagem (convertida
  automaticamente para WebP, mesmo pipeline dos artigos), e status (rascunho/publicado/arquivado)
- **Mensagens** — leads recebidos pelo formulário de contato
- **Usuários & permissões** (só admin) — criar, editar, remover usuários

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

- **Visualizador de PDF (`catalogo.html`):** usa PDF.js pra converter cada página do PDF em
  imagem, e a biblioteca **StPageFlip** pra cuidar da experiência de "livro" (arrastar o canto
  da página com mouse/touch, dobra realista, responsivo). Ambas via CDN (jsDelivr) — funciona
  offline localmente também, mas depende de internet quando publicado (o que já é o caso de tudo
  que usa Firebase). O PDF (`catalogo-medcontrol.pdf`) tem ~9MB — carrega uma vez por visita e
  fica em cache do navegador depois. Pra atualizar o catálogo, basta subir um novo arquivo com
  esse mesmo nome por cima do atual no repositório.

- A linha "Sistema Sterifast" ainda está com placeholder `[imagem]` — quando tiver a
  imagem real, é só me mandar que eu aplico do mesmo jeito que as outras
- `blog.html`/`artigo.html`/`catalogo.html` podem pedir criação de índice composto no
  Firestore na primeira consulta — normal, resolve uma vez só clicando no link do erro
- Placeholders `[logo]`, `[vídeo]`, `[mapa]` ainda pendentes de mídia real
