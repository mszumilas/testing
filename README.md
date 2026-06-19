# Testy E2E Playwright – ING.pl (Cookies)

## 📌 Opis projektu

Projekt zawiera automatyczne testy E2E dla strony **ING.pl**, napisane w Python + Playwright.  
Głównym celem jest:

- obsługa bannera cookies ING,
- akceptacja wymaganych i analitycznych cookies,
- walidacja, że cookies analityczne zostały ustwaione,
- walidacja, że żadne cookies marketingowe nie zostały ustawione,
- uruchamianie testów na Chrome i Firefox.


---

## 🧰 Wymagania

- Python 3.9+
- Playwright 1.40+
- pytest
- pip

---

## 📦 Instalacja

```bash
pip install pytest pytest-playwright
playwright install
```

---

## 🌐 Uruchamianie testów na Chrome i Firefox

```bash
pytest
```
W celu zmiany przegladarek należy zmienić konfiguracje w pliku conftest.py linijka 22 i wpisać w parametry żądane przeglądarki. 

W celu uruchomienia testów bez trybu headless należy zmienić w pliku conftest.py w linijce 28 (headless=True) na (headless=False).
