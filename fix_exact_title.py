import os, re

img_file = "water_order.png?v=4" if os.path.exists("water_order.png") else "water_jar.svg?v=4"
app_url = "water_order_app.html?v=2" if os.path.exists("water_order_app.html") else "https://calm-elf-a7af6e.netlify.app/"

inject_js = f'''
<script id="muku24-netlify-injector">
function addNetlifyCard() {{
  // 1. Upar chipki hui faltu "Muku24 Special Tool" patti hatana
  document.querySelectorAll('div').forEach(d => {{
    if (d.innerText && d.innerText.includes('New Portal Tool') && d.innerText.includes('Muku24 Special Tool') && d.offsetHeight < 220) {{
      d.remove();
    }}
  }});

  const existing = document.getElementById('muku24-special-netlify-card');
  if (existing) existing.remove();
  
  const allHeadings = document.querySelectorAll('h3, h4, h2, div, span');
  let targetCard = null;
  
  for (let el of allHeadings) {{
    if (el.children.length === 0 && el.innerText && el.innerText.trim() === 'Resume/CV Maker') {{
      targetCard = el.closest('.grid > div') || el.parentElement.parentElement;
      break;
    }}
  }}

  if (targetCard && targetCard.parentElement) {{
    const newCard = targetCard.cloneNode(true);
    newCard.id = 'muku24-special-netlify-card';
    
    // Photo lagana
    const img = newCard.querySelector('img');
    if (img) {{
      img.src = '{img_file}';
      img.alt = 'Mernal Water Order';
      img.style.objectFit = 'contain';
      img.style.background = '#ffffff';
    }}
    
    // Card ke andar jahan-jahan "Resume/CV Maker" ya "POPULAR" likha hai use sahi jagah badalna
    newCard.querySelectorAll('*').forEach(el => {{
      if (el.children.length === 0 && el.innerText) {{
        const txt = el.innerText.trim();
        if (txt === 'Resume/CV Maker') {{
          el.innerText = 'Mernal Water Order (मिनरल वाटर आर्डर)';
        }} else if (txt === 'POPULAR' || txt.includes('Mernal Water')) {{
          el.innerText = 'NEW SERVICE';
        }} else if (txt.includes('Create professional Indian-style')) {{
          el.innerText = 'Ghar, dukan ya shaadi-party ke liye 20L RO chilled water jar online book karein. (घर या पार्टी के लिए पानी आर्डर करें।)';
        }}
      }}
    }});
    
    // Open Tool Button set karna
    const link = newCard.querySelector('a, button');
    if (link) {{
      if (link.tagName === 'A') {{
        link.href = '{app_url}';
        link.target = '_blank';
        link.removeAttribute('onclick');
      }} else {{
        link.onclick = function() {{ window.open('{app_url}', '_blank'); }};
      }}
      link.innerText = 'Open Tool';
    }}
    
    targetCard.parentElement.insertBefore(newCard, targetCard);
  }}
}}

window.addEventListener('DOMContentLoaded', addNetlifyCard);
window.addEventListener('load', addNetlifyCard);
setTimeout(addNetlifyCard, 200);
</script>
'''

for fn in ["csc.html", "index.html", "new.html", "final.html"]:
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
            
        # Upar wala faltu card HTML se bhi saaf karna
        c = re.sub(r'<div class="bg-white rounded-xl border border-slate-200.*?Open Service</a>\s*</div>', '', c, flags=re.DOTALL)
        c = re.sub(r'<script id="muku24-netlify-injector">.*?</script>', '', c, flags=re.DOTALL)
        
        if '</body>' in c:
            c = c.replace('</body>', inject_js + '\n</body>')
        else:
            c = c + inject_js
            
        with open(fn, "w", encoding="utf-8") as f:
            f.write(c)

print("Resume/CV Maker hat gaya aur Mernal Water Order 100% sahi jagah lag gaya!")
