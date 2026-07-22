# -*- coding: utf-8 -*-
"""
Gerador de páginas do site MedControl.
Monta cada página HTML a partir de componentes compartilhados (head, header,
footer, botão flutuante do WhatsApp) + conteúdo específico de cada página.
Rodar com: python3 gen_site.py
"""
import os

WA_LINK = "https://wa.me/551432087108?text=Ol%C3%A1%2C%20gostaria%20de%20falar%20com%20um%20especialista%20MedControl."

NAV_ITEMS = [
    ("linhas.html", "Produtos"),
    ("sobre.html", "Sobre"),
    ("depoimentos.html", "Depoimentos"),
    ("blog.html", "Blog"),
    ("contato.html", "Contato"),
]

WHATSAPP_ICON = '''<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M20.52 3.48A11.86 11.86 0 0 0 12.06 0C5.5 0 .18 5.32.18 11.88c0 2.09.55 4.13 1.6 5.93L0 24l6.34-1.66a11.86 11.86 0 0 0 5.72 1.46h.01c6.56 0 11.88-5.32 11.88-11.88 0-3.17-1.24-6.15-3.43-8.44ZM12.07 21.5h-.01a9.55 9.55 0 0 1-4.87-1.33l-.35-.21-3.76.98 1-3.66-.23-.38a9.5 9.5 0 0 1-1.46-5.02c0-5.26 4.29-9.54 9.55-9.54 2.55 0 4.94.99 6.74 2.79a9.47 9.47 0 0 1 2.79 6.75c0 5.26-4.28 9.62-9.4 9.62Zm5.44-7.15c-.3-.15-1.77-.87-2.05-.97-.28-.1-.48-.15-.68.15-.2.3-.78.97-.96 1.17-.18.2-.35.22-.65.07-.3-.15-1.27-.47-2.42-1.5-.9-.8-1.5-1.79-1.68-2.09-.18-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.07-.15-.68-1.65-.93-2.26-.25-.6-.5-.52-.68-.53l-.58-.01c-.2 0-.52.07-.79.37-.27.3-1.03 1-1.03 2.45s1.06 2.85 1.21 3.05c.15.2 2.09 3.2 5.06 4.49.71.31 1.26.49 1.7.63.72.23 1.37.2 1.88.12.57-.09 1.77-.72 2.02-1.42.25-.7.25-1.29.17-1.42-.07-.13-.27-.2-.57-.35Z"/></svg>'''

WHATSAPP_ICON_FILLED = WHATSAPP_ICON.replace('<svg aria-hidden="true" viewBox="0 0 24 24">', '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true">').replace('<path d=', '<path fill="currentColor" d=')


def head(title, description, og_title=None, og_description=None):
    og_title = og_title or title
    og_description = og_description or description
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="author" content="MedControl" />

  <meta property="og:title" content="{og_title}" />
  <meta property="og:description" content="{og_description}" />
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="pt_BR" />
  <meta name="twitter:card" content="summary_large_image" />

  <link rel="icon" href="favicon.ico" type="image/x-icon" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap" />

  <link rel="stylesheet" href="styles.css" />
</head>
<body>
'''


def header(active=None):
    links = []
    for href, label in NAV_ITEMS:
        current = ' aria-current="page"' if href == active else ''
        links.append(f'        <a href="{href}"{current}>{label}</a>')
    nav = "\n".join(links)
    return f'''  <!-- ===================== HEADER / NAV ===================== -->
  <header class="site-header">
    <div class="container">
      <a href="index.html" aria-label="MedControl">
        <img src="logo.svg" alt="MedControl" class="logo-img" />
      </a>
      <nav class="nav-links">
{nav}
      </nav>
      <a href="{WA_LINK}"
         target="_blank" rel="noopener noreferrer" class="btn btn-accent">
        WhatsApp
      </a>
    </div>
  </header>

  <main>
'''


def page_banner(eyebrow, title_html, lead, current_label, parent_crumb=None):
    if parent_crumb:
        parent_label, parent_href = parent_crumb
        crumb = f'''<a href="index.html">Início</a>
          <span aria-hidden="true">/</span>
          <a href="{parent_href}">{parent_label}</a>
          <span aria-hidden="true">/</span>
          <span>{current_label}</span>'''
    else:
        crumb = f'''<a href="index.html">Início</a>
          <span aria-hidden="true">/</span>
          <span>{current_label}</span>'''
    return f'''    <!-- ===================== BANNER DA PÁGINA ===================== -->
    <section class="page-banner">
      <div class="container">
        <div class="breadcrumb">
          {crumb}
        </div>
        <span class="eyebrow">{eyebrow}</span>
        <h1>{title_html}</h1>
        <p class="lead">{lead}</p>
      </div>
    </section>
'''


def whatsapp_float(extra_scripts=""):
    return f'''  <!-- ===================== WHATSAPP FLOATING BUTTON ===================== -->
  <a href="{WA_LINK}"
     target="_blank" rel="noopener noreferrer" aria-label="Falar no WhatsApp com a MedControl" class="whatsapp-float">
    {WHATSAPP_ICON}
    <span class="whatsapp-float-text">Fale com um especialista</span>
  </a>

  <script src="script.js"></script>
{extra_scripts}</body>
</html>
'''


CONTACT_FORM_SCRIPTS = '''
  <!-- Firebase — envio do formulário de contato como lead pro painel administrativo -->
  <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore-compat.js"></script>
  <script src="js/firebase-config.js"></script>
  <script>
  (function () {
    const form = document.getElementById("contactForm");
    const msgEl = document.getElementById("contactFormMsg");
    const btn = document.getElementById("contactFormSubmit");
    if (!form) return;

    function showMsg(text, type) {
      msgEl.textContent = text;
      msgEl.className = "msg show " + type;
    }

    form.addEventListener("submit", async function (e) {
      e.preventDefault();

      if (!window.MC || !MC.configured || !MC.db) {
        showMsg("Formulário indisponível no momento. Fale com a gente pelo WhatsApp.", "err");
        return;
      }

      const name = document.getElementById("name").value.trim();
      const email = document.getElementById("email").value.trim();
      const phone = document.getElementById("phone").value.trim();
      const subjectSelect = document.getElementById("subject");
      const subjectLabel = subjectSelect.options[subjectSelect.selectedIndex]
        ? subjectSelect.options[subjectSelect.selectedIndex].text
        : "";
      const message = document.getElementById("message").value.trim();

      if (!name || !email || !message) {
        showMsg("Preencha nome, e-mail e mensagem antes de enviar.", "err");
        return;
      }

      btn.disabled = true;
      const originalText = btn.innerHTML;
      btn.innerHTML = "Enviando...";

      try {
        await MC.db.collection("leads").add({
          name: name,
          email: email,
          phone: phone,
          subject: subjectLabel,
          message: message,
          status: "novo",
          archived: false,
          source: "contato.html",
          createdAt: firebase.firestore.FieldValue.serverTimestamp(),
        });
        showMsg("Mensagem enviada com sucesso! Em breve nossa equipe entra em contato.", "ok");
        form.reset();
      } catch (err) {
        showMsg("Não foi possível enviar agora. Tente novamente ou fale pelo WhatsApp.", "err");
      } finally {
        btn.disabled = false;
        btn.innerHTML = originalText;
      }
    });
  })();
  </script>
