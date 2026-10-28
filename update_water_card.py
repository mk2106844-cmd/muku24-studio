import os, re

# 2. Agar screenshot folder me na mile toh bilkul aapki photo jaisa 3D Blue Water Jar banana
svg_water = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="100%">
  <defs>
    <linearGradient id="jarBody" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="25%" stop-color="#7dd3fc"/>
      <stop offset="50%" stop-color="#e0f2fe"/>
      <stop offset="80%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="jarDark" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#0369a1" stop-opacity="0.9"/>
    </linearGradient>
  </defs>
  <rect width="400" height="300" fill="#ffffff"/>
  <!-- Tilted Second Jar in Background -->
  <g transform="translate(260, 195) rotate(78)">
    <rect x="-20" y="-105" width="40" height="16" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2"/>
    <rect x="-15" y="-89" width="30" height="22" fill="#0284c7"/>
    <path d="M-15,-67 L-65,-35 L65,-35 L15,-67 Z" fill="url(#jarBody)"/>
    <rect x="-65" y="-35" width="130" height="125" rx="14" fill="url(#jarBody)" stroke="#0284c7" stroke-width="2"/>
    <rect x="-67" y="-5" width="134" height="14" rx="6" fill="url(#jarDark)"/>
    <rect x="-67" y="40" width="134" height="14" rx="6" fill="url(#jarDark)"/>
  </g>
  <!-- Standing Main 20L Water Jar -->
  <g transform="translate(115, 20)">
    <!-- White Cap -->
    <rect x="-22" y="0" width="44" height="18" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
    <!-- Neck -->
    <rect x="-16" y="18" width="32" height="26" fill="#0284c7"/>
    <!-- Shoulder -->
    <path d="M-16,44 L-75,80 L75,80 L16,44 Z" fill="url(#jarBody)" stroke="#38bdf8" stroke-width="1"/>
    <!-- Main Cylinder Body -->
    <rect x="-75" y="80" width="150" height="165" rx="16" fill="url(#jarBody)" stroke="#0284c7" stroke-width="2"/>
    <!-- 3D Ribs/Rings -->
    <rect x="-77" y="115" width="154" height="16" rx="7" fill="url(#jarDark)"/>
    <rect x="-77" y="170" width="154" height="16" rx="7" fill="url(#jarDark)"/>
    <rect x="-75" y="222" width="150" height="23" rx="10" fill="url(#jarDark)"/>
    <!-- Shine/Reflection -->
    <rect x="-45" y="88" width="18" height="145" rx="9" fill="#ffffff" fill-opacity="0.55"/>
  </g>
</svg>'''

with open("water_jar.svg", "w", encoding="utf-8") as f:
    f.write(svg_water)

img_file = "water_order.png?v=2" if os.path.exists("water_order.png") else "water_jar.svg?v=2"

# 3. Card Injector Script (Mernal Water Oder + Water Description + Fresh Data Link)
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
    
    // Photo lagana
    const img = newCard.querySelector('img');
    if (img) {{
      img.src = '{img_file}';
      img.alt = 'Mernal Water Oder';
      img.style.objectFit = 'contain';
      img.style.background = '#ffffff';
    }}
    
    // Naam: Mernal Water Oder
    const title = newCard.querySelector('h3, h4, h2, .font-bold');
    if (title) {{
      title.innerText = 'Mernal Water Oder';
    }}
    
    // Description: Water Order ke liye
    const desc = newCard.querySelector('p');
    if (desc) {{
      desc.innerText = 'Shuddh aur thanda 20L Mineral Water Jar ghar, dukan ya shaadi-party ke liye online book aur order karein.';
    }}
    
    // Open Tool Button (Fresh session parameter ke saath taaki purana data na aaye)
    const link = newCard.querySelector('a, button');
    const freshUrl = 'https://calm-elf-a7af6e.netlify.app/?new_order=' + new Date().getTime();
    if (link) {{
      if (link.tagName === 'A') {{
        link.href = freshUrl;
        link.target = '_blank';
        link.removeAttribute('onclick');
      }} else {{
        link.onclick = function() {{ window.open(freshUrl, '_blank'); }};
      }}
      link.innerText = 'Order Now / Open Tool';
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

print("Mernal Water Oder Card + Water Photo + Description 100% Updated!")
