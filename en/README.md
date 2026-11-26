# Modern Power BI Semantic Modeling – training materials

Dummy data, starter models and hands-on labs for the 3-day training.
All data is fictional: **Vistula Outdoor Co.**, a company selling outdoor and sports equipment
to business customers in EMEA, the Americas and APAC.

## Before Day 1 – install

| Tool | Needed for | Link |
|---|---|---|
| Power BI Desktop (latest) | all days | https://aka.ms/pbidesktopstore |
| DAX Studio | Day 1 (Lab 1.3), Day 2 | https://daxstudio.org |
| Tabular Editor 2 (free) | Day 2 | https://github.com/TabularEditor/TabularEditor/releases |
| VS Code + TMDL extension, Git | Day 3 | https://code.visualstudio.com · https://git-scm.com |

## What is in this repository

```
data/                CSV files (UTF-8, comma-separated, en-US number format)
  D_Date.csv           calendar 2022–2026 incl. fiscal year (starts 1 July) and ISO weeks
  D_Product.csv        260 products: Category › Subcategory › Product
  D_Customer.csv       4,000 business customers with segment
  D_Geography.csv      42 cities: Region › Country › City
  D_Employee.csv       sales organization (parent-child), used on Day 2
  F_Sales_2022.csv …   sales order lines, one file per year (Jan 2022 – Oct 2026, ~527k lines)
  F_Budget.csv         budget at month × category × region grain
  Sales_Flat_2025.csv  one denormalized extract (used in the trainer demo)
day1/
  Day1_start.pbix      starter model for all Day 1 labs
  Lab_1.1_Budget.md
  Lab_1.2_Calculation_Group.md
  Lab_1.3_VertiPaq.md
generator/
  generate_data.py     how the data was generated (deterministic)
```

## Using the starter file

`Day1_start.pbix` already contains the data – open it and start the lab.

If you refresh, data is loaded from this repository through the Power Query parameter **DataSource**.
If GitHub is blocked in your network:

1. Download this repository as ZIP (green **Code** button → *Download ZIP*) and unpack it, e.g. to `C:\PBI-Training\`.
2. In Power BI Desktop: **Transform data → Edit parameters → DataSource** = `C:\PBI-Training\data\`
   (keep the trailing backslash).
3. Refresh.

Every lab starts from the day's starter file. Labs don't depend on each other – if you skip one,
you can still do the next.
