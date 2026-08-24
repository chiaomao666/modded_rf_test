from pathlib import Path
p = Path('assets/static/js/main.29e3c7d8.js')
text = p.read_text(encoding='utf-8')
text = text.replace('concat(_.name, "？預計將於")', 'concat(n, "？預計將於")')
text = text.replace('concat(_.name, " 需要")', 'concat(n, " 需要")')
p.write_text(text, encoding='utf-8')
print('patched')
