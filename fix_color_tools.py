import os, re

# 1. Pehle backup se clean file wapas lena taaki koi text/menu kharab na ho
if os.path.exists(os.path.expanduser("~/my_backup/csc.html")):
    with open(os.path.expanduser("~/my_backup/csc.html"), "r", encoding="utf-8", errors="ignore") as f:
        base_html = f.read()
else:
    with open("csc.html", "r", encoding="utf-8", errors="ignore") as f:
        base_html = f.read()

# Pichle badlaav wapas normal karna (agar backup me na ho)
base_html = re.sub(r'<style id="mukesh-custom-app-theme">.*?</style>', '', base_html, flags=re.DOTALL)
base_html = re.sub(r'<style id="muku3p-clean-brand">.*?</style>', '', base_html, flags=re.DOTALL)
base_html = re.sub(r'<style id="muku3p-color-adjust">.*?</style>', '', base_html, flags=re.DOTALL)
base_html = re.sub(r'<div class="app-search-wrap">.*?</script>', '', base_html, flags=re.DOTALL)

# Agri card photo aur Muku3p naam pakka karna
base_html = re.sub(r'sita_card\.jpg(\?v=\d+)?|kisan\.jpg(\?v=\d+)?|farmer_card\.jpg(\?v=\d+)?', 'agri_card.svg?v=1', base_html)
base_html = re.sub(r'https?://[^\s"\'<>]*(ibb\.co|imgbb|googleusercontent)[^\s"\'<>]*', 'agri_card.svg?v=1', base_html, flags=re.I)
base_html = base_html.replace("Mukesh CSC Tools", "Muku3p")
base_html = base_html.replace("Smart CSC Tools", "Muku3p")

# 2. Sirf Colour Change aur All Tools Mobile Adjustment CSS
style_only = '''
<style id="muku3p-color-adjust">
  /* Laal/Maroon colour ki jagah clean Teal-Blue colour */
  .bg-gradient-to-r, .from-red-700, .bg-red-700, .bg-red-800, 
  [style*="#991b1b"], [style*="#b91c1c"], [style*="#be123c"], [style*="#881337"] {
    background: linear-gradient(135deg, #0f766e 0%, #0369a1 100%) !important;
  }

  /* Buttons aur Active Tabs ka colour */
  .bg-red-600, .bg-rose-600, .bg-red-500, .hover\\:bg-red-700:hover {
    background-color: #0284c7 !important;
    border-color: #0284c7 !important;
    color: #ffffff !important;
  }

  /* Text aur numbers (50+, 100K+, Muku3p logo) ka colour */
  .text-red-600, .text-rose-600, .text-red-700, .text-rose-700 {
    color: #0284c7 !important;
  }

  /* All Tools Adjustment: Phone me side-menu hatakar saare tools full screen barabar dikhana */
  @media (max-width: 768px) {
    aside, .w-64, .md\\:w-64, .lg\\:w-1\\/4 {
      display: none !important;
    }
    .grid {
      grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
      gap: 12px !important;
      padding: 4px !important;
    }
    .grid > div {
      display: flex !important;
      flex-direction: column !important;
      justify-content: space-between !important;
      height: 100% !important;
      padding: 12px !important;
    }
    .grid > div img {
      height: 110px !important;
      object-fit: contain !important;
      background: #f8fafc !important;
      border-radius: 8px !important;
    }
  }
</style>
'''

if '</head>' in base_html:
    base_html = base_html.replace('</head>', style_only + '\n</head>')
else:
    base_html = style_only + base_html

for fn in ["csc.html", "index.html", "new.html", "final.html"]:
    with open(fn, "w", encoding="utf-8") as f:
        f.write(base_html)

print("Done! Sab pehle jaisa hai, sirf colour aur All Tools adjust ho gaya!")
