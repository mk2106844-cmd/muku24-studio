import os, re

hacker_code = '''
<style id="muku3p-hacker-theme">
  /* 1. Full Dark Cyber-Blue Hacker Background */
  html, body {
    background-color: #050814 !important;
    background-image: 
      radial-gradient(circle at 50% 0%, rgba(0, 240, 255, 0.12) 0%, transparent 60%),
      linear-gradient(rgba(0, 240, 255, 0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0, 240, 255, 0.03) 1px, transparent 1px) !important;
    background-size: 100% 100%, 24px 24px, 24px 24px !important;
    color: #e2e8f0 !important;
  }

  /* 2. Top Navbar / Header Hacker Glass Look */
  header, nav, .sticky, .fixed.top-0, .bg-white {
    background-color: #0a1024 !important;
    color: #e2e8f0 !important;
    border-color: rgba(0, 240, 255, 0.25) !important;
  }

  /* Muku3p Brand Neon Glow */
  header a, nav a, .font-bold {
    color: #f8fafc !important;
  }
  header .text-sky-600, nav .text-sky-600, [class*="logo"], header a:first-of-type {
    color: #00f0ff !important;
    text-shadow: 0 0 10px rgba(0, 240, 255, 0.6) !important;
    font-family: monospace !important;
    letter-spacing: 1px !important;
  }

  /* 3. Hero Banner Cyber Matrix Look */
  section:first-of-type {
    background: linear-gradient(180deg, #070d24 0%, #050814 100%) !important;
    border-bottom: 1px solid rgba(0, 240, 255, 0.3) !important;
    box-shadow: 0 10px 30px rgba(0, 240, 255, 0.08) !important;
  }

  /* Headings & Numbers (50+, 100K+) Neon Cyan */
  h1, h2, h3, h4 {
    color: #ffffff !important;
  }
  p, span, div {
    color: #94a3b8;
  }

  /* 4. Tool Cards - Compact, Equal Height & Neon Border */
  .grid > div {
    background: #0b132b !important;
    border: 1px solid rgba(0, 240, 255, 0.28) !important;
    border-radius: 14px !important;
    box-shadow: 0 0 15px rgba(0, 240, 255, 0.06), inset 0 0 12px rgba(0, 240, 255, 0.03) !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    overflow: hidden !important;
    transition: all 0.2s ease !important;
  }
  .grid > div:hover, .grid > div:active {
    border-color: #00f0ff !important;
    box-shadow: 0 0 20px rgba(0, 240, 255, 0.35) !important;
    transform: translateY(-2px) !important;
  }

  /* 5. FIX CROPPED IMAGES: Koi bhi photo side se nahi kategi! */
  .grid > div img {
    width: 100% !important;
    height: 115px !important;
    object-fit: contain !important;
    background: #060b19 !important;
    padding: 6px !important;
    border-radius: 10px !important;
    border: 1px solid rgba(0, 240, 255, 0.15) !important;
    margin-bottom: 8px !important;
  }

  /* Image ke bahar wale pastel dabbe ko dark hacker box banana */
  .grid > div > div:first-child {
    background: transparent !important;
    padding: 8px 8px 0 8px !important;
  }

  /* 6. Mobile App Perfect Compact Text & Alignment */
  .grid > div h3, .grid > div h2, .grid > div .font-bold {
    color: #00f0ff !important;
    font-size: 14px !important;
    line-height: 1.3 !important;
    margin-bottom: 4px !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 1 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
  }

  .grid > div p {
    color: #94a3b8 !important;
    font-size: 11.5px !important;
    line-height: 1.35 !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    margin-bottom: 10px !important;
    height: 32px !important;
  }

  /* 7. Open Tool Button - Full Width Cyber Neon Button */
  .grid > div a, .grid > div button, a[class*="bg-sky-"], button[class*="bg-sky-"] {
    background: linear-gradient(90deg, #0284c7 0%, #00f0ff 100%) !important;
    color: #020617 !important;
    font-weight: 800 !important;
    font-size: 12.5px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    border-radius: 8px !important;
    padding: 8px 12px !important;
    width: 100% !important;
    text-align: center !important;
    display: block !important;
    box-shadow: 0 0 12px rgba(0, 240, 255, 0.4) !important;
    border: none !important;
  }

  /* Grid Layout for Mobile & Desktop */
  aside, [class*="sidebar"] {
    display: none !important;
  }
  .grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)) !important;
    gap: 14px !important;
    padding: 8px !important;
  }
  @media (max-width: 640px) {
    .grid {
      grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
      gap: 10px !important;
      padding: 6px !important;
    }
  }
</style>

<script id="muku3p-hacker-js">
function enforceHackerLook() {
  document.querySelectorAll('div, aside').forEach(el => {
    const txt = (el.innerText || '').trim();
    // 1. Fake popup (Amit Kumar / Rahul Sharma / Just now) ko 100% hatana
    if ((txt.includes('Just now') || txt.includes('used ')) && el.offsetHeight < 160 && el.offsetWidth < 380) {
      el.style.setProperty('display', 'none', 'important');
      el.remove();
    }
    // 2. Left Categories box hatana
    if (txt.startsWith('Categories') && txt.includes('Need Help?') && el.offsetWidth < 360) {
      el.style.setProperty('display', 'none', 'important');
    }
  });
}
setInterval(enforceHackerLook, 400);
window.addEventListener('DOMContentLoaded', enforceHackerLook);
</script>
'''

for fn in ["csc.html", "index.html", "new.html", "final.html"]:
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8", errors="ignore") as f:
            h = f.read()

        # Purane styles aur scripts hatana
        h = re.sub(r'<style id="muku3p-.*?">.*?</style>', '', h, flags=re.DOTALL)
        h = re.sub(r'<script id="muku3p-.*?">.*?</script>', '', h, flags=re.DOTALL)

        # Naya Blue Hacker Theme lagana
        if '</body>' in h:
            h = h.replace('</body>', hacker_code + '\n</body>')
        else:
            h = h + hacker_code

        with open(fn, "w", encoding="utf-8") as f:
            f.write(h)

print("Blue Hacker Theme + Mobile App Cards 100% Ready!")
