// MedControl — Landing Page
// JS mínimo: só o ano dinâmico no rodapé. Nenhuma dependência externa.

document.addEventListener("DOMContentLoaded", () => {
  const year = new Date().getFullYear();
  const el = document.getElementById("copyright");
  if (el) {
    el.textContent = `© ${year} MedControl · Todos os direitos reservados`;
  }
});
