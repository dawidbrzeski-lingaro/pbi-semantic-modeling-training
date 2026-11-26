# Lab 1.2 – Calculation group: time intelligence bez mnożenia miar

**Moduł 3B · ok. 20 min · start z `Day1_start.pbix`**

Zamiast pisać `Sales Amount YTD`, `Margin YTD`, `Sales Amount PY` … dla każdej miary,
tworzysz jedną calculation group, która działa dla wszystkich miar.

## 1. Utwórz calculation group

1. **Model view → Home → Calculation group** (potwierdź komunikat o miarach niejawnych – implicit measures).
2. Zmień nazwę tabeli na **Time Intelligence**, a jej kolumny na **Period**.
3. Zmień nazwę pierwszego elementu na **Current**: `SELECTEDMEASURE ()`.
4. Dodaj pozostałe elementy (**New calculation item**) w tej kolejności:

```dax
YTD =
CALCULATE ( SELECTEDMEASURE (), DATESYTD ( D_Date[Date] ) )
```

```dax
PY =
CALCULATE ( SELECTEDMEASURE (), SAMEPERIODLASTYEAR ( D_Date[Date] ) )
```

```dax
YoY =
VAR _Current = SELECTEDMEASURE ()
VAR _PY =
    CALCULATE ( SELECTEDMEASURE (), SAMEPERIODLASTYEAR ( D_Date[Date] ) )
RETURN
    _Current - _PY
```

```dax
YoY % =
VAR _Current = SELECTEDMEASURE ()
VAR _PY =
    CALCULATE ( SELECTEDMEASURE (), SAMEPERIODLASTYEAR ( D_Date[Date] ) )
RETURN
    DIVIDE ( _Current - _PY, _PY )
```

5. Zaznacz element **YoY %** → włącz **Dynamic format string** → `"0.0%"`.

`D_Date` jest oznaczona jako tabela dat, więc funkcje time intelligence działają na `D_Date[Date]`.

## 2. Test

Macierz (Matrix): wiersze **D_Date[Year]**, kolumny **Time Intelligence[Period]**, wartości **Sales Amount**.
Potem zamień wartość na **Margin** i **Order Count** – te same pięć elementów działa dla każdej miary.

**Sprawdź wynik (Sales Amount):**

| Year | Current | PY | YoY % |
|---|---:|---:|---:|
| 2024 | 112 037 249 | 101 433 774 | 10,5% |
| 2025 | 120 007 633 | 112 037 249 | 7,1% |

YTD dla **marca 2025** (wiersze: hierarchia Calendar do poziomu Year Month) = **21 848 846**.

## 3. Do dyskusji

1. Dlaczego Power BI wyłączył miary niejawne, gdy utworzyłeś grupę?
2. Wstaw do macierzy **Margin %**. Czy **YoY** ma sens dla wskaźnika procentowego? Jak byś to rozwiązał?
3. Co się stanie, jeśli raport używa też drugiej calculation group (np. przeliczania walut)? Sprawdź, czym jest **precedence**.

## 4. Wyzwanie (opcjonalne)

Rok fiskalny zaczyna się 1 lipca. Dodaj element **Fiscal YTD**:

```dax
Fiscal YTD =
CALCULATE ( SELECTEDMEASURE (), DATESYTD ( D_Date[Date], "06-30" ) )
```

Przetestuj z wierszami **D_Date[Fiscal Year]**. Kontrola: Sales Amount dla **FY2026** (lip 2025 – cze 2026) = **125 558 962**.
