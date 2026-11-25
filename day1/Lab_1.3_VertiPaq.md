# Lab 1.3 – Where does the memory go? VertiPaq Analyzer

**Module 4 · ~20 min · starts from `Day1_start.pbix` · requires DAX Studio**

## 1. Measure the starting point

1. **External Tools → DAX Studio** (or start DAX Studio and connect to the open PBIX).
2. **Advanced → View Metrics**.
3. On the **Tables** tab note the total model size and the size of **F_Sales**.
4. On the **Columns** tab sort by **Total Size**. Write down the top 5 columns with their
   **Cardinality**, **Total Size** and **% DB**.

| Column | Cardinality | Total size | % DB |
|---|---:|---:|---:|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

## 2. Analyze

For each of the top 5 columns answer:

- Is it used in any measure, relationship or report?
- Why is its cardinality so high?
- Can it be removed, split or made less precise?

## 3. Optimize in Power Query

Open **Transform data → F_Sales** and add these steps at the end:

1. **Remove** `Order Line GUID` and `Comment` – not used anywhere.
2. **Split the timestamp** – keep only the hour of the order; the date is already in `OrderDateKey`:
   add a custom column **Order Hour** = `Time.Hour([Order Date Time])` (whole number),
   then remove `Order Date Time` and `Last Updated`.
3. **Reduce precision** of `Net Amount`: round to 2 decimals and change the type to **Fixed decimal number**:

   ```m
   Rounded = Table.TransformColumns(
       PreviousStep,
       {{"Net Amount", each Number.Round(_, 2), Currency.Type}}
   )
   ```

   (replace `PreviousStep` with the name of your last step)

**Close & Apply**.

## 4. Measure again

Re-run **View Metrics** and compare:

| | Before | After |
|---|---:|---:|
| Model size | | |
| F_Sales size | | |

Check that **Sales Amount** for 2025 is still **120,007,633**.

## 5. Discuss

1. Which single change saved the most? Why?
2. `Sales Order Number` also has high cardinality, but `Order Count` uses it. What are the options?
3. What would you check in VertiPaq Analyzer before every release of a model?
