# 👾 Moja strona Jekyll

To jest statyczna strona internetowa oparta na [Jekyll](https://jekyllrb.com/), hostowana na [GitHub Pages](https://pages.github.com/), znajdziejsz ją pod adresem [jaqbiak](https://jaqbiak.space)

## 🛠️ Wymagania

Aby uruchomić stronę lokalnie, potrzebujesz:

- Ruby (zalecana wersja: `3.1.x`) – zarządzaj wersjami przez [`rbenv`](https://github.com/rbenv/rbenv)
- Bundler
- Git
- System macOS, Linux lub Windows (zalecany WSL)

## 🚀 Uruchamianie lokalnie

1. **Zainstaluj Ruby** (np. przez `rbenv`):
    ```bash
    rbenv install 3.1.4
    rbenv global 3.1.4
2. **Zainstaluj Bundler**:
    ```bash
    gem install bundler
    bundle install
3. **Uruchom serwer lokalny Jekyll**:
    ```bash
    bundle exec jekyll serve
4. **Otwórz stronę w przeglądarce pod adresem**:
    ```bash
    http://localhost:4000