'''


def footer():
    return f'''  <!-- ===================== FOOTER ===================== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" aria-label="MedControl">
            <img src="logo-branco.svg" alt="MedControl" class="footer-logo-img" />
          </a>
          <p>Há mais de 39 anos, parceira técnica de hospitais e clínicas brasileiras em esterilização, segurança e controle de infecção. Comprometimento em cada processo.</p>
          <div class="social-icons">
            <a href="https://www.instagram.com/medcontrol.bauru/" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
            </a>
            <a href="https://www.facebook.com/medcontrolbauru" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
            </a>
            <a href="https://www.linkedin.com/company/medcontrol/posts/?feedView=all" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
            </a>
            <a href="{WA_LINK}"
               target="_blank" rel="noopener noreferrer" aria-label="WhatsApp">
              {WHATSAPP_ICON_FILLED}
            </a>
          </div>
        </div>

        <div class="footer-nav">
          <h3>Navegação</h3>
          <ul>
            <li><a href="index.html">Início</a></li>
            <li><a href="sobre.html">Sobre</a></li>
            <li><a href="linhas.html">Produtos</a></li>
            <li><a href="depoimentos.html">Depoimentos</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li><a href="contato.html">Contato</a></li>
          </ul>
        </div>

        <div class="footer-lines">
          <h3>Produtos</h3>
          <ul>
            <li><a href="phm-medcontrol.html">Equipamentos em comodato</a></li>
            <li><a href="linhas.html#embalagens">Embalagens para esterilização</a></li>
            <li><a href="linhas.html#indicadores">Indicadores e controle de processo</a></li>
            <li><a href="linhas.html#suporte">Suporte técnico e capacitação</a></li>
          </ul>
        </div>

        <div class="footer-contact">
          <h3>Contato</h3>
          <ul>
            <li>Rua Jacy Stevaux Vilaça, 2-66<br />Jardim Contorno — Bauru / SP<br />CEP 17047-250</li>
            <li><a href="tel:+551432087108">(14) 3208-7108</a></li>
            <li><a href="mailto:contato@medcontrolbauru.com.br">contato@medcontrolbauru.com.br</a></li>
            <li>Segunda a sexta · 08h às 17h</li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div id="copyright"></div>
        <div class="footer-bottom-links">
          <a href="#">Política de privacidade</a>
          <a href="#">Termos de uso</a>
        </div>
      </div>
    </div>
  </footer>

