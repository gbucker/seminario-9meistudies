"""Monta index.html a partir de src/: esqueleto + slides + notas."""
import re
from pathlib import Path

root = Path(__file__).parent
sk = (root / "src/skeleton.html").read_text(encoding="utf-8")
sl = (root / "src/slides.html").read_text(encoding="utf-8")
notes = (root / "src/notes.js").read_text(encoding="utf-8")

a, b = sk.index("<!-- 00 -->"), sk.index('<div id="notes">')
out = sk[:a] + sl + "\n" + sk[b:]
out = re.sub(r"const NOTES=\{.*?\n\};", lambda m: notes, out, flags=re.S)
out = out.replace('const TR={ex:{en:"original sentence in English",pt:"frase original em português"}};', "const TR={};")
out = out.replace("H.traducao={step(s,n,jump){if(n===1&&!jump){trSet('ex',false);setTimeout(()=>trAnim('ex',true),700);}else if(n>=1)trSet('ex',true);}};", "")
out = out.replace("<title>TÍTULO CURTO</title>", "<title>Limites semióticos do humor computacional · MEISTUDIES</title>")
out = out.replace("agent@seminario", "agent@meistudies")
(root / "index.html").write_text(out, encoding="utf-8")
print("index.html gerado")
