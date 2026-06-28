from pathlib import Path
import re, base64
p = Path('index-old.html')
s = p.read_text(encoding='utf-8', errors='ignore')
matches = re.findall(r'src="(data:image/(png|webp);base64,([A-Za-z0-9+/=\n\r]+))"', s)
out = Path('assets')
out.mkdir(exist_ok=True)
if not matches:
    print('no matches')
else:
    for i, m in enumerate(matches):
        full = m[0]
        mime = m[1]
        b64 = m[2]
        b64 = re.sub(r'\s+', '', b64)
        ext = 'png' if mime=='png' else 'webp'
        data = base64.b64decode(b64)
        outp = out / f'family_from_index_old_{i}.{ext}'
        outp.write_bytes(data)
        print('wrote', outp)