'''


def write_page(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {filename}")


LOREM = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.",
    "Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet.",
    "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident.",
]

print("Gerando páginas...")

# =============================================================================
# HOME (index.html) — hero + teasers de cada página, com links "saiba mais"
# =============================================================================

home_body = f'''    <!-- ===================== HERO ===================== -->
    <section id="top" class="hero">
      <div class="container">
        <div class="hero-main">
          <h1><span class="hero-title-regular">A segurança de uma operação</span> <span class="accent-word">começa muito antes!</span></h1>
          <p class="lead">
            Há mais de 39 anos ao lado de hospitais e clínicas brasileiras, com insumos certificados,
            equipamentos em comodato e suporte técnico que não some depois da entrega.
          </p>
          <div class="hero-ctas">
            <a href="{WA_LINK}"
               target="_blank" rel="noopener noreferrer" class="btn btn-accent-lg">
              Falar com um especialista <span aria-hidden="true">→</span>
            </a>
          </div>
        </div>
        <div class="hero-media">
          <img src="hero-nurse.webp" alt="Profissional de saúde MedControl" class="hero-nurse" />
        </div>
      </div>
    </section>

    <!-- ===================== SOCIAL PROOF ===================== -->
    <section aria-label="Instituições atendidas" class="social-proof">
      <div class="container">
        <p>Parceira técnica de hospitais, clínicas e centros cirúrgicos em todo o Brasil</p>
        <div class="logo-grid">
          <div>[logo]</div>
          <div>[logo]</div>
          <div>[logo]</div>
          <div>[logo]</div>
          <div>[logo]</div>
          <div>[logo]</div>
        </div>
      </div>
    </section>

    <!-- ===================== ABOUT (teaser) ===================== -->
    <section class="about">
      <div class="container section-inner">
        <div class="about-media">
          <div class="media-placeholder">[imagem]</div>
        </div>
        <div class="about-copy">
          <span class="eyebrow">Institucional</span>
          <h2>Mais de 39 anos presentes onde a segurança começa.</h2>
          <p style="margin-top:1.5rem;">
            A MedControl é uma empresa brasileira dedicada à esterilização e à prevenção de
            contaminação em ambientes de saúde. Além do produto, oferecemos suporte técnico
            contínuo, treinamento de equipes e acompanhamento presencial — como parceiros
            consultivos de cada CME que atendemos.
          </p>
          <a href="sobre.html" class="product-card-cta" style="color:var(--blue);">Conheça a MedControl <span aria-hidden="true">→</span></a>
        </div>
      </div>
    </section>

    <!-- ===================== PRODUCT LINES (teaser) ===================== -->
    <section class="product-lines">
      <div class="container section-inner">
        <div class="product-lines-head">
          <div style="max-width:42rem;">
            <span class="eyebrow">Produtos</span>
            <h2>Tudo que sua central de esterilização precisa. Em um só lugar.</h2>
          </div>
          <a href="linhas.html" class="btn btn-outline-white">
            Ver todos os produtos <span aria-hidden="true">→</span>
          </a>
        </div>

        <div class="product-grid">
          <article class="product-card">
            <div class="product-card-top"><span>01</span><span>Linha</span></div>
            <h3>Equipamentos em comodato</h3>
            <p>Autoclaves, seladoras, lavadoras termodesinfectoras e esterilizadores a plasma — tecnologia de ponta sem alto investimento inicial.</p>
            <a href="phm-medcontrol.html" class="product-card-cta">Saiba mais <span aria-hidden="true">→</span></a>
          </article>
          <article class="product-card">
            <div class="product-card-top"><span>02</span><span>Linha</span></div>
            <h3>Embalagens para esterilização</h3>
            <p>Papel grau cirúrgico, bobinas tubulares e envelopes com resistência mecânica validada, em conformidade com ANVISA e normas internacionais.</p>
            <a href="linhas.html#embalagens" class="product-card-cta">Saiba mais <span aria-hidden="true">→</span></a>
          </article>
          <article class="product-card">
            <div class="product-card-top"><span>03</span><span>Linha</span></div>
            <h3>Indicadores e controle de processo</h3>
            <p>Indicadores biológicos, químicos e integradores Tipo 5 que validam cada parâmetro do ciclo, com rastreabilidade auditável.</p>
            <a href="linhas.html#indicadores" class="product-card-cta">Saiba mais <span aria-hidden="true">→</span></a>
          </article>
          <article class="product-card">
            <div class="product-card-top"><span>04</span><span>Linha</span></div>
            <h3>Suporte técnico e capacitação</h3>
            <p>Atendimento consultivo presencial, validação de processos e o programa CME Masterclass by MedControl.</p>
            <a href="linhas.html#suporte" class="product-card-cta">Saiba mais <span aria-hidden="true">→</span></a>
          </article>
        </div>
      </div>
    </section>

    <!-- ===================== DIFERENCIAIS (teaser) ===================== -->
    <section class="differentials">
      <div class="container section-inner">
        <div class="differentials-head">
          <span class="eyebrow">Diferenciais</span>
          <h2>Por que hospitais escolhem — e permanecem com — a MedControl.</h2>
        </div>
        <div class="differentials-grid">
          <div class="differential-card">
            <div class="n">+39</div>
            <p class="label">anos dedicados à segurança hospitalar</p>
            <p class="body">Uma trajetória construída ciclo a ciclo, ao lado das centrais de esterilização que não aceitam improvisar.</p>
          </div>
          <div class="differential-card">
            <div class="n">100%</div>
            <p class="label">conforme normas técnicas</p>
            <p class="body">Produtos e processos alinhados às exigências da ANVISA, RDC 15 e padrões internacionais.</p>
          </div>
          <div class="differential-card">
            <div class="n">0</div>
            <p class="label">abandonos após a venda</p>
            <p class="body">Suporte técnico presente e um consultor que conhece a realidade do seu CME de dentro pra fora.</p>
          </div>
          <div class="differential-card">
            <div class="n">24h</div>
            <p class="label">para cotação e retorno técnico</p>
            <p class="body">Envie sua demanda pelo WhatsApp e receba, no mesmo dia útil, cotação e recomendação técnica.</p>
          </div>
        </div>
        <a href="sobre.html#diferenciais" class="product-card-cta" style="color:var(--blue); margin-top:2.5rem;">Ver todos os diferenciais <span aria-hidden="true">→</span></a>
      </div>
    </section>

    <!-- ===================== DEPOIMENTOS (teaser) ===================== -->
    <section class="testimonials">
      <div class="container section-inner">
        <div class="testimonials-head">
          <span class="eyebrow">Depoimentos</span>
          <h2>A voz de quem opera uma central de esterilização todos os dias.</h2>
        </div>
        <div class="testimonials-grid">
          <figure class="testimonial-card">
            <div class="testimonial-media">
              <div class="media-placeholder">[imagem]</div>
            </div>
            <div class="testimonial-body">
              <blockquote>A MedControl não entrega só produto — entrega segurança. O suporte técnico que recebemos mudou o nível de confiança da nossa equipe em cada ciclo. É o tipo de parceria que a gente não troca.</blockquote>
              <figcaption>
                <div class="author">Enfermeira responsável, CME</div>
                <div class="org">Hospital de médio porte — Interior de SP</div>
              </figcaption>
            </div>
          </figure>
        </div>
        <a href="depoimentos.html" class="product-card-cta" style="color:var(--blue); margin-top:2.5rem;">Ver todos os depoimentos <span aria-hidden="true">→</span></a>
      </div>
    </section>

    <!-- ===================== VÍDEO INSTITUCIONAL ===================== -->
    <section class="video-section">
      <div class="container section-inner">
        <span class="eyebrow">Conheça a MedControl</span>
        <h2>Por que hospitais que não podem errar escolhem a MedControl.</h2>
        <div class="media-placeholder">[vídeo]</div>
      </div>
    </section>

    <!-- ===================== FINAL CTA ===================== -->
    <section class="final-cta">
      <div class="container section-inner">
        <div class="final-cta-main">
          <span class="eyebrow">Contato comercial</span>
          <h2>Sua CME merece um parceiro que conhece ela de dentro pra fora.</h2>
          <p class="lead">
            Fale com um especialista MedControl pelo WhatsApp e receba, no mesmo dia útil,
            cotação e recomendação técnica personalizada para o seu hospital ou clínica.
          </p>
          <div class="hero-ctas">
            <a href="{WA_LINK}"
               target="_blank" rel="noopener noreferrer" class="btn btn-white">
              Iniciar conversa no WhatsApp <span aria-hidden="true">→</span>
            </a>
            <a href="contato.html" class="btn btn-outline-white">Ver todos os contatos</a>
          </div>
        </div>
        <dl class="final-cta-info">
          <div>
            <dt>Endereço</dt>
            <dd>Rua Jacy Stevaux Vilaça, 2-66<br />Jardim Contorno — Bauru / SP<br />CEP 17047-250</dd>
          </div>
          <div>
            <dt>Atendimento</dt>
            <dd>Segunda a sexta · 08h às 17h</dd>
          </div>
          <div>
            <dt>Cobertura</dt>
            <dd>Todo o território nacional</dd>
          </div>
        </dl>
      </div>
    </section>
  </main>

