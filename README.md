# Modern Power BI Semantic Modeling – materiały szkoleniowe

Dane testowe, pliki startowe i ćwiczenia (laby) do 3-dniowego szkolenia.
Wszystkie dane są fikcyjne: **Vistula Outdoor Co.** – firma sprzedająca sprzęt outdoorowy i sportowy
klientom biznesowym w regionach EMEA, Americas i APAC.

*English version: [en/README.md](en/README.md)*

## Przed Dniem 1 – instalacja

| Narzędzie | Potrzebne do | Link |
|---|---|---|
| Power BI Desktop (najnowszy) | wszystkie dni | https://aka.ms/pbidesktopstore |
| DAX Studio | Dzień 1 (Lab 1.3), Dzień 2 | https://daxstudio.org |
| Tabular Editor 2 (darmowy) | Dzień 2 | https://github.com/TabularEditor/TabularEditor/releases |
| VS Code + rozszerzenie TMDL, Git | Dzień 3 | https://code.visualstudio.com · https://git-scm.com |

## Co jest w repozytorium

```
data/                pliki CSV (UTF-8, separator przecinek, format liczb en-US)
  D_Date.csv           kalendarz 2022–2026, w tym rok fiskalny (od 1 lipca) i tygodnie ISO
  D_Product.csv        260 produktów: Category › Subcategory › Product
  D_Customer.csv       4 000 klientów biznesowych z segmentem
  D_Geography.csv      42 miasta: Region › Country › City
  D_Employee.csv       organizacja sprzedaży (parent-child), używana w Dniu 2
  F_Sales_2022.csv …   pozycje zamówień sprzedaży, jeden plik na rok (sty 2022 – paź 2026, ~527 tys. pozycji)
  F_Budget.csv         budżet o granularności miesiąc × kategoria × region
  Sales_Flat_2025.csv  jeden zdenormalizowany extract (używany w demo trenera)
day1/
  Day1_start.pbix      plik startowy do wszystkich labów Dnia 1
  Lab_1.1_Budget.md
  Lab_1.2_Calculation_Group.md
  Lab_1.3_VertiPaq.md
generator/
  generate_data.py     jak wygenerowano dane (deterministycznie)
en/                  wersja angielska instrukcji
```

## Jak korzystać z pliku startowego

`Day1_start.pbix` zawiera już dane – otwórz go i zacznij lab.

Przy odświeżeniu dane są pobierane z tego repozytorium przez parametr Power Query **DataSource**.
Jeśli GitHub jest zablokowany w Twojej sieci:

1. Pobierz repozytorium jako ZIP (zielony przycisk **Code** → *Download ZIP*) i rozpakuj, np. do `C:\PBI-Training\`.
2. W Power BI Desktop: **Transform data → Edit parameters → DataSource** = `C:\PBI-Training\data\`
   (z ukośnikiem na końcu).
3. Odśwież dane (**Refresh**).

Każdy lab zaczyna się od pliku startowego danego dnia. Laby nie zależą od siebie – jeśli pominiesz jeden,
możesz zrobić następny.
