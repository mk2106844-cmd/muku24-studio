import os, re, urllib.request

# 1. Netlify wale Water App ko local save karke usme se aapka purana bhara hua data auto-clear karna
try:
    req = urllib.request.Request(
        "https://calm-elf-a7af6e.netlify.app/", 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    html_app = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
    
    # Har baar form khali rakhne aur purana saved data hatane ka script
    clear_data_script = """
    <head>
    <base href="https://calm-elf-a7af6e.netlify.app/">
    <script>
      // Purana bhara hua data hatana
      try {
        localStorage.clear();
        sessionStorage.clear();
      } catch(e) {}
      window.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('input, textarea, select').forEach(el => {
          if (el.type !== 'submit' && el.type !== 'button') {
            el.value = '';
          }
        });
      });
    </script>
    """
    html_app = re.sub(r'<head>', clear_data_script, html_app, count=1, flags=re.I)
    with open("water_order_app.html", "w", encoding="utf-8") as f:
        f.write(html_app)
    app_url = "water_order_app.html?v=1"
except Exception as e:
    app_url = "https://calm-elf-a7af6e.netlify.app/"

img_file = "water_order.png?v=3" if os.path.exists("water_order.png") else "water_jar.svg?v=3"

# 2. Card par Sahi Naam aur Description lagana
inject_js = f'''
<script id="muku24-netlify-injector">
function addNetlifyCard() {{
  const existing = document.getElementById('muku24-special-netlify-card');
  if (existing) existing.remove();
  
  const allHeadings = document.querySelectorAll('h3, h4, h2, div.font-bold');
  let targetCard = null;
  
  for (let el of allHeadings) {{
    if (el.innerText && (el.innerText.includes('Resume/CV Maker') || el.innerText.includes('UP Bhulekh'))) {{
      targetCard = el.closest('.grid > div') || el.parentElement.parentElement;
      break;
    }}
  }}

  if (targetCard && targetCard.parentElement) {{
    const newCard = targetCard.cloneNode(true);
    newCard.id = 'muku24-special-netlify-card';
    
    const img = newCard.querySelector('img');
    if (img) {{
      img.src = '{img_file}';
      img.alt = 'Mernal Water Order';
      img.style.objectFit = 'contain';
      img.style.background = '#ffffff';
    }}
    
    // NAME (TITLE)
    const title = newCard.querySelector('h3, h4, h2, .font-bold');
    if (title) {{
      title.innerText = 'Mernal Water Order (मिनरल वाटर आर्डर)';
    }}
    
    // DESCRIPTION
    const desc = newCard.querySelector('p');
    if (desc) {{
      desc.innerText = 'Ghar, dukan ya shaadi-party ke liye 20L RO chilled water jar online book karein. (घर या पार्टी के लिए पानी आर्डर करें।)';
    }}
    
    // OPEN TOOL BUTTON
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
setTimeout(addNetlifyCard, 300);
</script>
'''

for fn in ["csc.html", "index.html", "new.html", "final.html"]:
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
            
        c = re.sub(r'<script id="muku24-netlify-injector">.*?</script>', '', c, flags=re.DOTALL)
        
        if '</body>' in c:
            c = c.replace('</body>', inject_js + '\n</body>')
        else:
            c = c + inject_js
            
        with open(fn, "w", encoding="utf-8") as f:
            f.write(c)

print("Name, Description aur Fresh Form 100% Set ho gaya!")
