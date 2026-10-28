import glob, os, re

# Custom CSS for Mobile-First App Design
custom_style = '''
<style id="mukesh-custom-app-theme">
  :root {
    --primary: #0f172a;
    --accent: #2563eb;
    --accent-glow: #38bdf8;
    --bg-soft: #f8fafc;
    --card-bg: #ffffff;
    --text-main: #1e293b;
    --text-muted: #64748b;
  }

  body {
    background-color: var(--bg-soft) !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    padding-bottom: 75px !important;
  }

  /* Modern Mobile Header */
  header, .header, nav, .navbar {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%) !important;
    box-shadow: 0 4px 20px rgba(15, 23, 42, 0.25) !important;
    border-radius: 0 0 20px 20px !important;
  }

  /* Live Search Box Container */
  .app-search-wrap {
    max-width: 500px;
    margin: 15px auto 25px auto;
    padding: 0 16px;
  }
  .app-search-input {
    width: 100%;
    padding: 13px 20px;
    border-radius: 50px;
    border: 1.5px solid #cbd5e1;
    background: #ffffff;
    font-size: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    outline: none;
    box-sizing: border-box;
    transition: all 0.2s ease;
  }
  .app-search-input:focus {
    border-color: #2563eb;
    box-shadow: 0 4px 16px rgba(37,99,235,0.2);
  }

  /* Card Redesign */
  .grid > div, [class*="rounded-"], .card {
    border-radius: 18px !important;
    border: 1px solid #e2e8f0 !important;
    background: #ffffff !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.04) !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
    overflow: hidden !important;
  }
  .grid > div:active, .card:active {
    transform: scale(0.98) !important;
  }

  /* Buttons Styling */
  a[class*="bg-red-"], button[class*="bg-red-"], .btn, a[href*="tool"] {
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: #ffffff !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    box-shadow: 0 3px 10px rgba(37,99,235,0.3) !important;
    border: none !important;
  }

  /* Mobile App Bottom Navigation */
  .app-bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 62px;
    background: #ffffff;
    display: flex;
    justify-content: space-around;
    align-items: center;
    border-top: 1px solid #e2e8f0;
    box-shadow: 0 -4px 15px rgba(0,0,0,0.06);
    z-index: 9999;
  }
  .app-bottom-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: 11px;
    color: #64748b;
    text-decoration: none;
    font-weight: 600;
  }
  .app-bottom-item svg {
    width: 22px;
    height: 22px;
    margin-bottom: 3px;
    fill: currentColor;
  }
  .app-bottom-item.active {
    color: #2563eb;
  }

  /* Floating WhatsApp Button */
  .wa-float-btn {
    position: fixed;
    right: 16px;
    bottom: 76px;
    background: #22c55e;
    color: white;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 6px 18px rgba(34,197,94,0.4);
    z-index: 9998;
    text-decoration: none;
  }
</style>
'''

# Mobile App JavaScript (Live Instant Search)
custom_js = '''
<div class="app-search-wrap">
  <input type="text" id="toolSearchInput" class="app-search-input" placeholder="🔍 Search CSC Tools (Kisan, PDF, Resume...)" onkeyup="filterTools()">
</div>

<div class="app-bottom-nav">
  <a href="/index.html" class="app-bottom-item active">
    <svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
    Home
  </a>
  <a href="#tools" class="app-bottom-item">
    <svg viewBox="0 0 24 24"><path d="M4 8h4V4H4v4zm6 12h4v-4h-4v4zm-6 0h4v-4H4v4zm0-6h4v-4H4v4zm6 0h4v-4h-4v4zm6-10v4h4V4h-4zm-6 4h4V4h-4v4zm6 6h4v-4h-4v4zm0 6h4v-4h-4v4z"/></svg>
    All Tools
  </a>
  <a href="https://wa.me/918700353999?text=Hello%20Mukesh%20Ji,%20CSC%20Service%20chahiye" target="_blank" class="app-bottom-item">
    <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.82.49 3.53 1.35 5L2 22l5.13-1.33c1.43.82 3.09 1.33 4.87 1.33 5.52 0 10-4.48 10-10S17.52 2 12 2zm1 14h-2v-2h2v2zm0-4h-2V7h2v5z"/></svg>
    Support
  </a>
</div>

<a href="https://wa.me/918700353999?text=Hello%20Mukesh%20Ji" target="_blank" class="wa-float-btn" title="WhatsApp Help">
  <svg width="28" height="28" viewBox="0 0 24 24" fill="white"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-5.46-4.45-9.92-9.91-9.92z"/></svg>
</a>

<script>
function filterTools() {
  let q = document.getElementById("toolSearchInput").value.toLowerCase();
  let cards = document.querySelectorAll(".grid > div, .card, [class*='p-4'], [class*='p-6']");
  cards.forEach(card => {
    let txt = card.innerText.toLowerCase();
    if(card.closest('.app-bottom-nav') || card.closest('.app-search-wrap') || card.closest('header')) return;
    if(txt.length > 5) {
      if(txt.includes(q)) {
        card.style.display = "";
      } else {
        card.style.display = "none";
      }
    }
  });
}
</script>
'''

for fn in ['csc.html', 'index.html', 'new.html', 'final.html']:
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        
        # Purana custom style hatana agar ho to
        c = re.sub(r'<style id="mukesh-custom-app-theme">.*?</style>', '', c, flags=re.DOTALL)
        
        # Naya Style head me inject karna
        if '</head>' in c:
            c = c.replace('</head>', custom_style + '\n</head>')
        else:
            c = custom_style + c
            
        # Naya Mobile Search aur Bottom Nav body ke end me jodna
        if '</body>' in c:
            c = c.replace('</body>', custom_js + '\n</body>')
        else:
            c = c + custom_js
            
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)

print('Mobile-First App Theme Successfully Injected!')
