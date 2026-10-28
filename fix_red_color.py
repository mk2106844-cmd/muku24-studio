import os, glob, re

# HTML aur CSS files ke andar jitne bhi Red/Maroon colors hain unhe Royal Blue (#2563eb) me badalna
def change_red_to_blue(text):
    # Hex color codes replace karna
    red_codes = ['#991b1b', '#b91c1c', '#dc2626', '#ef4444', '#7f1d1d', '#881337', '#9f1239', '#be123c', '#e11d48', '#a91d3a', '#c7253e', '#800020', '#8b0000', '#a51c30']
    for rc in red_codes:
        text = text.replace(rc, '#2563eb')
        text = text.replace(rc.upper(), '#2563eb')
    
    # Tailwind ya inline red classes ko blue me badalna
    text = re.sub(r'bg-(red|rose)-([0-9]+)', r'bg-blue-600', text)
    text = re.sub(r'text-(red|rose)-([0-9]+)', r'text-blue-600', text)
    text = re.sub(r'border-(red|rose)-([0-9]+)', r'border-blue-600', text)
    text = re.sub(r'from-(red|rose)-([0-9]+)', r'from-indigo-900', text)
    text = re.sub(r'to-(red|rose)-([0-9]+)', r'to-blue-700', text)
    return text

# Global Style joki kisi bhi bache hue red element ko Royal Blue gradient me badal dega
blue_override_style = '''
<style id="muku3p-royal-blue-theme">
  /* Lal banner ko Royal Blue Gradient banana */
  section:first-of-type, .bg-red-700, .bg-red-800, .from-red-700, [style*="background"] {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%) !important;
  }
  /* Lal text aur numbers ko blue banana */
  .text-red-600, .text-red-700, .text-rose-600 {
    color: #2563eb !important;
  }
  /* Lal buttons aur active tabs ko blue banana */
  .bg-red-600, .bg-rose-600, button.bg-red-600 {
    background-color: #2563eb !important;
  }
  /* Side Categories box ko hide karna aur grid barabar karna */
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
  .grid > div a, .grid > div button {
    background: #2563eb !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
    padding: 9px 12px !important;
    text-align: center !important;
    display: block !important;
    width: 100% !important;
  }
</style>
<script>
function removeJunkPopups() {
  document.querySelectorAll('div, aside').forEach(el => {
    const txt = (el.innerText || '').trim();
    if ((txt.includes('Just now') || txt.includes('used ')) && el.offsetHeight < 160 && el.offsetWidth < 380) {
      el.remove();
    }
  });
}
window.addEventListener('DOMContentLoaded', removeJunkPopups);
setInterval(removeJunkPopups, 400);
</script>
'''

for fn in ["csc.html", "index.html", "new.html", "final.html"]:
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        content = change_red_to_blue(content)
        
        if '</head>' in content:
            content = content.replace('</head>', blue_override_style + '\n</head>')
        else:
            content = blue_override_style + content
            
        with open(fn, "w", encoding="utf-8") as f:
            f.write(content)

print("Red color successfully replaced with Royal Blue!")
