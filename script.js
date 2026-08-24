// MedControl — Landing Page
// JS mínimo: ano dinâmico no rodapé + menu hambúrguer no mobile
// + rolagem suave (Lenis) + animações sutis de entrada ao rolar (fade/blur).
// Nenhuma dependência própria além da Lenis, carregada via CDN.

document.addEventListener("DOMContentLoaded", () => {
  const year = new Date().getFullYear();
  const el = document.getElementById("copyright");
  if (el) {
    el.textContent = `© ${year} MedControl · Todos os direitos reservados`;
  }

  const menuBtn = document.getElementById("mobileMenuBtn");
  const menuPanel = document.getElementById("mobileMenu");
  if (menuBtn && menuPanel) {
    menuBtn.addEventListener("click", () => {
      const isOpen = menuPanel.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
    menuPanel.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        menuPanel.classList.remove("open");
        menuBtn.setAttribute("aria-expanded", "false");
      });
    });
  }

  // ------------------------------------------------------------------
  // Rolagem suave (Lenis) — sutil, sem exagero. Se a biblioteca não
  // carregar por algum motivo, a página simplesmente usa a rolagem
  // padrão do navegador (nada quebra).
  // ------------------------------------------------------------------
  if (window.Lenis) {
    const lenis = new Lenis({ duration: 1.1 });
    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);
  }

  // ------------------------------------------------------------------
  // Animações de entrada ao rolar (fade + leve blur). A classe .reveal
  // só é adicionada aqui, via JS — se o JS não rodar, nada fica
  // escondido (o conteúdo aparece normalmente, sem animação).
  // ------------------------------------------------------------------
  const revealSelectors = [
    ".section-inner .eyebrow",
    ".section-inner h2",
    "[class*='-card']",
    ".line-block",
    ".phm-step",
    ".spec-row",
    ".about-copy",
    ".about-media img",
    ".phm-intro-copy",
    ".phm-intro img",
    ".materials-table-wrap",
    ".compare-table-wrap",
    ".spec-table-wrap",
    ".article-hero",
    ".article-body > p",
    ".institutional-video",
    ".legal-body > h2",
    ".legal-body > p",
    ".logo-grid img",
    ".final-cta-info",
  ].join(", ");

  const revealEls = document.querySelectorAll(revealSelectors);

  if (revealEls.length && "IntersectionObserver" in window) {
    revealEls.forEach((target) => target.classList.add("reveal"));

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("in-view");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );

    revealEls.forEach((target) => observer.observe(target));
  }
});