'''

page = (
    head(
        "MedControl — Parceira Técnica em Esterilização Hospitalar | Bauru/SP",
        "Há mais de 39 anos ao lado de hospitais e clínicas brasileiras. Insumos, equipamentos em comodato e suporte técnico contínuo para centrais de esterilização. Fale com um especialista.",
        "MedControl — Parceira Técnica em Esterilização Hospitalar",
        "Insumos certificados, equipamentos em comodato e consultoria técnica para CME hospitalar. Segurança e parceria em cada processo.",
    )
    + header(active=None)
    + home_body
    + footer()
    + whatsapp_float()
)
write_page("index.html", page)

# =============================================================================
# QUEM SOMOS (fusão de Sobre + Diferenciais)
# =============================================================================

quem_somos_body = f'''{page_banner(
    "Institucional",
    "Mais de 39 anos ao lado de quem cuida da segurança hospitalar.",
    "A MedControl nasceu para ser mais do que uma fornecedora — uma parceira técnica presente em cada etapa do processo de esterilização, do primeiro pedido ao suporte contínuo.",
    "Sobre",
)}
    <!-- ===================== NOSSA HISTÓRIA ===================== -->
    <section class="about">
      <div class="container section-inner">
        <div class="about-media">
          <div class="media-placeholder">[imagem]</div>
        </div>
        <div class="about-copy">
          <span class="eyebrow">Nossa história</span>
          <h2>Construída ciclo a ciclo, ao lado de quem não pode errar.</h2>
          <p style="margin-top:1.5rem;">
            A MedControl é uma empresa brasileira dedicada exclusivamente ao universo da
            esterilização e da prevenção ao risco de contaminação em ambientes de saúde. Ao
            longo de mais de 39 anos, construímos essa trajetória junto de enfermeiros
            responsáveis, coordenações de CME e gestores hospitalares que confiaram na gente
            para operar com precisão, todos os dias.
          </p>
          <p>
            Aqui, a venda é só o começo. Oferecemos suporte técnico contínuo, treinamento de
            equipes e acompanhamento presencial da operação — porque entendemos que segurança
            hospitalar não se sustenta com produto. Se sustenta com quem está ao seu lado
            quando algo falha.
          </p>
        </div>
      </div>
    </section>

    <!-- ===================== COMO TRABALHAMOS ===================== -->
    <section class="differentials">
      <div class="container section-inner">
        <div class="differentials-head">
          <span class="eyebrow">Como trabalhamos</span>
          <h2>Parceria consultiva, não relação de fornecedor.</h2>
        </div>
        <div class="differentials-grid">
          <div class="differential-card">
            <p class="label">Mapeamento de processos</p>
            <p class="body">Entendemos a realidade da sua central antes de recomendar qualquer produto ou equipamento.</p>
          </div>
          <div class="differential-card">
            <p class="label">Protocolos orientados</p>
            <p class="body">Ajudamos a documentar e padronizar rotinas, reduzindo variação e retrabalho da equipe.</p>
          </div>
          <div class="differential-card">
            <p class="label">Acompanhamento presencial</p>
            <p class="body">Nossos consultores vão até o hospital — a distância nunca foi motivo pra ausência.</p>
          </div>
          <div class="differential-card">
            <p class="label">Capacitação contínua</p>
            <p class="body">Treinamos as equipes com o programa CME Masterclass, elevando o padrão técnico do time.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================== DIFERENCIAIS (resumido) ===================== -->
    <section id="diferenciais">
      <div class="container section-inner">
        <div class="differentials-head">
          <span class="eyebrow">Diferenciais</span>
          <h2>Por que hospitais escolhem — e permanecem com — a MedControl.</h2>
        </div>
        <div class="differentials-grid">
          <div class="differential-card">
            <div class="n">+39</div>
            <p class="label">anos de trajetória</p>
            <p class="body">Ao lado das centrais de esterilização que não aceitam improvisar.</p>
          </div>
          <div class="differential-card">
            <div class="n">100%</div>
            <p class="label">conforme normas técnicas</p>
            <p class="body">Alinhados às exigências da ANVISA, RDC 15 e padrões internacionais.</p>
          </div>
          <div class="differential-card">
            <div class="n">0</div>
            <p class="label">abandonos após a venda</p>
            <p class="body">Suporte técnico presente e consultor que conhece seu CME de dentro pra fora.</p>
          </div>
          <div class="differential-card">
            <div class="n">24h</div>
            <p class="label">para retorno técnico</p>
            <p class="body">Cotação e recomendação técnica no mesmo dia útil, pelo WhatsApp.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================== CTA ===================== -->
    <section class="final-cta">
      <div class="container section-inner">
        <div class="final-cta-main">
          <span class="eyebrow">Vamos conversar?</span>
          <h2>Conheça de perto como podemos apoiar sua central de esterilização.</h2>
          <p class="lead">
            Fale com um especialista MedControl e entenda, na prática, como funciona nossa
            parceria técnica.
          </p>
          <div class="hero-ctas">
            <a href="{WA_LINK}"
               target="_blank" rel="noopener noreferrer" class="btn btn-white">
              Falar com um especialista <span aria-hidden="true">→</span>
            </a>
          </div>
        </div>
      </div>
    </section>
  </main>

'''

page = (
    head(
        "Sobre — MedControl | Parceira Técnica em Esterilização Hospitalar",
        "Conheça a história e os diferenciais da MedControl: mais de 39 anos ao lado de hospitais e clínicas brasileiras, com suporte técnico contínuo e acompanhamento presencial.",
    )
    + header(active="sobre.html")
    + quem_somos_body
    + footer()
    + whatsapp_float()
)
write_page("sobre.html", page)

# =============================================================================
# LINHAS DE PRODUTO
# =============================================================================

linhas_body = f'''{page_banner(
    "Linhas de produto",
    "Tudo que sua central de esterilização precisa. Em um só lugar.",
    "Da embalagem ao equipamento, do indicador ao suporte técnico — um portfólio pensado para cobrir cada etapa do ciclo de esterilização, com curadoria técnica em cada item.",
    "Produtos",
)}
    <!-- ===================== LINHAS DETALHADAS ===================== -->
    <section>
      <div class="container section-inner">
        <div class="lines-list">

          <div class="line-block" id="comodato">
            <div class="line-media">
              <div class="media-placeholder">[imagem]</div>
            </div>
            <div class="line-copy">
              <span class="line-number">01 · Linha</span>
              <h2>Equipamentos em comodato</h2>
              <p>
                Autoclaves, seladoras, lavadoras termodesinfectoras e esterilizadores a plasma
                disponíveis em comodato — tecnologia de ponta sem alto investimento inicial,
                com manutenção inclusa e custo previsível para sua gestão. Ideal para hospitais
                que precisam modernizar a central sem comprometer o orçamento anual.
              </p>
              <a href="phm-medcontrol.html" class="btn btn-outline-blue">
                Saiba mais <span aria-hidden="true">→</span>
              </a>
            </div>
          </div>

          <div class="line-block" id="embalagens">
            <div class="line-media">
              <div class="media-placeholder">[imagem]</div>
            </div>
            <div class="line-copy">
              <span class="line-number">02 · Linha</span>
              <h2>Embalagens para esterilização</h2>
              <p>
                Papel grau cirúrgico, bobinas tubulares e envelopes com resistência mecânica
                validada — garantindo a barreira estéril do início ao fim do ciclo, em
                conformidade com a ANVISA e normas internacionais. Selecionamos cada material
                testando resistência a furos, selagem e armazenamento, para que a barreira
                estéril chegue intacta até o centro cirúrgico.
              </p>
              <a href="{WA_LINK}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-blue">
                Falar com um especialista <span aria-hidden="true">→</span>
              </a>
            </div>
          </div>

          <div class="line-block" id="indicadores">
            <div class="line-media">
              <div class="media-placeholder">[imagem]</div>
            </div>
            <div class="line-copy">
              <span class="line-number">03 · Linha</span>
              <h2>Indicadores e controle de processo</h2>
              <p>
                Indicadores biológicos, químicos e integradores Tipo 5 que validam cada
                parâmetro do ciclo — garantindo certeza técnica, rastreabilidade e
                documentação auditável para a sua CME. Cada lote é acompanhado de laudo
                técnico, facilitando auditorias e visitas de vigilância sanitária.
              </p>
              <a href="{WA_LINK}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-blue">
                Falar com um especialista <span aria-hidden="true">→</span>
              </a>
            </div>
          </div>

          <div class="line-block" id="suporte">
            <div class="line-media">
              <div class="media-placeholder">[imagem]</div>
            </div>
            <div class="line-copy">
              <span class="line-number">04 · Linha</span>
              <h2>Suporte técnico e capacitação</h2>
              <p>
                Atendimento consultivo presencial, validação de processos, treinamento de
                equipes e o programa de capacitação CME Masterclass by MedControl — porque
                parceria de verdade vai muito além da entrega do produto. Formamos equipes
                mais seguras, com menos retrabalho e mais autonomia técnica no dia a dia.
              </p>
              <a href="{WA_LINK}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-blue">
                Falar com um especialista <span aria-hidden="true">→</span>
              </a>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ===================== CTA CATÁLOGO ===================== -->
    <section class="final-cta">
      <div class="container section-inner">
        <div class="final-cta-main">
          <span class="eyebrow">Catálogo completo</span>
          <h2>Quer conhecer o portfólio completo da MedControl?</h2>
          <p class="lead">
            Solicite o catálogo pelo WhatsApp e receba, no mesmo dia útil, a lista completa de
            produtos com ficha técnica de cada item.
          </p>
          <div class="hero-ctas">
            <a href="{WA_LINK}"
               target="_blank" rel="noopener noreferrer" class="btn btn-white">
              Solicitar catálogo <span aria-hidden="true">→</span>
            </a>
          </div>
        </div>
      </div>
    </section>
  </main>

