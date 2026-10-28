import os, re

# 1. Sabse pehle backup se bilkul clean original files wapas lena taaki koi design kharab na ho
if os.path.exists(os.path.expanduser("~/my_backup/csc.html")):
    with open(os.path.expanduser("~/my_backup/csc.html"), "r", encoding="utf-8", errors="ignore") as f:
        clean_html = f.read()
else:
    with open("csc.html", "r", encoding="utf-8", errors="ignore") as f:
        clean_html = f.read()

# Naam Muku3p pakka karna aur fake popup hatana
clean_html = clean_html.replace("Mukesh CSC Tools", "Muku3p")
clean_html = clean_html.replace("Smart CSC Tools", "Muku3p")

# 2. Perfect Light SaaS Theme jo buttons ko bilkul safe rakhega
safe_pro_theme = '''
<style id="muku3p-perfect-theme">
  /* Background Soft Professional */
  html, body {
    background-color: #f1f5f9 !important;
    color: #1e293b !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  }

  /* Navbar Clean White */
  header, nav {
    background: #ffffff !important;
    border-bottom: 1px solid #e2e8f0 !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
  }

  /* Side Categories box hatana aur Grid layout barabar karna */
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

  /* Tool Cards Styling */
  .grid > div {
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04) !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
  }
  .grid > div img {
    width: 100% !important;
    height: 115px !important;
    object-fit: contain !important;
    background: #f8fafc !important;
    border-radius: 10px !important;
    padding: 6px !important;
  }

  /* Open Tool Buttons */
  .grid > div a, .grid > div button {
    background: #0284c7 !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
    padding: 9px 12px !important;
    text-align: center !important;
    display: block !important;
    width: 100% !important;
    box-shadow: 0 3px 10px rgba(2, 132, 199, 0.25) !important;
    border: none !important;
  }
</style>

<script id="muku3p-clean-js">
function removeJunk() {
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
window.addEventListener('DOMContentLoaded', removeJunk);
setInterval(removeJunk, 400);
</script>
'''

if '</head>' in clean_html:
    clean_html = clean_html.replace('</head>', safe_pro_theme + '\n</head>')
else:
    clean_html = safe_pro_theme + clean_html

for fn in ["csc.html", "index.html", "new.html", "final.html"]:
    with open(fn, "w", encoding="utf-8") as f:
        f.write(clean_html)

print("Website 100% Fixed & Cleaned!")
