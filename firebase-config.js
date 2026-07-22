/* ==========================================================================
   MedControl — Configuração do Firebase (painel administrativo)
   ==========================================================================
   1. Crie um projeto em https://console.firebase.google.com
   2. Ative: Authentication → método "E-mail/senha"
              Firestore Database → modo produção
              Storage (opcional — veja IMAGE_MODE abaixo)
   3. Em "Configurações do projeto → Geral → Seus apps", crie um app Web e
      cole as chaves abaixo, substituindo os valores de exemplo.
   4. Crie o primeiro usuário admin manualmente:
      a) Authentication → Adicionar usuário (e-mail + senha)
      b) Firestore → coleção "users" → documento com ID = UID desse usuário
         → campos: { name: "Seu nome", email: "seu@email.com", role: "admin" }
      Depois disso, você consegue criar os próximos usuários direto pelo painel.
   ========================================================================== */

(function () {
  const firebaseConfig = {
    apiKey: "AIzaSyALDTptO2u9JHDOuS42PO2OfN3WPvBGvks",
    authDomain: "medcontrol-e07c2.firebaseapp.com",
    projectId: "medcontrol-e07c2",
    storageBucket: "medcontrol-e07c2.firebasestorage.app",
    messagingSenderId: "707582669538",
    appId: "1:707582669538:web:88d4d121041d174d51a4bb",
  };

  // Enquanto as chaves acima não forem preenchidas, o painel mostra a tela
  // de configuração em vez de tentar conectar com credenciais inválidas.
  const isConfigured = firebaseConfig.apiKey !== "COLE_AQUI_SUA_API_KEY";

  if (isConfigured) {
    firebase.initializeApp(firebaseConfig);
  }

  window.MC = {
    configured: isConfigured,
    config: firebaseConfig,
    auth: isConfigured ? firebase.auth() : null,
    db: isConfigured ? firebase.firestore() : null,
    // Storage é opcional: no plano gratuito (Spark) do Firebase, o Storage
    // exige upgrade para o plano Blaze. Enquanto isso, IMAGE_MODE "inline"
    // guarda a capa do artigo como base64 direto no Firestore (funciona,
    // mas com limite de tamanho por imagem). Quando fizer o upgrade pra
    // Blaze, troque para "storage" e a capa passa a subir pro Firebase
    // Storage normalmente.
    storage: isConfigured && firebase.apps.length && firebase.storage ? (() => { try { return firebase.storage(); } catch (e) { return null; } })() : null,
    IMAGE_MODE: "inline", // "inline" ou "storage"
    ROLES: ["admin", "editor"],
  };
})();
