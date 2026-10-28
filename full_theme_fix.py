import os, glob, re

# 1. HTML aur CSS dono files me jahan bhi Red/Maroon color code hai use Blue/Teal karna
red_hex_patterns = [
    r'#991b1b', r'#b91c1c', r'#dc2626', r'#ef4444', r'#7f1d1d',
    r'#881337', r'#9f1239', r'#be123c', r'#e11d48', r'#f43f5e',
    r'#a91d3a', r'#c7253e', r'#800020', r'#8b0000', r'#a51c30',
    r'#b01e28', r'#d90429', r'#ef233c', r'#c1121f', r'#780000'
]

def replace_colors(text):
    for pat in red_hex_patterns:
        text = re.sub(pat, '#0284c7', text, flags=re.I)
    # Tailwind classes me red aur rose ko sky/teal me badalna
    text = re.sub(r'\b(bg|text|border|from|to|via|ring)-(red|rose|crimson|pink)-([0-9]{2,3})\b', r'\1-sky-\3', text)
    return text

# Saari CSS files update karna
for css_file in glob.glob('**/*.css', recursive=True):
    try:
        with open(css_file, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        c = replace_colors(c)
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(c)
    except:
        pass

# 2. Universal CSS & JS جو Desktop Mode aur Mobile Mode dono me colour + layout set karega
universal_override = '''
<style id="muku3p-universal-theme">
  :root {
    --primary: #0284c7 !important;
    --primary-dark: #0369a1 !important;
    --secondary: #0f766e !important;
    --red: #0284c7 !important;
    --maroon: #0f766e !important;
  }

  /* Hero Section aur Banner ka Naya Colour (Desktop + Mobile) */
  section:first-of-type, .hero, .banner, [class*="hero"], [class*="banner"] {
    background: linear-gradient(135deg, #0f172a 0%, #0f766e 50%, #0284c7 100%) !important;
  }

  /* Saare Open Tool Buttons, Category Pills aur Contact Us Button */
  a, button, span, div {
    border-color: inherit;
  }
  a[class*="bg-"], button[class*="bg-"], .btn {
    transition: all 0.2s ease !important;
  }

  /* Desktop + Mobile Dono me Side Categories Box hatakar All Tools Full-Width Karna */
  aside, [class*="sidebar"] {
    display: none !important;
  }

  /* Tools Grid ko Desktop aur Mobile dono par auto-fit barabar cards me set karna */
  .grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)) !important;
    gap: 16px !important;
    width: 100% !important;
  }

  @media (max-width: 640px) {
    .grid {
      grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
      gap: 10px !important;
    }
  }
</style>

<script id="muku3p-runtime-fixer">
function applyMukuTheme() {
  // 1. Jahan bhi Red/Maroon background ya text computed style me ho use Teal-Blue karna
  document.querySelectorAll('*').forEach(el => {
    const st = window.getComputedStyle(el);
    
    // Background Red check
    const bg = st.backgroundColor;
    const bgImg = st.backgroundImage;
    if (bg && bg.startsWith('rgb')) {
      const m = bg.match(/\\d+/g);
      if (m && parseInt(m[0]) > 140 && parseInt(m[1]) < 60 && parseInt(m[2]) < 80) {
        el.style.setProperty('background-color', '#0284c7', 'important');
      }
    }
    if (bgImg && (bgImg.includes('rgb(1') || bgImg.includes('rgb(2') || bgImg.includes('radial') || bgImg.includes('linear'))) {
      if (el.innerText.includes('Welcome to Muku3p')) {
        el.style.setProperty('background', 'linear-gradient(135deg, #0f172a 0%, #0f766e 50%, #0284c7 100%)', 'important');
      }
    }

    // Text Red check (50+, 100K+, Muku3p logo)
    const col = st.color;
    if (col && col.startsWith('rgb')) {
      const m = col.match(/\\d+/g);
      if (m && parseInt(m[0]) > 150 && parseInt(m[1]) < 60 && parseInt(m[2]) < 80) {
        el.style.setProperty('color', '#0284c7', 'important');
      }
    }

    // Left side wala Categories box chupana (Desktop + Mobile dono me)
    if (el.tagName === 'DIV' || el.tagName === 'ASIDE') {
      const txt = (el.innerText || '').trim();
      if (txt.startsWith('Categories') && txt.includes('Need Help?') && el.offsetWidth < 350) {
        el.style.setProperty('display', 'none', 'important');
        if (el.parentElement) {
          el.parentElement.style.setProperty('display', 'block', 'important');
        }
      }
    }
  });
}

window.addEventListener('DOMContentLoaded', applyMukuTheme);
window.addEventListener('load', applyMukuTheme);
setTimeout(applyMukuTheme, 300);
</script>
'''

for fn in ["csc.html", "index.html", "new.html", "final.html"]:
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8", errors="ignore") as f:
            h = f.read()

        # Purane styles saaf karna
        h = re.sub(r'<style id="muku3p-.*?">.*?</style>', '', h, flags=re.DOTALL)
        h = re.sub(r'<script id="muku3p-runtime-fixer">.*?</script>', '', h, flags=re.DOTALL)

        # Hex colors aur classes replace karna
        h = replace_colors(h)

        # Naya universal style aur script lagana
        if '</body>' in h:
            h = h.replace('</body>', universal_override + '\n</body>')
        else:
            h = h + universal_override

        with open(fn, "w", encoding="utf-8") as f:
            f.write(h)

print("Theme Colour + Desktop & Mobile Mode Layout 100% Updated!")
