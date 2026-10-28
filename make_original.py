import os, re

# Safe CSS jo sirf copy-wala laal color badlega aur fake popup chupayega
safe_style = '''
<style id="muku3p-clean-brand">
  /* 1. Fake popup (Rahul Sharma) ko hamesha ke liye gayab karna */
  #notification-popup, .notification-popup, [id*="popup"], [class*="toast"], .fixed.bottom-4.left-4, .fixed.bottom-5.left-5 {
    display: none !important;
    opacity: 0 !important;
    pointer-events: none !important;
  }

  /* 2. Copy wala Maroon/Red banner hatakar Muku3p Royal Indigo Banner */
  .bg-gradient-to-r, .from-red-700, .bg-red-700, .bg-red-800, [style*="#991b1b"], [style*="#b91c1c"], [style*="#be123c"] {
    background: linear-gradient(135deg, #1e1b4b 0%, #4338ca 50%, #3b82f6 100%) !important;
  }

  /* 3. Open Tool buttons aur Active tabs ko Indigo-Blue banana (Text hamesha safed rahega) */
  .bg-red-600, .bg-rose-600, .bg-red-700, .bg-rose-700, button.bg-red-600, a.bg-red-600 {
    background-color: #4338ca !important;
    color: #ffffff !important;
    border-color: #4338ca !important;
  }

  /* 4. Numbers (50+, 100K+) aur Logo ka laal rang badalna */
  .text-red-600, .text-rose-600, .text-red-700, .text-rose-700 {
    color: #4338ca !important;
  }

  /* 5. Card hover border ko Indigo karna */
  .hover\\:border-red-500:hover, .border-red-500 {
    border-color: #4338ca !important;
  }
</style>
'''

for fn in ["csc.html", "index.html", "new.html", "final.html"]:
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()

        # Purane extra styles hatana agar pehle ke bache hon
        c = re.sub(r'<style id="mukesh-custom-app-theme">.*?</style>', '', c, flags=re.DOTALL)
        c = re.sub(r'<style id="muku3p-clean-brand">.*?</style>', '', c, flags=re.DOTALL)
        c = re.sub(r'<div class="app-search-wrap">.*?</script>', '', c, flags=re.DOTALL)

        # 1. Website ka Naam aur Text Muku3p karna
        c = re.sub(r'<title>.*?</title>', '<title>Muku3p - All-in-One Digital Tools</title>', c, flags=re.I)
        c = c.replace("Mukesh CSC Tools", "Muku3p")
        c = c.replace("Muku3p Digital", "Muku3p")
        c = c.replace("Smart CSC Tools", "Muku3p")
        c = c.replace("smartcsctools", "muku3p")

        # 2. Copy-paste wali lines badalna
        c = c.replace("Our Tools Collection", "Muku3p Smart Tools")
        c = re.sub(r'CSC VLE के लिए 100% Free & Usefull Smart Tools\.?', 'All-in-One Fast, Free & Smart Digital Workspace by Muku3p.', c)
        c = re.sub(r'Muku3p ke liye 100% Free & Usefull Smart Tools\.?', 'All-in-One Fast, Free & Smart Digital Workspace by Muku3p.', c)
        c = re.sub(r"India's Most Trusted.*?100% Free -", "CREATE • EDIT • AUTOMATE — Fast & Smart Digital Utilities by Muku3p", c, flags=re.DOTALL)
        c = c.replace("View All CSC Tools", "Explore Muku3p Tools")
        c = c.replace("Active CSC Users", "Happy Users")

        # 3. Upar ke faltu menu links ko clean karna
        c = c.replace(">CSC Billing<", "><")
        c = c.replace(">CSC Work<", "><")
        c = c.replace(">Videos<", "><")
        c = c.replace(">Blog<", "><")

        # 4. Rahul Sharma popup text hatana
        c = c.replace("Rahul Sharma", "")

        # 5. Safe CSS jodna
        if '</head>' in c:
            c = c.replace('</head>', safe_style + '\n</head>')
        else:
            c = safe_style + c

        with open(fn, "w", encoding="utf-8") as f:
            f.write(c)

print("Muku3p Original Look Ready!")
