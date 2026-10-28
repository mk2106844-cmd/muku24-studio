import http.server, socketserver, os, re, time, shutil

DIRECTORY = os.path.expanduser('~/rea')

HTML_PAGE = '''<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Upload Kisan Card</title>
<style>
  body { font-family: sans-serif; text-align: center; padding: 25px; background: #f0f2f5; margin: 0; }
  .card { background: #fff; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-width: 380px; margin: 30px auto; }
  h2 { color: #333; margin-top: 0; font-size: 20px; }
  input[type=file] { margin: 20px 0; font-size: 15px; width: 100%; }
  button { background: #e11d48; color: white; border: none; padding: 12px 20px; font-size: 16px; border-radius: 8px; font-weight: bold; width: 100%; cursor: pointer; }
  #status { margin-top: 15px; font-weight: bold; font-size: 15px; }
</style>
</head>
<body>
<div class="card">
  <h2>किसान कार्ड की फ़ोटो चुनें</h2>
  <p style="color:#666; font-size:14px;">गैलरी से सीता कुमारी वाली किसान कार्ड की फ़ोटो सेलेक्ट करें</p>
  <input type="file" id="photoInput" accept="image/*">
  <button onclick="uploadPhoto()">वेबसाइट पर फ़ोटो लगाएँ</button>
  <div id="status"></div>
</div>
<script>
function uploadPhoto() {
  const file = document.getElementById('photoInput').files[0];
  if(!file) { alert('कृपया पहले फ़ोटो सेलेक्ट करें!'); return; }
  const st = document.getElementById('status');
  st.style.color = '#0066cc';
  st.innerText = 'फ़ोटो अपलोड हो रही है...';
  
  fetch('/save_kisan_card', { method: 'POST', body: file })
    .then(r => r.text())
    .then(res => {
      st.style.color = 'green';
      st.innerHTML = '✅ फ़ोटो लग गई!<br><br><a href="/index.html" style="color:#e11d48; font-size:16px;">यहाँ क्लिक करके वेबसाइट देखें</a>';
    })
    .catch(err => {
      st.style.color = 'red';
      st.innerText = 'एरर आया, दोबारा कोशिश करें।';
    });
}
</script>
</body>
</html>'''

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == '/upload':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML_PAGE.encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/save_kisan_card':
            length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(length)
            
            img_path = os.path.join(DIRECTORY, 'kisan.jpg')
            with open(img_path, 'wb') as f:
                f.write(data)
            
            v = str(int(time.time()))
            for fn in ['csc.html', 'index.html']:
                fp = os.path.join(DIRECTORY, fn)
                if os.path.exists(fp):
                    with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
                        c = f.read()
                    c = re.sub(r'https?://[^\s"\'<>]*imgbb[^\s"\'<>]*', 'kisan.jpg?v=' + v, c, flags=re.I)
                    c = re.sub(r'https://play-lh\.googleusercontent\.com/[^\s"\'<>]+', 'kisan.jpg?v=' + v, c)
                    with open(fp, 'w', encoding='utf-8') as f:
                        f.write(c)
            
            if os.path.exists(os.path.join(DIRECTORY, 'csc.html')):
                shutil.copy(os.path.join(DIRECTORY, 'csc.html'), os.path.join(DIRECTORY, 'index.html'))
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'SUCCESS')
        else:
            self.send_error(404)

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(('', 8080), Handler) as httpd:
    httpd.serve_forever()
