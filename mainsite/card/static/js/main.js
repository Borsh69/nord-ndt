"use strict";

// Только поведение интерфейса. Данные и маршруты подключаются на вашей стороне.
// Фокус на якорной секции помогает пользователям клавиатуры продолжить навигацию.
document.addEventListener("click", (event) => {
  const link = event.target.closest('a[href^="#"]');
  if (!link || event.defaultPrevented || event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
  const id = link.getAttribute("href").slice(1);
  const target = document.getElementById(id);
  if (!target) return;
  if (!target.hasAttribute("tabindex")) {
    target.setAttribute("tabindex", "-1");
    target.addEventListener("blur", () => target.removeAttribute("tabindex"), {once: true});
  }
  target.focus({preventScroll: true});
});
