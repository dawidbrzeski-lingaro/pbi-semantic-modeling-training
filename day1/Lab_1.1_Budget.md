# Lab 1.1 – Second fact table: actual vs. budget

**Module 3A · ~20 min · starts from `Day1_start.pbix`**

The budget is planned at a coarser grain than sales: **month × product category × region**.
You add it as a separate fact table and build actual-vs-budget measures on top of both facts.

## 1. Load the budget

1. **Home → Transform data**.
2. **New Source → Blank Query**, open **Advanced Editor** and paste:

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

3. Rename the query to **F_Budget** → **Close & Apply**.

## 2. Relationships

In **Model view** create three relationships:

| From | To | Cardinality | Cross-filter direction |
|---|---|---|---|
| F_Budget[DateKey] | D_Date[DateKey] | Many-to-one | Single |
| F_Budget[Category] | D_Product[Category] | **Many-to-many** | Single – *D_Product filters F_Budget* |
| F_Budget[Region] | D_Geography[Region] | **Many-to-many** | Single – *D_Geography filters F_Budget* |

`DateKey` in the budget is always the first day of the month, so the regular relationship to the date table works.
Hide all F_Budget columns – users work with measures only.

## 3. Measures

Create in the **_measures** table, display folder **Budget**:

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

Format: `#,##0` for the first two, `0.0%` for the last one.

## 4. Test

Matrix: rows **D_Product[Category]**, columns **D_Date[Year]**, values **Sales Amount, Budget Amount, Sales vs Budget %**.

**Check your result (2025):**

| Category | Sales Amount | Budget Amount | Sales vs Budget % |
|---|---:|---:|---:|
| Camping | 27,058,299 | 27,879,100 | -2.9% |
| Climbing | 9,639,993 | 9,545,700 | 1.0% |
| Cycling | 40,475,450 | 42,077,600 | -3.8% |
| Running | 16,968,942 | 17,342,200 | -2.2% |
| Water Sports | 25,864,948 | 26,260,000 | -1.5% |
| **Total** | **120,007,633** | **123,104,600** | **-2.5%** |

2026 shows a large gap because sales end in October while the budget covers the full year.

## 5. Discuss

1. Add **D_Product[Product Name]** below Category. What happens to Budget Amount – and why?
2. Replace Year with **D_Date[Date]**. On which days does the budget appear?
3. Filter **D_Customer[Segment]**. Does the budget react? Should it?

## 6. Challenge (optional)

Show the budget only at the grain where it exists – blank below category and below month:

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

What other columns would you add to the condition? What are the trade-offs of this approach?
