from pathlib import Path

root = Path(__file__).resolve().parent
p = root / "assets/static/js/main.29e3c7d8.js"
text = p.read_text(encoding="utf-8")

text = text.replace('concat(_.name,', 'concat(n,', 2)

p.write_text(text, encoding="utf-8")
print("patched")