'''

page = (
    head(
        "Linhas de Produto MedControl — Embalagens, Equipamentos e Indicadores",
        "Conheça as linhas de produto da MedControl: embalagens para esterilização, equipamentos em comodato, indicadores de controle de processo e suporte técnico especializado.",
    )
    + header(active="linhas.html")
    + linhas_body
    + footer()
    + whatsapp_float()
)
write_page("linhas.html", page)

# =============================================================================
# PHM MEDCONTROL — página de produto (Equipamentos em comodato)
# =============================================================================

phm_body = f'''{page_banner(
    "Equipamentos em comodato",
    "PHM MedControl",
    "Esterilizador a plasma por peróxido de hidrogênio vaporizado em baixa temperatura — tecnologia de ponta para preservar instrumentos termossensíveis, com ciclos rápidos e sem resíduos tóxicos.",
    "PHM MedControl",
    parent_crumb=("Produtos", "linhas.html"),
)}
    <!-- ===================== O QUE É ===================== -->
    <section class="phm-intro">
      <div class="container section-inner">
        <div class="media-placeholder">[imagem]</div>
        <div class="phm-intro-copy">
          <span class="eyebrow">O que é o PHM</span>
          <h2>Esterilização a plasma, sem abrir mão da segurança.</h2>
          <p>
            O peróxido de hidrogênio, popularmente conhecido como água oxigenada, é um potente
            agente esterilizante utilizado em ambientes hospitalares. O PHM MedControl aplica
            essa tecnologia através da Esterilização por Plasma de Peróxido de Hidrogênio (EPPH):
            o peróxido, em concentração de aproximadamente 59%, recebe um campo eletromagnético
            por radiofrequência que gera uma nuvem de partículas altamente ionizadas — reativas o
            suficiente para eliminar a maioria das moléculas essenciais ao metabolismo de células
            vivas, sem danificar materiais termossensíveis.
          </p>
        </div>
      </div>
    </section>

    <!-- ===================== COMO FUNCIONA ===================== -->
    <section style="background-color:var(--gray-light);">
      <div class="container section-inner">
        <span class="eyebrow">Como funciona</span>
        <h2>O ciclo de esterilização em 5 fases.</h2>
        <div class="phm-steps">
          <div class="phm-step">
            <div class="n">1</div>
            <div class="t">Vácuo</div>
            <p>Obtido pela ação da bomba de vácuo.</p>
          </div>
          <div class="phm-step">
            <div class="n">2</div>
            <div class="t">Injeção</div>
            <p>O peróxido de hidrogênio é injetado na câmara em forma de vapor.</p>
          </div>
          <div class="phm-step">
            <div class="n">3</div>
            <div class="t">Difusão</div>
            <p>O vapor de peróxido se difunde por toda a câmara e materiais.</p>
          </div>
          <div class="phm-step">
            <div class="n">4</div>
            <div class="t">Plasma</div>
            <p>Formação do plasma através do uso de radiofrequência.</p>
          </div>
          <div class="phm-step">
            <div class="n">5</div>
            <div class="t">Ventilação</div>
            <p>Interrompe o plasma e injeta ar na câmara, retornando à pressão atmosférica.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================== MATERIAIS ===================== -->
    <section>
      <div class="container section-inner">
        <span class="eyebrow">Compatibilidade</span>
        <h2>Materiais compatíveis e incompatíveis.</h2>
        <div class="phm-materials" style="margin-top:2.5rem;">
          <div class="phm-materials-card ok">
            <h3>Pode ser esterilizado com peróxido de hidrogênio</h3>
            <ul>
              <li>Aço inoxidável</li>
              <li>Plásticos</li>
              <li>Vidros</li>
              <li>Borrachas</li>
              <li>Acrílicos</li>
              <li>Alumínio</li>
              <li>Bronze</li>
              <li>Látex</li>
              <li>PVC</li>
              <li>Silicone</li>
              <li>Teflon</li>
              <li>Fibras ópticas</li>
              <li>Materiais elétricos</li>
            </ul>
          </div>
          <div class="phm-materials-card no">
            <h3>Não deve ser esterilizado por esse método</h3>
            <ul>
              <li>Celulose</li>
              <li>Ferro</li>
              <li>Líquidos</li>
              <li>Materiais à base de papel</li>
              <li>Tecidos</li>
              <li>Lumens longos e estreitos (fundo cego)</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================== PARÂMETROS ===================== -->
    <section style="background-color:var(--gray-light);">
      <div class="container section-inner">
        <span class="eyebrow">Controle de processo</span>
        <h2>5 parâmetros críticos, monitorados em cada ciclo.</h2>
        <div class="differentials-grid" style="margin-top:2.5rem;">
          <div class="differential-card">
            <p class="label">Temperatura</p>
          </div>
          <div class="differential-card">
            <p class="label">Pressão</p>
          </div>
          <div class="differential-card">
            <p class="label">Concentração do peróxido</p>
          </div>
          <div class="differential-card">
            <p class="label">Energia do plasma</p>
          </div>
        </div>
        <p style="margin-top:1.5rem;color:#55585a;font-size:0.9375rem;">
          Esses parâmetros — mais o tempo total do ciclo — são cuidadosamente controlados para
          garantir a eficácia da esterilização, preservando a integridade dos materiais processados.
        </p>
      </div>
    </section>

    <!-- ===================== BENEFÍCIOS ===================== -->
    <section>
      <div class="container section-inner">
        <span class="eyebrow">Benefícios</span>
        <h2>Por que o PHM faz sentido para a sua CME.</h2>
        <div class="differentials-grid" style="margin-top:2.5rem;">
          <div class="differential-card">
            <p class="label">Eficácia em baixa temperatura</p>
            <p class="body">Opera entre 45°C e 55°C, preservando endoscópios, fibras ópticas, componentes eletrônicos e plásticos que não resistiriam ao calor.</p>
          </div>
          <div class="differential-card">
            <p class="label">Ciclos rápidos</p>
            <p class="body">Entre 25 e 45 minutos, contra até 16 horas de outros métodos de baixa temperatura — mais rotatividade de materiais e produtividade na CME.</p>
          </div>
          <div class="differential-card">
            <p class="label">Segurança para equipe e paciente</p>
            <p class="body">Sem resíduos tóxicos: os subprodutos do processo são apenas água e oxigênio. Menor risco ocupacional que óxido de etileno ou formaldeído.</p>
          </div>
          <div class="differential-card">
            <p class="label">Benefícios ambientais</p>
            <p class="body">Processo ecologicamente responsável, com consumo mínimo de água e até 87% menos energia elétrica que a esterilização a vapor.</p>
          </div>
          <div class="differential-card">
            <p class="label">Compatibilidade ampla</p>
            <p class="body">Preserva metais sensíveis, instrumentos com componentes eletrônicos e ópticos, e materiais modernos como polímeros especiais.</p>
          </div>
          <div class="differential-card">
            <p class="label">Economia a longo prazo</p>
            <p class="body">Prolonga a vida útil dos instrumentos, reduz o tempo de inatividade do arsenal e diminui a necessidade de reprocessamento externo.</p>
          </div>
          <div class="differential-card">
            <p class="label">Monitoramento e rastreabilidade</p>
            <p class="body">Indicador biológico de resposta rápida (20 minutos) e integração com o sistema de rastreabilidade Sterifast, do ciclo de limpeza ao uso no paciente.</p>
          </div>
          <div class="differential-card">
            <p class="label">Adaptabilidade operacional</p>
            <p class="body">Múltiplos ciclos programáveis e diferentes tamanhos de câmara, ajustando-se ao volume de processamento da sua instituição.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================== COMPARATIVO ===================== -->
    <section style="background-color:var(--gray-light);">
      <div class="container section-inner">
        <span class="eyebrow">Comparativo</span>
        <h2>Como o PHM se compara a outros métodos de esterilização.</h2>
        <div class="compare-table-wrap">
          <table class="compare-table">
            <thead>
              <tr>
                <th>Método</th>
                <th>Temperatura</th>
                <th>Tempo de ciclo</th>
                <th>Compatibilidade</th>
                <th>Segurança</th>
                <th>Impacto ambiental</th>
              </tr>
            </thead>
            <tbody>
              <tr class="highlight">
                <td>PHM (plasma de peróxido)</td>
                <td>35–55°C</td>
                <td>30–90 min</td>
                <td>Excelente p/ termossensíveis</td>
                <td>Alta</td>
                <td>Baixo</td>
              </tr>
              <tr>
                <td>Vapor (autoclave)</td>
                <td>121–134°C</td>
                <td>30–60 min</td>
                <td>Limitada a termorresistentes</td>
                <td>Alta</td>
                <td>Médio (água)</td>
              </tr>
              <tr>
                <td>Óxido de etileno (EtO)</td>
                <td>37–63°C</td>
                <td>10–16h</td>
                <td>Excelente</td>
                <td>Baixa</td>
                <td>Alto</td>
              </tr>
              <tr>
                <td>Formaldeído (VBTF)</td>
                <td>~60°C</td>
                <td>~5h</td>
                <td>Boa</td>
                <td>Média</td>
                <td>Médio-alto</td>
              </tr>
              <tr>
                <td>Ácido peracético</td>
                <td>Ambiente–40°C</td>
                <td>30–60 min</td>
                <td>Média (corrosivo)</td>
                <td>Média</td>
                <td>Baixo</td>
              </tr>
              <tr>
                <td>Radiação (gama/e-beam)</td>
                <td>Ambiente</td>
                <td>Variável</td>
                <td>Variável</td>
                <td>Média</td>
                <td>Baixo</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p style="margin-top:1.5rem;color:#55585a;font-size:0.9375rem;max-width:48rem;">
          O PHM oferece um equilíbrio único: ciclos relativamente rápidos, operação em baixa
          temperatura, segurança para operadores e pacientes, baixo impacto ambiental e excelente
          compatibilidade com materiais termossensíveis — uma opção valiosa para CMEs modernas que
          processam instrumentos complexos e sensíveis.
        </p>
      </div>
    </section>

    <!-- ===================== CONFORMIDADE ===================== -->
    <section>
      <div class="container section-inner">
        <span class="eyebrow">Conformidade</span>
        <h2>Registrado na ANVISA, fabricado sob certificação internacional.</h2>
        <p style="margin-top:1.25rem;color:#55585a;font-size:1rem;line-height:1.75;max-width:48rem;">
          O PHM MedControl possui notificação de dispositivo médico junto à ANVISA (Agência
          Nacional de Vigilância Sanitária) e é fabricado por planta certificada ISO 13485 —
          norma internacional de sistemas de gestão da qualidade para dispositivos médicos.
        </p>
      </div>
    </section>

    <!-- ===================== CTA ===================== -->
    <section class="final-cta">
      <div class="container section-inner">
        <div class="final-cta-main">
          <span class="eyebrow">Vamos conversar?</span>
          <h2>Peça uma demonstração do PHM para a sua central.</h2>
          <p class="lead">
            Fale com um especialista MedControl e entenda as condições de comodato para o seu
            hospital ou clínica.
          </p>
          <div class="hero-ctas">
            <a href="{WA_LINK}"
               target="_blank" rel="noopener noreferrer" class="btn btn-white">
              Falar com um especialista <span aria-hidden="true">→</span>
            </a>
          </div>
        </div>
      </div>
    </section>
  </main>

