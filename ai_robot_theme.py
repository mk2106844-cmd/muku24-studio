import os, re

ai_theme = '''
<style id="muku3p-ai-robot-theme">
  /* 1. Har jagah se White aur Red hatakar Deep Midnight AI Blue-Black Background */
  html, body, main, section, article, footer, 
  .bg-white, .bg-gray-50, .bg-gray-100, .bg-slate-50, .bg-slate-100 {
    background-color: #050511 !important;
    background-image: radial-gradient(circle at 75% 25%, #12153d 0%, #050511 70%) !important;
    color: #cbd5e1 !important;
  }

  /* 2. Top Header & Navbar (Pitch Dark + Electric Blue DS. Style Logo) */
  header, nav {
    background: rgba(5, 5, 17, 0.95) !important;
    border-bottom: 1px solid #1e2259 !important;
  }
  header a:first-of-type, .logo, [class*="logo"] {
    background: #0033ff !important;
    color: #ffffff !important;
    padding: 4px 12px !important;
    border-radius: 6px !important;
    font-weight: 900 !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 0 15px rgba(0, 51, 255, 0.6) !important;
  }

  /* 3. Hero Banner & Gradient Text ("Web Design?" Photo Style) */
  h1, h2 {
    background: linear-gradient(95deg, #ffffff 0%, #c7d2fe 45%, #818cf8 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    color: #ffffff !important;
    font-weight: 800 !important;
  }

  /* 4. 50+, 100K+, 100%, 24/7 Stats Cards Fix (Ab numbers saaf chamkenge) */
  .grid > div, [class*="shadow"], [class*="rounded-xl"], [class*="rounded-2xl"] {
    background: linear-gradient(145deg, #0b0d26 0%, #070818 100%) !important;
    border: 1px solid #1e2460 !important;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.7) !important;
  }

  /* 5. Category Filter Buttons (All Tools, Document Tools...) */
  button, a[role="tab"], .rounded-full {
    background: #0d102d !important;
    color: #94a3b8 !important;
    border: 1px solid #23296b !important;
  }
  button.active, .bg-sky-600, .bg-red-600 {
    background: #0033ff !important;
    color: #ffffff !important;
    border-color: #3b82f6 !important;
    box-shadow: 0 0 14px rgba(0, 51, 255, 0.5) !important;
  }

  /* 6. Tool Cards ka Upar Wala Safed Box Dark AI Metallic Banana */
  .grid > div > div {
    background: transparent !important;
  }
  .grid > div img {
    width: 100% !important;
    height: 110px !important;
    object-fit: contain !important;
    background: #04050f !important;
    padding: 6px !important;
    border-radius: 10px !important;
    border: 1px solid #1e2460 !important;
  }

  /* Card Titles & Description */
  .grid > div h3, .grid > div h4, .grid > div .font-bold {
    color: #e0e7ff !important;
    -webkit-text-fill-color: #e0e7ff !important;
    font-size: 14px !important;
  }
  .grid > div p {
    color: #8b9bb4 !important;
    font-size: 11.5px !important;
  }

  /* 7. Open Tool Buttons - Pure Electric Blue ("DS." Badge Colour) */
  .grid > div a, .grid > div button {
    background: linear-gradient(90deg, #0033ff 0%, #4f46e5 100%) !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    font-weight: 700 !important;
    border-radius: 8px !important;
    border: 1px solid #6366f1 !important;
    box-shadow: 0 4px 15px rgba(0, 51, 255, 0.45) !important;
    text-align: center !important;
    padding: 8px 10px !important;
    width: 100% !important;
    display: block !important;
  }

  /* POPULAR / TRENDING Ribbon Electric Purple-Blue */
  [class*="ribbon"], .absolute {
    border-color: transparent !important;
  }
</style>

<script id="muku3p-ai-robot-js">
function fixAllElements() {
  // 1. Koi bhi safed (white) section ya card bacha ho to use Dark AI Blue karna
  document.querySelectorAll('div, section, main, header, nav, aside').forEach(el => {
    const bg = window.getComputedStyle(el).backgroundColor;
    if (bg === 'rgb(255, 255, 255)' || bg === 'rgb(249, 250, 251)' || bg === 'rgb(248, 250, 252)' || bg === 'rgb(243, 244, 246)') {
      el.style.setProperty('background', '#070818', 'important');
      el.style.setProperty('color', '#cbd5e1', 'important');
    }
  });

  // 2. 50+, 100K+, 100%, 24/7 numbers ko chamkila Lavender-Blue banana
  document.querySelectorAll('*').forEach(el => {
    if (el.children.length === 0) {
      const t = (el.innerText || '').trim();
      if (['50+', '100K+', '100%', '24/7', 'Our Tools Collection'].includes(t)) {
        el.style.setProperty('color', '#a5b4fc', 'important');
        el.style.setProperty('-webkit-text-fill-color', '#a5b4fc', 'important');
        el.style.setProperty('font-weight', '900', 'important');
      }
      if (t === 'All Tools' || t === 'Muku3p') {
        el.style.setProperty('background', '#0033ff', 'important');
        el.style.setProperty('color', '#ffffff', 'important');
        el.style.setProperty('-webkit-text-fill-color', '#ffffff', 'important');
      }
    }
  });

  // 3. Left Categories sidebar aur fake popup hatana
  document.querySelectorAll('div, aside').forEach(el => {
    const txt = (el.innerText || '').trim();
    if ((txt.includes('Just now') || txt.includes('used ')) && el.offsetHeight < 160 && el.offsetWidth < 380) {
      el.remove();
    }
    if (txt.startsWith('Categories') && txt.includes('Need Help?') && el.offsetWidth < 360) {
      el.style.setProperty('display', 'none', 'important');
    }
  });
}

window.addEventListener('DOMContentLoaded', fixAllElements);
window.addEventListener('load', fixAllElements);
setInterval(fixAllElements, 300);
</script>
'''

for fn in ["csc.html", "index.html", "new.html", "final.html"]:
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8", errors="ignore") as f:
            h = f.read()

        # Purane styles aur scripts saaf karna
        h = re.sub(r'<style id="muku3p-.*?">.*?</style>', '', h, flags=re.DOTALL)
        h = re.sub(r'<script id="muku3p-.*?">.*?</script>', '', h, flags=re.DOTALL)

        # Naya AI Robot Dark Electric Theme lagana
        if '</body>' in h:
            h = h.replace('</body>', ai_theme + '\n</body>')
        else:
            h = h + ai_theme

        with open(fn, "w", encoding="utf-8") as f:
            f.write(h)

print("AI Robot Web Design Theme 100% Applied!")
