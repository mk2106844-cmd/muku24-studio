import os, re

# 1. Naye Tool ke liye Sundar SVG Poster Image banana
svg_banner = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="100%" stop-color="#2563eb"/>
    </linearGradient>
  </defs>
  <rect width="400" height="220" rx="16" fill="url(#bg)"/>
  <circle cx="350" cy="40" r="60" fill="#ffffff" fill-opacity="0.08"/>
  <circle cx="50" cy="180" r="70" fill="#ffffff" fill-opacity="0.06"/>
  <rect x="130" y="30" width="140" height="32" rx="16" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="200" y="51" font-family="sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">✨ NEW SERVICE</text>
  <text x="200" y="115" font-family="sans-serif" font-size="30" font-weight="900" fill="#ffffff" text-anchor="middle">Muku24 App</text>
  <text x="200" y="150" font-family="sans-serif" font-size="15" font-weight="600" fill="#bfdbfe" text-anchor="middle">Smart Online Portal Tool</text>
</svg>'''

with open("netlify_tool.svg", "w", encoding="utf-8") as f:
    f.write(svg_banner)

# 2. JavaScript jo page khulte hi 1st Card ki exact design copy karke naya tool #1 par laga dega
inject_js = '''
<script id="muku24-netlify-injector">
function addNetlifyCard() {
  if (document.getElementById('muku24-special-netlify-card')) return;
  
  // Resume/CV Maker ya UP Bhulekh wala card dhoondhna
  const allHeadings = document.querySelectorAll('h3, h4, h2, div.font-bold');
  let targetCard = null;
  
  for (let el of allHeadings) {
    if (el.innerText && (el.innerText.includes('Resume/CV Maker') || el.innerText.includes('UP Bhulekh'))) {
      targetCard = el.closest('.grid > div') || el.parentElement.parentElement;
      break;
    }
  }

  if (targetCard && targetCard.parentElement) {
    // Pehle card ka exact clone banana taaki design 100% same rahe
    const newCard = targetCard.cloneNode(true);
    newCard.id = 'muku24-special-netlify-card';
    
    // Photo badalna
    const img = newCard.querySelector('img');
    if (img) {
      img.src = 'netlify_tool.svg?v=1';
      img.alt = 'Muku24 Special Tool';
    }
    
    // Heading (Naam) badalna
    const title = newCard.querySelector('h3, h4, h2, .font-bold');
    if (title) {
      title.innerText = 'Muku24 Special Portal';
    }
    
    // Description badalna
    const desc = newCard.querySelector('p');
    if (desc) {
      desc.innerText = 'Muku24 Studio ka naya online digital tool. Direct use karne ke liye Open Tool par click karein.';
    }
    
    // Link (Open Tool button) badalna
    const link = newCard.querySelector('a, button');
    if (link) {
      if (link.tagName === 'A') {
        link.href = 'https://calm-elf-a7af6e.netlify.app/';
        link.target = '_blank';
        link.removeAttribute('onclick');
      } else {
        link.onclick = function() { window.open('https://calm-elf-a7af6e.netlify.app/', '_blank'); };
      }
      link.innerText = 'Open Tool';
    }
    
    // Sabse aage (1st Number par) lagana
    targetCard.parentElement.insertBefore(newCard, targetCard);
  }
}

window.addEventListener('DOMContentLoaded', addNetlifyCard);
window.addEventListener('load', addNetlifyCard);
setTimeout(addNetlifyCard, 300);
</script>
'''

for fn in ["csc.html", "index.html", "new.html", "final.html"]:
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
            
        # Purana broken code hatana
        c = re.sub(r'<script id="muku24-netlify-injector">.*?</script>', '', c, flags=re.DOTALL)
        
        if '</body>' in c:
            c = c.replace('</body>', inject_js + '\n</body>')
        else:
            c = c + inject_js
            
        with open(fn, "w", encoding="utf-8") as f:
            f.write(c)

print("Naya Tool 1st Number par 100% Jud Gaya!")
