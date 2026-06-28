from pathlib import Path
import re,base64
arch = Path('archiv')
out = Path('assets')
out.mkdir(exist_ok=True)
count=0
for p in arch.glob('*.html'):
    t=p.read_text(encoding='utf-8',errors='ignore')
    for m in re.finditer(r'src=\"(data:image/(png|webp);base64,([A-Za-z0-9+/=]+))\"', t):
        full=m.group(1)
        ext = 'png' if m.group(2)=='png' else 'webp'
        b64 = m.group(3)
        data = base64.b64decode(b64)
        outp = out/ f'extracted_{p.stem}_{count}.{ext}'
        outp.write_bytes(data)
        print('wrote', outp)
        count+=1
print('done',count)
