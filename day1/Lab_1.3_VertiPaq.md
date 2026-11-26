# Lab 1.3 – Optymalizacja modelu -  VertiPaq Analyzer

**Moduł 4 · ok. 20 min · start z `Day1_start.pbix` · wymaga DAX Studio**

## 1. Zmierz punkt wyjścia

1. **External Tools → DAX Studio** (albo uruchom DAX Studio i połącz się z otwartym PBIX).
2. **Advanced → View Metrics**.
3. Na zakładce **Tables** zapisz łączny rozmiar modelu i rozmiar **F_Sales**.
4. Na zakładce **Columns** posortuj po **Total Size**. Zapisz 5 największych kolumn z ich
   **Cardinality**, **Total Size** i **% DB**.

| Kolumna | Cardinality | Total size | % DB |
|---|---:|---:|---:|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

## 2. Analiza

Dla każdej z 5 największych kolumn odpowiedz:

- Czy jest używana w jakiejś mierze, relacji lub raporcie?
- Dlaczego ma tak wysoką kardynalność?
- Czy można ją usunąć, rozdzielić albo zmniejszyć jej precyzję?

## 3. Optymalizacja w Power Query

Otwórz **Transform data → F_Sales** i dodaj na końcu te kroki:

1. **Usuń** `Order Line GUID` i `Comment` – nigdzie nieużywane.
2. **Rozdziel znacznik czasu** – zostaw tylko godzinę zamówienia; data jest już w `OrderDateKey`:
   dodaj kolumnę niestandardową (custom column) **Order Hour** = `Time.Hour([Order Date Time])` (liczba całkowita),
   potem usuń `Order Date Time` i `Last Updated`.
3. **Zmniejsz precyzję** `Net Amount`: zaokrąglij do 2 miejsc po przecinku i zmień typ na **Fixed decimal number**:

   ```m
   Rounded = Table.TransformColumns(
       PreviousStep,
       {{"Net Amount", each Number.Round(_, 2), Currency.Type}}
   )
   ```

   (zamień `PreviousStep` na nazwę swojego ostatniego kroku)

**Close & Apply**.

## 4. Zmierz ponownie

Uruchom ponownie **View Metrics** i porównaj:

| | Przed | Po |
|---|---:|---:|
| Rozmiar modelu | | |
| Rozmiar F_Sales | | |

Sprawdź, czy **Sales Amount** za 2025 nadal wynosi **120 007 633**.

## 5. Do dyskusji

1. Która pojedyncza zmiana dała największą oszczędność? Dlaczego?
2. `Sales Order Number` też ma wysoką kardynalność, ale korzysta z niej `Order Count`. Jakie są opcje?
3. Co sprawdziłbyś w VertiPaq Analyzer przed każdym wydaniem modelu?