'''

page = (
    head(
        "PHM MedControl — Esterilizador a Plasma por Peróxido de Hidrogênio",
        "Conheça o PHM MedControl: esterilizador a plasma por peróxido de hidrogênio vaporizado em baixa temperatura, disponível em comodato. Ciclos rápidos, sem resíduos tóxicos.",
    )
    + header(active="linhas.html")
    + phm_body
    + footer()
    + whatsapp_float()
)
write_page("phm-medcontrol.html", page)

# =============================================================================
# DEPOIMENTOS
# =============================================================================

def testimonial(quote, author, org):
    return f'''          <figure class="testimonial-card">
            <div class="testimonial-media">
              <div class="media-placeholder">[imagem]</div>
            </div>
            <div class="testimonial-body">
              <blockquote>{quote}</blockquote>
              <figcaption>
                <div class="author">{author}</div>
                <div class="org">{org}</div>
              </figcaption>
            </div>
          </figure>
'''

testimonials_html = "".join([
    testimonial(
        "A MedControl não entrega só produto — entrega segurança. O suporte técnico que recebemos mudou o nível de confiança da nossa equipe em cada ciclo. É o tipo de parceria que a gente não troca.",
        "Enfermeira responsável, CME",
        "Hospital de médio porte — Interior de SP",
    ),
    testimonial(
        "Retorno rápido, produto certificado e uma equipe que realmente entende de CME. Eles chegam antes da gente perceber que precisa de suporte. Isso é diferente de tudo que conhecemos no setor.",
        "Coordenação de suprimentos",
        "Rede hospitalar — Centro-Oeste",
    ),
    testimonial(
        "Desde que migramos para a MedControl, o retrabalho da nossa central caiu de forma perceptível. Insumo de qualidade faz diferença no resultado. E o comodato dos equipamentos foi decisivo para modernizar sem comprometer o orçamento.",
        "Gerência assistencial",
        "Clínica cirúrgica — Bauru/SP",
    ),
    testimonial(
        "O que mais pesa pra gente é ter alguém do outro lado que entende de rotina hospitalar, não só de venda. A MedControl acompanha de perto, e isso se traduz em segurança pro paciente.",
        "Coordenação de enfermagem",
        "Hospital regional — Sul de Minas",
    ),
    testimonial(
        "Trocamos de fornecedor há dois anos e nunca mais pensamos em voltar. Rastreabilidade completa, prazo cumprido e um time técnico que resolve o problema antes de virar uma crise.",
        "Gestão hospitalar",
        "Hospital privado — Grande São Paulo",
    ),
])

depoimentos_body = f'''{page_banner(
    "Depoimentos",
    "A voz de quem opera uma central de esterilização todos os dias.",
    "Enfermeiros, coordenadores de CME e gestores hospitalares contam como a parceria com a MedControl mudou a rotina da central.",
    "Depoimentos",
)}
    <section class="testimonials">
      <div class="container section-inner">
        <div class="testimonials-grid">
{testimonials_html}        </div>
      </div>
    </section>

    <!-- ===================== PARCEIROS / CLIENTES ===================== -->
    <section aria-label="Instituições atendidas" class="social-proof">
      <div class="container">
        <p>Parceira técnica de hospitais, clínicas e centros cirúrgicos em todo o Brasil</p>
        <div class="logo-grid">
          <div>[logo]</div>
          <div>[logo]</div>
          <div>[logo]</div>
          <div>[logo]</div>
          <div>[logo]</div>
          <div>[logo]</div>
        </div>
      </div>
    </section>

    <section class="final-cta">
      <div class="container section-inner">
        <div class="final-cta-main">
          <span class="eyebrow">Sua central pode ser a próxima</span>
          <h2>Fale com um especialista e veja como podemos apoiar sua CME.</h2>
          <p class="lead">
            Envie sua demanda pelo WhatsApp e receba, no mesmo dia útil, cotação e recomendação
            técnica personalizada.
          </p>
          <div class="hero-ctas">
            <a href="{WA_LINK}"
               target="_blank" rel="noopener noreferrer" class="btn btn-white">
              Falar com um especialista <span aria-hidden="true">→</span>
            </a>
          </div>
        </div>
      </div>
    </section>
  </main>

