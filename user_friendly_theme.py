import os, re

clean_theme = '''
<style id="muku3p-user-friendly-theme">
  /* 1. Clean, Soft & User-Friendly Light Background */
  html, body, main, section, article, footer, 
  .bg-white, .bg-gray-50, .bg-gray-100, .bg-slate-50, .bg-slate-100 {
    background-color: #f8fafc !important;
    color: #1e293b !important;
  }

  /* 2. Top Header & Navbar */
  header, nav {
    background: #ffffff !important;
    border-bottom: 1px solid #e2e8f0 !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04) !important;
  }
  header a:first-of-type, .logo, [class*="logo"] {
    color: #0284c7 !important;
    font-weight: 800 !important;
  }

  /* 3. Hero Banner - Professional Clean Blue */
  section:first-of-type {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%) !important;
    color: #ffffff !important;
  }
  section:first-of-type h1, section:first-of-type p {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
  }

  /* 4. Tool Cards - Clean White Cards with Soft Shadow */
  .grid > div, [class*="shadow"], [class*="rounded-xl"] {
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05) !important;
    border-radius: 16px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
  }

  /* 5. Tool Images Container */
  .grid > div > div:first-child {
    background: #f1f5f9 !important;
    border-radius: 12px !important;
    padding: 8px !important;
  }
  .grid > div img {
    width: 100% !important;
    height: 120px !important;
    object-fit: contain !important;
    background: #ffffff !important;
    border-radius: 8px !important;
  }

  /* 6. Card Titles & Text (Saaf aur readable) */
  .grid > div h3, .grid > div h4, .grid > div .font-bold {
    color: #0f172a !important;
    font-size: 15px !important;
    font-weight: 700 !important;
  }
  .grid > div p {
    color: #64748b !important;
    font-size: 12px !important;
  }

  /* 7. Open Tool Buttons - Professional Blue */
  .grid > div a, .grid > div button {
    background: #0284c7 !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
    padding: 10px 14px !important;
    text-align: center !important;
    display: block !important;
    width: 100% !important;
    box-shadow: 0 3px 10px rgba(2, 132, 199, 0.3) !important;
    border: none !important;
  }
  .grid > div a:hover {
    background: #0369a1 !important;
  }

  /* 8. Grid Layout Adjustment for Mobile & Desktop */
  aside, [class*="sidebar"] {
    display: none !important;
  }
  .grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)) !important;
    gap: 16px !important;
    padding: 10px !important;
  }
  @media (max-width: 640px) {
    .grid {
      grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
      gap: 10px !important;
      padding: 6px !important;
    }
  }
</style>

<script id="muku3p-user-friendly-js">
function cleanUI() {
  // Fake popup aur sidebar hatana
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
window.addEventListener('DOMContentLoaded', cleanUI);
setInterval(cleanUI, 400);
</script>
'''

for fn in ["csc.html", "index.html", "new.html", "final.html"]:
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8", errors="ignore") as f:
            h = f.read()

        # Purane styles hatana
        h = re.sub(r'<style id="muku3p-.*?">.*?</style>', '', h, flags=re.DOTALL)
        h = re.sub(r'<script id="muku3p-.*?">.*?</script>', '', h, flags=re.DOTALL)

        if '</body>' in h:
            h = h.replace('</body>', clean_theme + '\n</body>')
        else:
            h = h + clean_theme

        with open(fn, "w", encoding="utf-8") as f:
            f.write(h)

print("User Friendly Clean Theme Applied!")
