// ═══════════════════════════════════════════════════
//  INTERACTIVE NEURAL NETWORK PARTICLE CANVAS
// ═══════════════════════════════════════════════════

(function initHeroCanvas() {
  const canvas = document.getElementById('heroCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let width, height, particles, mouse;
  const PARTICLE_COUNT = 80;
  const CONNECTION_DIST = 150;
  const MOUSE_RADIUS = 200;

  mouse = { x: -1000, y: -1000 };

  function resize() {
    const hero = document.getElementById('heroSection');
    if (!hero) return;
    width = canvas.width = hero.offsetWidth;
    height = canvas.height = hero.offsetHeight;
  }

  function createParticles() {
    particles = [];
    for (let i = 0; i < PARTICLE_COUNT; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.5,
        vy: (Math.random() - 0.5) * 0.5,
        radius: Math.random() * 2 + 0.5,
        alpha: Math.random() * 0.5 + 0.2,
        hue: Math.random() > 0.5 ? 270 : 300 // Purple or pink hue
      });
    }
  }

  function drawParticle(p) {
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
    ctx.fillStyle = `hsla(${p.hue}, 70%, 75%, ${p.alpha})`;
    ctx.fill();

    // Glow effect
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.radius * 3, 0, Math.PI * 2);
    ctx.fillStyle = `hsla(${p.hue}, 70%, 75%, ${p.alpha * 0.1})`;
    ctx.fill();
  }

  function drawConnections() {
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < CONNECTION_DIST) {
          const alpha = (1 - dist / CONNECTION_DIST) * 0.15;
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(192, 132, 252, ${alpha})`;
          ctx.lineWidth = 0.5;
          ctx.stroke();
        }
      }
    }
  }

  function drawMouseConnections() {
    particles.forEach(p => {
      const dx = mouse.x - p.x;
      const dy = mouse.y - p.y;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < MOUSE_RADIUS) {
        const alpha = (1 - dist / MOUSE_RADIUS) * 0.3;
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(mouse.x, mouse.y);
        ctx.strokeStyle = `rgba(232, 121, 249, ${alpha})`;
        ctx.lineWidth = 0.8;
        ctx.stroke();

        // Attract slightly toward mouse
        p.vx += dx * 0.00005;
        p.vy += dy * 0.00005;
      }
    });
  }

  function updateParticles() {
    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;

      // Damping
      p.vx *= 0.999;
      p.vy *= 0.999;

      // Boundaries — wrap around
      if (p.x < -10) p.x = width + 10;
      if (p.x > width + 10) p.x = -10;
      if (p.y < -10) p.y = height + 10;
      if (p.y > height + 10) p.y = -10;

      // Gentle alpha oscillation
      p.alpha += Math.sin(Date.now() * 0.001 + p.x) * 0.002;
      p.alpha = Math.max(0.1, Math.min(0.6, p.alpha));
    });
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);
    drawConnections();
    drawMouseConnections();
    particles.forEach(drawParticle);
    updateParticles();
    requestAnimationFrame(animate);
  }

  // Mouse tracking
  const hero = document.getElementById('heroSection');
  if (hero) {
    hero.addEventListener('mousemove', (e) => {
      const rect = hero.getBoundingClientRect();
      mouse.x = e.clientX - rect.left;
      mouse.y = e.clientY - rect.top;
    });
    hero.addEventListener('mouseleave', () => {
      mouse.x = -1000;
      mouse.y = -1000;
    });
  }

  window.addEventListener('resize', () => {
    resize();
  });

  resize();
  createParticles();
  animate();
})();


// ═══════════════════════════════════════════════════
//  TOGGLE, EXPAND/COLLAPSE
// ═══════════════════════════════════════════════════

function toggle(header) {
  const body = header.nextElementSibling;
  const btn = header.querySelector('.toggle-btn');
  const isOpen = body.classList.contains('open');
  body.classList.toggle('open', !isOpen);
  btn.textContent = isOpen ? '+' : '−';
}

function expandAll() {
  document.querySelectorAll('.level-body').forEach(b => b.classList.add('open'));
  document.querySelectorAll('.toggle-btn').forEach(b => b.textContent = '−');
}

function collapseAll() {
  document.querySelectorAll('.level-body').forEach(b => b.classList.remove('open'));
  document.querySelectorAll('.toggle-btn').forEach(b => b.textContent = '+');
}


// ═══════════════════════════════════════════════════
//  SCROLL EVENTS: Progress bar, reveals, quick nav
// ═══════════════════════════════════════════════════

window.addEventListener('scroll', () => {
  const scrollTop = window.scrollY;
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const pct = (scrollTop / docHeight) * 100;
  document.getElementById('progressLine').style.width = pct + '%';

  // Back to top button
  const backBtn = document.querySelector('.back-top');
  if (backBtn) {
    scrollTop > 300 ? backBtn.classList.add('show') : backBtn.classList.remove('show');
  }

  // Reveals
  document.querySelectorAll('.reveal').forEach(el => {
    const rect = el.getBoundingClientRect();
    const winH = window.innerHeight;
    if (rect.top < winH - 100) {
      el.classList.add('visible');
    }
  });

  // Quick Nav Highlights
  const levels = document.querySelectorAll('.level-card');
  const navLinks = document.querySelectorAll('.quick-nav a');
  let currentId = '';

  levels.forEach(lvl => {
    const rect = lvl.getBoundingClientRect();
    if (rect.top < window.innerHeight / 2) {
      currentId = lvl.id;
    }
  });

  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === `#${currentId}`) {
      link.classList.add('active');
    }
  });
});


