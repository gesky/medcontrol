// MedControl — Landing Page
// JS mínimo: ano dinâmico no rodapé + menu hambúrguer no mobile. Nenhuma dependência externa.

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
});
