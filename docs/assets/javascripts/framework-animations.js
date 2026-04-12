document.addEventListener("DOMContentLoaded", () => {
  const bars = document.querySelectorAll(".metric-fill[data-target]");
  if (!bars.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const target = Number(el.getAttribute("data-target") || 0);
        const bounded = Math.max(0, Math.min(100, target));
        el.style.width = `${bounded}%`;
        observer.unobserve(el);
      });
    },
    { threshold: 0.25 }
  );

  bars.forEach((bar) => observer.observe(bar));
});