'''

page = (
    head(
        "Depoimentos MedControl — O que Dizem Hospitais e Clínicas Parceiras",
        "Veja depoimentos reais de enfermeiros, coordenadores de CME e gestores hospitalares sobre a parceria técnica com a MedControl.",
    )
    + header(active="depoimentos.html")
    + depoimentos_body
    + footer()
    + whatsapp_float()
)
write_page("depoimentos.html", page)

# =============================================================================
# CONTATO
# =============================================================================

contato_body = f'''{page_banner(
    "Contato comercial",
    "Fale com um especialista MedControl.",
    "Envie sua demanda pelo WhatsApp e receba, no mesmo dia útil, cotação e recomendação técnica de um consultor especializado em CME hospitalar.",
    "Contato",
)}
    <section class="contact-main-section section-inner">
      <div class="container">
        <div class="contact-main-grid">

          <div class="contact-left-col">

            <div class="whatsapp-sell-box">
              <div>
                <div class="sell-title">Conversar via WhatsApp</div>
                <div class="sell-desc">Fale diretamente com um especialista MedControl agora mesmo, para resposta imediata.</div>
              </div>
              <a href="{WA_LINK}"
                 target="_blank" rel="noopener noreferrer" class="btn btn-outline-blue">
                Abrir chat <span aria-hidden="true">→</span>
              </a>
            </div>

            <div class="social-contact-row">
              <a href="https://www.instagram.com/medcontrol.bauru/" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
                <svg viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
                Instagram
              </a>
              <a href="https://www.facebook.com/medcontrolbauru" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
                <svg viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
                Facebook
              </a>
              <a href="https://www.linkedin.com/company/medcontrol/posts/?feedView=all" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
                <svg viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                LinkedIn
              </a>
            </div>

            <div class="base-info-box">
              <div class="base-title">Nossa base</div>
              <div class="base-desc">
                <span style="color:var(--text); font-weight:700; display:block; margin-bottom:0.15rem;">MedControl Bauru</span>
                <a href="https://www.google.com/maps/dir/?api=1&destination=Rua+Jacy+Stevaux+Vila%C3%A7a,+2-66+-+Jardim+Contorno,+Bauru+-+SP,+17047-250" target="_blank" rel="noopener noreferrer">
                  Rua Jacy Stevaux Vilaça, 2-66 — Jardim Contorno, Bauru - SP, 17047-250
                </a><br />
                (14) 3208-7108 · Segunda a sexta, 08h às 17h
              </div>
            </div>

            <div class="map-wrapper">
              <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3978.7785885322946!2d-49.04736529999999!3d-22.3362043!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94bf67a8f3e2df3f%3A0x1d6ac693740046d6!2sMedcontrol%20Comercio%20de%20Materiais%20Hospitalares%20EIRELI!5e1!3m2!1sen!2sbr!4v1784723779617!5m2!1sen!2sbr" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
            </div>

          </div>

          <div class="contact-form-container">
            <span class="form-eyebrow">Envie uma mensagem</span>

            <form id="contactForm">
              <div class="form-group">
                <label for="name">Nome completo</label>
                <input type="text" id="name" placeholder="Ex: Maria Silva">
              </div>

              <div class="form-group">
                <label for="email">E-mail</label>
                <input type="email" id="email" placeholder="maria@hospital.com.br">
              </div>

              <div class="form-group">
                <label for="phone">Telefone / WhatsApp</label>
                <input type="tel" id="phone" placeholder="(14) 99999-0000">
              </div>

              <div class="form-group">
                <label for="subject">Assunto de interesse</label>
                <select id="subject">
                  <option value="" disabled selected>Selecione uma opção...</option>
                  <option value="embalagens">Embalagens para esterilização</option>
                  <option value="comodato">Equipamentos em comodato</option>
                  <option value="indicadores">Indicadores e controle de processo</option>
                  <option value="suporte">Suporte técnico e capacitação</option>
                  <option value="outros">Outros assuntos</option>
                </select>
              </div>

              <div class="form-group">
                <label for="message">Mensagem</label>
                <textarea id="message" rows="5" placeholder="Como podemos ajudar a sua central de esterilização?"></textarea>
              </div>

              <div id="contactFormMsg" class="msg"></div>

              <button type="submit" id="contactFormSubmit" class="btn btn-accent-lg" style="width: 100%; justify-content: center; border: none; cursor: pointer;">
                Enviar mensagem <span aria-hidden="true">→</span>
              </button>
            </form>
          </div>

        </div>
      </div>
    </section>
  </main>

