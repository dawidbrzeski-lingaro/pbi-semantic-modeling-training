# Lab 1.1 – Druga tabela faktów: wykonanie vs budżet

**Moduł 3A · ok. 20 min · start z `Day1_start.pbix`**

Budżet jest planowany z mniejszą szczegółowością (granularnością) niż sprzedaż: **miesiąc × kategoria produktu × region**.
Dodajesz go jako osobną tabelę faktów i budujesz miary wykonanie vs budżet na obu faktach.

## 1. Załaduj budżet

1. **Home → Transform data**.
2. **New Source → Blank Query**, otwórz **Advanced Editor** i wklej:

   ```m
   let
       Source = fnGetCsv("F_Budget.csv"),
       Typed = Table.TransformColumnTypes(
           Source,
           {
               {"Budget Month", type date},
               {"DateKey", Int64.Type},
               {"Category", type text},
               {"Region", type text},
               {"Budget Amount", type number}
           },
           "en-US"
       )
   in
       Typed
   ```

3. Zmień nazwę zapytania na **F_Budget** → **Close & Apply**.

## 2. Relacje

W **Model view** utwórz trzy relacje:

| Od | Do | Kardynalność | Kierunek filtrowania |
|---|---|---|---|
| F_Budget[DateKey] | D_Date[DateKey] | Many-to-one | Single |
| F_Budget[Category] | D_Product[Category] | **Many-to-many** | Single – *D_Product filtruje F_Budget* |
| F_Budget[Region] | D_Geography[Region] | **Many-to-many** | Single – *D_Geography filtruje F_Budget* |

`DateKey` w budżecie to zawsze pierwszy dzień miesiąca, więc zwykła relacja z tabelą dat działa.
Ukryj wszystkie kolumny F_Budget – użytkownicy pracują tylko na miarach.

## 3. Miary

Utwórz w tabeli **_measures**, w folderze (display folder) **Budget**:

```dax
Budget Amount =
SUM ( F_Budget[Budget Amount] )
```

```dax
Sales vs Budget =
[Sales Amount] - [Budget Amount]
```

```dax
Sales vs Budget % =
DIVIDE ( [Sales Amount] - [Budget Amount], [Budget Amount] )
```

Format: `#,##0` dla dwóch pierwszych, `0.0%` dla ostatniej.

## 4. Test

Macierz (Matrix): wiersze **D_Product[Category]**, kolumny **D_Date[Year]**, wartości **Sales Amount, Budget Amount, Sales vs Budget %**.

**Sprawdź wynik (2025):**

| Category | Sales Amount | Budget Amount | Sales vs Budget % |
|---|---:|---:|---:|
| Camping | 27 058 299 | 27 879 100 | -2,9% |
| Climbing | 9 639 993 | 9 545 700 | 1,0% |
| Cycling | 40 475 450 | 42 077 600 | -3,8% |
| Running | 16 968 942 | 17 342 200 | -2,2% |
| Water Sports | 25 864 948 | 26 260 000 | -1,5% |
| **Total** | **120 007 633** | **123 104 600** | **-2,5%** |

W 2026 widać dużą różnicę, bo sprzedaż kończy się w październiku, a budżet obejmuje cały rok.

## 5. Do dyskusji

1. Dodaj **D_Product[Product Name]** pod Category. Co dzieje się z Budget Amount – i dlaczego?
2. Zamień Year na **D_Date[Date]**. W które dni pojawia się budżet?
3. Przefiltruj **D_Customer[Segment]**. Czy budżet reaguje? Czy powinien?

## 6. Wyzwanie (opcjonalne)

Pokaż budżet tylko na poziomie granularności, na którym istnieje – puste poniżej kategorii i poniżej miesiąca:

```dax
Budget Amount =
IF (
    ISFILTERED ( D_Product[Subcategory] )
        || ISFILTERED ( D_Product[Product Name] )
        || ISFILTERED ( D_Product[Product Code] )
        || ISFILTERED ( D_Date[Date] ),
    BLANK (),
    SUM ( F_Budget[Budget Amount] )
)
```

Jakie inne kolumny dodałbyś do warunku? Jakie są wady i zalety tego podejścia?
