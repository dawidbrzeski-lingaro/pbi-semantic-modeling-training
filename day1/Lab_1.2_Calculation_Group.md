# Lab 1.2 – Calculation group: time intelligence without measure sprawl

**Module 3B · ~20 min · starts from `Day1_start.pbix`**

Instead of writing `Sales Amount YTD`, `Margin YTD`, `Sales Amount PY` … for every measure,
you create one calculation group that works for all measures.

## 1. Create the calculation group

1. **Model view → Home → Calculation group** (confirm the prompt about implicit measures).
2. Rename the table to **Time Intelligence** and its column to **Period**.
3. Rename the first item to **Current**: `SELECTEDMEASURE ()`.
4. Add the remaining items (**New calculation item**), in this order:

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

5. Select the **YoY %** item → turn on **Dynamic format string** → `"0.0%"`.

`D_Date` is marked as a date table, so the time-intelligence functions work on `D_Date[Date]`.

## 2. Test

Matrix: rows **D_Date[Year]**, columns **Time Intelligence[Period]**, values **Sales Amount**.
Then swap the value to **Margin** and **Order Count** – the same five items work for every measure.

**Check your result (Sales Amount):**

| Year | Current | PY | YoY % |
|---|---:|---:|---:|
| 2024 | 112,037,249 | 101,433,774 | 10.5% |
| 2025 | 120,007,633 | 112,037,249 | 7.1% |

YTD at **March 2025** (rows: Calendar hierarchy down to Year Month) = **21,848,846**.

## 3. Discuss

1. Why did Power BI turn off implicit measures when you created the group?
2. Put **Margin %** in the matrix. Is **YoY** meaningful for a ratio? How would you handle it?
3. What happens if a report also uses a second calculation group (e.g. currency conversion)? Look up **precedence**.

## 4. Challenge (optional)

The fiscal year starts on 1 July. Add a **Fiscal YTD** item:

```dax
Fiscal YTD =
CALCULATE ( SELECTEDMEASURE (), DATESYTD ( D_Date[Date], "06-30" ) )
```

Test it with rows **D_Date[Fiscal Year]**. Check: Sales Amount for **FY2026** (Jul 2025 – Jun 2026) = **125,558,962**.
