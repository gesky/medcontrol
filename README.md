# MedControl — Site institucional (multi-página) + Painel administrativo

Site em HTML/CSS/JS puro, sem build step, sem dependências (exceto Firebase,
usado pelo painel administrativo e pelo formulário de contato).

## Páginas do site público

- `index.html` — Home (hero + resumo de cada seção, com links "saiba mais" pra página dedicada)
- `sobre.html` — Institucional (história + como trabalhamos + diferenciais, tudo em uma página só)
- `linhas.html` — Linhas de produto (com âncoras internas `#embalagens`, `#comodato`, `#indicadores`, `#suporte`)
- `depoimentos.html` — Depoimentos (5 depoimentos, cada um com placeholder de foto)
- `contato.html` — Contato (caixa de WhatsApp, redes sociais, endereço, mapa real do Google Maps,
  **formulário funcional** — grava lead direto no Firestore)
- `blog.html` — Listagem do blog (4 artigos placeholder, ainda estáticos)
- `blog-1.html` a `blog-4.html` — Artigos individuais estáticos, com navegação Anterior/Próximo

Menu (nesta ordem): **Linhas, Sobre, Depoimentos, Blog, Contato**.

## Painel administrativo (`admin.html`)

Painel com login (Firebase Authentication) para gerenciar:

- **Usuários & permissões** (só quem é `admin` vê essa aba) — criar, editar nome/permissão,
  remover. Duas permissões: `admin` (acesso total) e `editor` (edita conteúdo).
- **Mensagens** — leads recebidos pelo formulário da página Contato: nome, e-mail, telefone,
  assunto, mensagem. Suporta status (Novo/Lido/Contatado/Não responder), arquivar/restaurar,
  excluir, exportar CSV, contador de mensagens não lidas na aba, e paginação ("carregar mais")
  — mesma estrutura do painel do Plane Aviation.
- **Artigos** — criar, editar, arquivar/reativar e excluir artigos do blog, com capa,
  categoria, resumo, conteúdo e status (`rascunho` / `publicado` / `arquivado`).

### Formulário de contato → Mensagens no painel

A página `contato.html` está conectada ao Firestore: quando alguém preenche e envia o
formulário, a mensagem cai direto na coleção `leads` e aparece na aba **Mensagens** do
painel. Isso já está funcionando (não é mais ilustrativo) — só depende das chaves do
Firebase estarem certas em `js/firebase-config.js` e das regras em `firestore.rules`
estarem publicadas.

### Upload de capa dos artigos — agora em WebP

A capa dos artigos é convertida automaticamente para **WebP** antes de ser salva, tanto no
modo inline (Firestore) quanto no modo Storage — a mesma otimização que já usamos no Plane
Aviation. Se o navegador da pessoa não suportar exportação WebP (bem raro hoje em dia), o
painel cai automaticamente para JPEG sem quebrar nada.

### Como ativar

1. Crie um projeto em [console.firebase.google.com](https://console.firebase.google.com)
2. Ative **Authentication → método E-mail/senha**
3. Crie um **Firestore Database** (modo produção)
4. Cole as chaves do seu app web em `js/firebase-config.js` (tem instruções comentadas
   no topo do arquivo) — **já preenchido com as chaves do projeto `medcontrol-e07c2`**
5. Publique as regras de `firestore.rules` (Firebase Console → Firestore → Regras)
6. Crie o primeiro usuário admin manualmente:
   - Authentication → Adicionar usuário (e-mail + senha)
   - Firestore → coleção `users` → documento com **ID = UID** desse usuário →
     campos `{ name: "Seu nome", email: "seu@email.com", role: "admin" }`
7. Acesse `admin.html`, faça login — a partir daqui você já cria os próximos
   usuários direto pelo painel (aba Usuários & Permissões)

### Sobre upload de imagem (capa do artigo)

O Firebase Storage exige o plano pago (Blaze) do Firebase. Enquanto seu projeto
estiver no plano gratuito (Spark), o painel salva a capa do artigo (já convertida
pra WebP) direto no Firestore (`IMAGE_MODE: "inline"` em `js/firebase-config.js`).
Se e quando você migrar pro plano Blaze, troque para `IMAGE_MODE: "storage"` e as
capas WebP passam a subir pro Firebase Storage normalmente.

### Importante: o blog público ainda é estático

Por enquanto, os artigos criados no painel ficam salvos no Firestore (coleção
`articles`), mas `blog.html` e `blog-1.html`...`blog-4.html` continuam sendo
arquivos estáticos — não estão lendo do Firestore ainda. Quando você quiser,
dá pra conectar o `blog.html` pra buscar e listar os artigos publicados
direto do Firestore (as regras em `firestore.rules` já preveem essa leitura
pública). É só avisar quando quiser esse próximo passo.

## Arquivos de suporte

- `styles.css` — todos os estilos do site público (paleta, tipografia, componentes)
- `script.js` — só atualiza o ano no rodapé do site público
- `logo.svg` / `logo-branco.svg` — logos (colorido no header, branco no rodapé)
- `hero-nurse.png` / `hero-bg.jpg` — imagens do hero da home
- `js/firebase-config.js` — configuração do Firebase usada pelo `admin.html` e pelo
  formulário de `contato.html` (já preenchida com as chaves do projeto `medcontrol-e07c2`)
- `firestore.rules` — regras de segurança pra colar no Firebase Console
- `gen_site.py` — script Python que gera as páginas do site público (não inclui o admin.html,
  que é mantido à parte por ter estrutura própria)

## Testar localmente

```bash
python3 -m http.server 8000
# depois abra http://localhost:8000
```
O painel (`admin.html`) e o envio do formulário de contato só funcionam de verdade
depois que Authentication e Firestore estiverem ativados no Firebase Console.

## Deploy no GitHub Pages

1. Subir todos os arquivos (exceto `gen_site.py`) na raiz do repo, branch `main`
2. Settings → Pages → Source: `main` / `/ (root)`
3. **Atenção:** `admin.html` fica publicamente acessível (como qualquer página estática),
   mas só quem tiver login e permissão no Firestore consegue ver o conteúdo — a proteção
   real é a regra do Firestore, não a URL.

## Editar conteúdo do site público

- Cada página é um arquivo `.html` independente — edite direto nele
- Se precisar mudar o header, footer ou botão do WhatsApp em **todas** as páginas de uma vez,
  edite o `gen_site.py` e rode `python3 gen_site.py` de novo — ele regenera todos os HTMLs
  do site público (não mexe no `admin.html`)

## Pendências / observações

- `hero-nurse.png` está com 21MB — vale comprimir antes de subir pra produção
- Placeholders `[imagem]`, `[vídeo]`, `[logo]`, `[mapa]` — substituir por mídia real quando disponível
- O painel precisa das chaves do Firebase preenchidas em `js/firebase-config.js` pra funcionar
  (já estão preenchidas — falta só ativar Authentication + Firestore no console)
- O blog público ainda não lê os artigos do Firestore (ver seção acima)
