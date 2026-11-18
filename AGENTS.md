# AGENTS.md

Apresentação em HTML único, estética terminal neon (palco fixo 1600×900).

- Não edite `index.html` à mão. Edite os arquivos em `src/` e rode `python3 build.py`.
  - `src/skeleton.html`: CSS e motor (passos, console, notas, índice).
  - `src/slides.html`: as seções `<section class="slide">`, na ordem da apresentação.
  - `src/notes.js`: objeto `NOTES` com as notas por `data-id`.
- Magenta (`.mine`, `.badge`, `.q.mine`) marca leituras do apresentador; não use como decoração.
- Citações diretas são literais, com página.
- Antes de publicar, percorra todos os slides com Playwright e confira as capturas (sem texto sobre o rodapé).
