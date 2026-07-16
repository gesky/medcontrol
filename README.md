# MedControl — Landing Page (estático)

Site institucional em HTML/CSS/JS puro, sem build step, sem dependências.

## Arquivos

- `index.html` — todo o conteúdo e estrutura das seções
- `styles.css` — paleta monocromática (oklch), tipografia Montserrat, layout responsivo
- `script.js` — só atualiza o ano no rodapé (sem lógica de negócio)
- `favicon.ico`

## Testar localmente

Não precisa de servidor nem `npm install`. Só abrir `index.html` direto no navegador,
ou rodar um servidor simples se preferir ver com caminho relativo real:

```bash
python3 -m http.server 8000
# depois abra http://localhost:8000
```

## Deploy no GitHub Pages

1. Criar um repo novo (ex: `medcontrol-landing`)
2. Subir estes 4 arquivos na raiz (branch `main`)
3. Settings → Pages → Source: `main` / `/ (root)`
4. Apontar o domínio `medcontrolbauru.com.br` (ou subdomínio) via CNAME nas configurações de Pages, se for usar domínio próprio

## Editar

- **Textos:** direto no `index.html`, cada seção está comentada (`<!-- ===== NOME ===== -->`)
- **Cores/espaçamento:** tokens no topo do `styles.css` (`:root`), tudo em `oklch()` igual ao original
- **WhatsApp:** o número/link aparece repetido em vários CTAs — buscar por `wa.me/551432087108` pra trocar em todos de uma vez

## Painel administrativo de cursos (futuro)

Quando for desenvolver o painel, ele deve ser um projeto separado (app próprio,
com Firebase, seguindo o mesmo padrão do Muscle Memory/Ponte). A landing só
precisa de um link/botão apontando pra lá — não recomendado acoplar ao mesmo
projeto.
