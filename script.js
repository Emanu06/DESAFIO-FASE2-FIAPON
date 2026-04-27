
// Animação de entrada das seções ao rolar
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.style.opacity = '1';
      e.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.05 });
 
document.querySelectorAll('section:not(#hero)').forEach(sec => {
  sec.style.opacity = '0';
  sec.style.transform = 'translateY(30px)';
  sec.style.transition = 'opacity 0.7s ease, transform 0.7s ease';
  observer.observe(sec);
});