// ═══════════════════════════════════════════════════
//  SEARCH FUNCTIONALITY
// ═══════════════════════════════════════════════════

const searchInput = document.getElementById('searchInput');
const searchCount = document.getElementById('searchCount');

if (searchInput) {
  searchInput.addEventListener('input', (e) => {
    const q = e.target.value.toLowerCase();
    const cards = document.querySelectorAll('.level-card');
    let totalMatches = 0;

    if (!q) {
      cards.forEach(c => c.classList.remove('hidden-search'));
      document.querySelectorAll('.topic-item').forEach(t => t.style.display = 'block');
      searchCount.classList.remove('visible');
      return;
    }

    cards.forEach(card => {
      let cardMatches = false;
      const topics = card.querySelectorAll('.topic-item');

      topics.forEach(topic => {
        const text = topic.textContent.toLowerCase();
        if (text.includes(q)) {
          topic.style.display = 'block';
          cardMatches = true;
          totalMatches++;
        } else {
          topic.style.display = 'none';
        }
      });

      if (cardMatches || card.querySelector('.level-title').textContent.toLowerCase().includes(q)) {
        card.classList.remove('hidden-search');
        if (cardMatches) {
          const body = card.querySelector('.level-body');
          body.classList.add('open');
          card.querySelector('.toggle-btn').textContent = '−';
        }
      } else {
        card.classList.add('hidden-search');
      }
    });

    searchCount.textContent = `Found ${totalMatches} matching topics`;
    searchCount.classList.add('visible');
  });

  // Keyboard shortcut: Cmd/Ctrl + K to focus search
  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      searchInput.focus();
      searchInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  });
}


// ═══════════════════════════════════════════════════
//  INITIALIZATION
// ═══════════════════════════════════════════════════

// Trigger initial scroll to animate visible elements
window.dispatchEvent(new Event('scroll'));

// Auto-open Level 0 on load
setTimeout(() => {
  const firstBody = document.querySelector('.level-body');
  const firstBtn = document.querySelector('.toggle-btn');
  if (firstBody) { firstBody.classList.add('open'); firstBtn.textContent = '−'; }
}, 100);

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});