'''

page = (
    head(
        "Contato MedControl — Fale com um Especialista",
        "Entre em contato com a MedControl: WhatsApp, telefone, e-mail e endereço. Atendimento consultivo em todo o Brasil.",
    )
    + header(active="contato.html")
    + contato_body
    + footer()
    + whatsapp_float(CONTACT_FORM_SCRIPTS)
)
write_page("contato.html", page)

# =============================================================================
# BLOG — listagem dinâmica (Firestore) + página de artigo dinâmica
# =============================================================================

BLOG_LIST_SCRIPTS = '''
  <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore-compat.js"></script>
  <script src="js/firebase-config.js"></script>
  <script>
  (function () {
    const grid = document.getElementById("blogGrid");
    if (!grid) return;

    function esc(s) {
      return String(s == null ? "" : s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
    }

    if (!window.MC || !MC.configured || !MC.db) {
      grid.innerHTML = '<p style="grid-column:1/-1;color:#6b6d6e;">Não foi possível carregar os artigos no momento.</p>';
      return;
    }

    MC.db.collection("articles").where("status", "==", "publicado").orderBy("createdAt", "desc").get()
      .then(function (snap) {
        if (snap.empty) {
          grid.innerHTML = '<p style="grid-column:1/-1;color:#6b6d6e;">Nenhum artigo publicado ainda. Volte em breve.</p>';
          return;
        }
        let html = "";
        snap.forEach(function (doc) {
          const a = doc.data();
          const img = a.imageUrl
            ? '<img src="' + esc(a.imageUrl) + '" alt="' + esc(a.title || "") + '" style="width:100%;height:200px;object-fit:cover;display:block;border-bottom:1px solid var(--gray-light);">'
            : '<div class="media-placeholder">[imagem]</div>';
          html += ''
            + '<article class="blog-card">'
            +   img
            +   '<div class="blog-card-body">'
            +     '<h3>' + esc(a.title || "(sem título)") + '</h3>'
            +     '<p>' + esc(a.excerpt || "") + '</p>'
            +     '<a href="artigo.html?id=' + doc.id + '" class="blog-card-cta">Ler artigo <span aria-hidden="true">→</span></a>'
            +   '</div>'
            + '</article>';
        });
        grid.innerHTML = html;
      })
      .catch(function (err) {
        grid.innerHTML = '<p style="grid-column:1/-1;color:#6b6d6e;">Erro ao carregar artigos: ' + esc(err.message) + '</p>';
      });
  })();
  </script>
'''

blog_body = f'''{page_banner(
    "Blog MedControl",
    "Conteúdo técnico para quem vive uma central de esterilização.",
    "Boas práticas, tendências e orientações técnicas para enfermeiros, coordenadores de CME e gestores hospitalares.",
    "Blog",
)}
    <section>
      <div class="container section-inner">
        <div class="blog-grid" id="blogGrid">
          <p style="grid-column:1/-1;color:#6b6d6e;">Carregando artigos…</p>
        </div>
      </div>
    </section>
  </main>

'''

page = (
    head(
        "Blog MedControl — Conteúdo Técnico para CME Hospitalar",
        "Boas práticas, tendências e orientações técnicas sobre esterilização hospitalar, CME e segurança do paciente.",
    )
    + header(active="blog.html")
    + blog_body
    + footer()
    + whatsapp_float(BLOG_LIST_SCRIPTS)
)
write_page("blog.html", page)

# ---------------- Página de artigo individual (template dinâmico) ----------------

ARTIGO_SCRIPTS = '''
  <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore-compat.js"></script>
  <script src="js/firebase-config.js"></script>
  <script>
  (function () {
    const wrap = document.getElementById("articleWrap");
    if (!wrap) return;

    function esc(s) {
      return String(s == null ? "" : s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
    }
    function paragraphs(text) {
      return (text || "").split(/\\n+/).filter(Boolean).map(p => "<p>" + esc(p) + "</p>").join("");
    }

    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");

    if (!window.MC || !MC.configured || !MC.db || !id) {
      wrap.innerHTML = '<p style="color:#6b6d6e;">Artigo não encontrado. <a href="blog.html">Voltar para o blog</a>.</p>';
      return;
    }

    Promise.all([
      MC.db.collection("articles").doc(id).get(),
      MC.db.collection("articles").where("status", "==", "publicado").orderBy("createdAt", "desc").get()
    ]).then(function (results) {
      const doc = results[0];
      const listSnap = results[1];
      if (!doc.exists || doc.data().status !== "publicado") {
        wrap.innerHTML = '<p style="color:#6b6d6e;">Artigo não encontrado ou não publicado. <a href="blog.html">Voltar para o blog</a>.</p>';
        return;
      }
      const a = doc.data();
      document.title = (a.title || "Artigo") + " — Blog MedControl";

      const list = [];
      listSnap.forEach(d => list.push({ id: d.id, ...d.data() }));
      const idx = list.findIndex(x => x.id === id);
      const prevA = idx >= 0 && idx < list.length - 1 ? list[idx + 1] : null;
      const nextA = idx > 0 ? list[idx - 1] : null;

      const img = a.imageUrl
        ? '<img src="' + esc(a.imageUrl) + '" alt="' + esc(a.title || "") + '" style="width:100%;border-radius:12px;display:block;">'
        : '<div class="media-placeholder">[imagem]</div>';

      let navHtml = '<div class="article-nav">';
      navHtml += prevA
        ? '<a href="artigo.html?id=' + prevA.id + '" class="article-nav-link"><span class="direction">← Anterior</span><span class="title">' + esc(prevA.title) + '</span></a>'
        : '<span></span>';
      navHtml += nextA
        ? '<a href="artigo.html?id=' + nextA.id + '" class="article-nav-link next"><span class="direction">Próximo →</span><span class="title">' + esc(nextA.title) + '</span></a>'
        : '';
      navHtml += '</div>';

      wrap.innerHTML = ''
        + '<a href="blog.html" class="blog-back-link">← Voltar para o blog</a>'
        + '<div class="article-hero">' + img + '</div>'
        + '<div class="article-body">' + paragraphs(a.content) + '</div>'
        + navHtml;

      const bannerEyebrow = document.getElementById("artBannerEyebrow");
      const bannerTitle = document.getElementById("artBannerTitle");
      if (bannerEyebrow) bannerEyebrow.textContent = a.category || "Artigo";
      if (bannerTitle) bannerTitle.textContent = a.title || "";
    }).catch(function (err) {
      wrap.innerHTML = '<p style="color:#6b6d6e;">Erro ao carregar o artigo: ' + esc(err.message) + '</p>';
    });
  })();
  </script>
'''

artigo_body = '''    <section class="page-banner">
      <div class="container">
        <div class="breadcrumb">
          <a href="index.html">Início</a>
          <span aria-hidden="true">/</span>
          <a href="blog.html">Blog</a>
        </div>
        <span class="eyebrow" id="artBannerEyebrow">Artigo</span>
        <h1 id="artBannerTitle">Carregando…</h1>
      </div>
    </section>

    <section>
      <div class="container section-inner" id="articleWrap">
        <p style="color:#6b6d6e;">Carregando artigo…</p>
      </div>
    </section>
  </main>

'''

page = (
    head(
        "Artigo — Blog MedControl",
        "Conteúdo técnico MedControl sobre esterilização hospitalar e segurança do paciente.",
    )
    + header(active="blog.html")
    + artigo_body
    + footer()
    + whatsapp_float(ARTIGO_SCRIPTS)
)
write_page("artigo.html", page)

print("Concluído.")
