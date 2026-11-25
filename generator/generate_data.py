"""
Vistula Outdoor Co. – dummy dataset for the "Modern Power BI Semantic Modeling" training.

Fictional company selling outdoor and sports equipment to business customers worldwide.
Deterministic: the same seed and scale always produce the same data.

Usage (local):   python generate_data.py --out ../data --scale 1
Usage (Fabric):  import the functions and call build_all(scale=20) – see the Fabric notebook.

scale = 1  → ~600k sales lines (participant CSV pack, GitHub-friendly)
scale = 20 → ~12M sales lines (trainer demo in Fabric Lakehouse / Warehouse)
"""
import argparse
import os
import numpy as np
import pandas as pd

SEED = 20261127
START = pd.Timestamp("2022-01-01")
END_SALES = pd.Timestamp("2026-10-31")
END_CAL = pd.Timestamp("2026-12-31")

# ----------------------------------------------------------------------------- geography
CITIES = [
    # City, Country, Region, weight
    ("Warsaw", "Poland", "EMEA", 6), ("Krakow", "Poland", "EMEA", 3), ("Gdansk", "Poland", "EMEA", 2),
    ("Wroclaw", "Poland", "EMEA", 2), ("Berlin", "Germany", "EMEA", 5), ("Munich", "Germany", "EMEA", 4),
    ("Hamburg", "Germany", "EMEA", 3), ("Paris", "France", "EMEA", 5), ("Lyon", "France", "EMEA", 2),
    ("London", "United Kingdom", "EMEA", 5), ("Manchester", "United Kingdom", "EMEA", 2),
    ("Madrid", "Spain", "EMEA", 3), ("Barcelona", "Spain", "EMEA", 3), ("Milan", "Italy", "EMEA", 3),
    ("Rome", "Italy", "EMEA", 2), ("Amsterdam", "Netherlands", "EMEA", 3), ("Stockholm", "Sweden", "EMEA", 2),
    ("Oslo", "Norway", "EMEA", 2), ("Prague", "Czech Republic", "EMEA", 2), ("Vienna", "Austria", "EMEA", 2),
    ("Zurich", "Switzerland", "EMEA", 2), ("Copenhagen", "Denmark", "EMEA", 2), ("Dubai", "United Arab Emirates", "EMEA", 2),
    ("New York", "United States", "Americas", 6), ("Chicago", "United States", "Americas", 4),
    ("Denver", "United States", "Americas", 3), ("Seattle", "United States", "Americas", 3),
    ("Los Angeles", "United States", "Americas", 4), ("Toronto", "Canada", "Americas", 3),
    ("Vancouver", "Canada", "Americas", 3), ("Mexico City", "Mexico", "Americas", 2),
    ("Sao Paulo", "Brazil", "Americas", 2), ("Santiago", "Chile", "Americas", 1),
    ("Tokyo", "Japan", "APAC", 4), ("Osaka", "Japan", "APAC", 2), ("Seoul", "South Korea", "APAC", 3),
    ("Singapore", "Singapore", "APAC", 3), ("Sydney", "Australia", "APAC", 3), ("Melbourne", "Australia", "APAC", 2),
    ("Auckland", "New Zealand", "APAC", 1), ("Mumbai", "India", "APAC", 2), ("Shanghai", "China", "APAC", 3),
]

# ----------------------------------------------------------------------------- products
CATEGORIES = {
    # Category: (subcategories, price range, cost ratio range, seasonality by month 1..12)
    "Camping": (["Tents", "Sleeping Bags", "Camp Kitchen", "Backpacks"], (40, 650),
                (0.48, 0.62), [0.6, 0.6, 0.8, 1.0, 1.3, 1.5, 1.6, 1.4, 1.0, 0.8, 0.7, 0.9]),
    "Climbing": (["Ropes", "Harnesses", "Helmets", "Climbing Shoes"], (35, 420),
                 (0.50, 0.65), [0.8, 0.8, 0.9, 1.1, 1.2, 1.2, 1.2, 1.2, 1.1, 1.0, 0.8, 0.9]),
    "Cycling": (["Road Bikes", "Mountain Bikes", "Bike Helmets", "Cycling Apparel"], (30, 3200),
                (0.55, 0.70), [0.5, 0.6, 0.9, 1.3, 1.5, 1.5, 1.4, 1.3, 1.0, 0.8, 0.6, 0.8]),
    "Running": (["Running Shoes", "Running Apparel", "Sports Watches", "Hydration"], (15, 520),
                (0.45, 0.60), [1.3, 1.1, 1.1, 1.1, 1.0, 0.9, 0.9, 0.9, 1.0, 1.0, 1.0, 1.1]),
    "Water Sports": (["Kayaks", "Paddle Boards", "Wetsuits", "Life Jackets"], (45, 1800),
                     (0.52, 0.66), [0.3, 0.3, 0.6, 0.9, 1.4, 1.9, 2.0, 1.8, 1.1, 0.6, 0.4, 0.4]),
}
BRANDS = ["Northpeak", "Riverstone", "Altura", "Kestrel", "Bluefin", "Granite Line"]
COLORS = ["Black", "Blue", "Red", "Green", "Grey", "Orange", "White", "Yellow"]
MODEL_WORDS = ["Trail", "Summit", "Ridge", "Horizon", "Glacier", "Canyon", "Breeze", "Falcon", "Nova",
               "Aspen", "Delta", "Vertex", "Pulse", "Drift", "Echo", "Orbit", "Tundra", "Sierra"]

# ----------------------------------------------------------------------------- customers
CUST_A = ["Alpine", "Blue", "Coastal", "Crest", "Evergreen", "Frontier", "Granite", "Harbor", "Highland",
          "Lakeside", "Maple", "Meridian", "Northern", "Oak", "Pacific", "Pinnacle", "Prairie", "Redwood",
          "River", "Silver", "Stone", "Summit", "Sunrise", "Timber", "Valley", "Vista", "Westwind", "Wild"]
CUST_B = ["Outdoor", "Sports", "Adventure", "Gear", "Trading", "Supply", "Outfitters", "Expeditions",
          "Retail", "Active", "Trek", "Pro Shop"]
CUST_C = ["Ltd", "GmbH", "S.A.", "Sp. z o.o.", "Inc.", "LLC", "Co.", "Group", "AB", "B.V."]
SEGMENTS = [("Small business", 0.50, 0.00), ("Mid-market", 0.32, 0.05), ("Enterprise", 0.18, 0.10)]

FIRST = ["Anna", "Piotr", "Katarzyna", "Tomasz", "Maria", "Jan", "Laura", "Lukas", "Sophie", "Marco",
         "Elena", "James", "Olivia", "Daniel", "Emma", "Carlos", "Lucia", "Kenji", "Yuki", "Min-jun",
         "Priya", "Liam", "Chloe", "Noah", "Isabel", "Ethan", "Mia", "Oscar", "Hannah", "Felix"]
LAST = ["Nowak", "Kowalski", "Wisniewska", "Schmidt", "Muller", "Dubois", "Martin", "Rossi", "Garcia",
        "Smith", "Johnson", "Brown", "Taylor", "Lee", "Tanaka", "Sato", "Kim", "Patel", "Andersson",
        "Jensen", "Novak", "Silva", "Lopez", "Walker", "Fischer", "Moreau", "Bianchi", "Clark"]

COMMENTS = ["Customer requested delivery before 12:00, ref {}",
            "Split shipment approved by account manager, ticket {}",
            "Call before delivery, gate code {}",
            "Invoice to head office, PO {}",
            "Promo bundle applied, campaign {}",
            "Deliver to loading dock {}, ask for warehouse lead",
            "Express shipping requested, order note {}"]


def _rng(offset=0):
    return np.random.default_rng(SEED + offset)


def build_geography():
    df = pd.DataFrame(CITIES, columns=["City", "Country", "Region", "Weight"])
    df.insert(0, "GeographyKey", np.arange(1, len(df) + 1))
    return df


def build_products(n=260):
    rng = _rng(1)
    rows, key = [], 1
    cats = list(CATEGORIES)
    per_cat = n // len(cats)
    used = set()
    for cat in cats:
        subs, (pmin, pmax), (cmin, cmax), _ = CATEGORIES[cat]
        for i in range(per_cat):
            sub = subs[i % len(subs)]
            brand = rng.choice(BRANDS)
            while True:
                name = f"{brand} {rng.choice(MODEL_WORDS)} {rng.integers(100, 999)} {sub.rstrip('s')}"
                if name not in used:
                    used.add(name)
                    break
            price = float(np.exp(rng.uniform(np.log(pmin), np.log(pmax))))
            price = round(price, 0) - 0.01
            cost = round(price * rng.uniform(cmin, cmax), 2)
            rows.append((key, f"P{key:05d}", name, sub, cat, brand, rng.choice(COLORS), cost, price))
            key += 1
    return pd.DataFrame(rows, columns=["ProductKey", "Product Code", "Product Name", "Subcategory",
                                       "Category", "Brand", "Color", "Unit Cost", "List Price"])


def build_employees(geo):
    """Parent-child sales organization: Head of Sales → Regional Directors → Sales Managers → Sales Reps."""
    rng = _rng(2)
    rows = []

    def person(key, mgr, title, region, salary):
        f, l = rng.choice(FIRST), rng.choice(LAST)
        email = f"{f.lower().replace('-', '')}.{l.lower()}{key}@vistula-outdoor.example"
        rows.append((key, mgr, f"{f} {l}", title, region, email, int(salary)))

    key = 1
    person(key, None, "Head of Sales", "Global", 26000); head = key; key += 1
    reps_by_region = {}
    for region, n_mgr in [("EMEA", 3), ("Americas", 2), ("APAC", 2)]:
        person(key, head, "Regional Sales Director", region, rng.integers(17000, 21000)); director = key; key += 1
        reps_by_region[region] = []
        for _ in range(n_mgr):
            person(key, director, "Sales Manager", region, rng.integers(12000, 15000)); mgr = key; key += 1
            for _ in range(rng.integers(4, 7)):
                person(key, mgr, "Sales Representative", region, rng.integers(7000, 10500))
                reps_by_region[region].append(key); key += 1
    df = pd.DataFrame(rows, columns=["EmployeeKey", "ManagerKey", "Employee Name", "Title", "Region",
                                     "Email", "Monthly Salary"])
    df["ManagerKey"] = df["ManagerKey"].astype("Int64")
    return df, reps_by_region


def build_customers(geo, reps_by_region, n=4000):
    rng = _rng(3)
    seg_names = [s[0] for s in SEGMENTS]
    seg_p = [s[1] for s in SEGMENTS]
    geo_p = geo["Weight"] / geo["Weight"].sum()
    gkeys = rng.choice(geo["GeographyKey"].values, size=n, p=geo_p.values)
    names, used = [], set()
    while len(names) < n:
        nm = f"{rng.choice(CUST_A)} {rng.choice(CUST_B)} {rng.choice(CUST_C)}"
        if nm in used:
            nm = f"{nm} {rng.integers(2, 99)}"
        if nm not in used:
            used.add(nm); names.append(nm)
    region_of = geo.set_index("GeographyKey")["Region"]
    reps = [rng.choice(reps_by_region[region_of[g]]) for g in gkeys]
    df = pd.DataFrame({
        "CustomerKey": np.arange(1, n + 1),
        "Customer Code": [f"C{k:06d}" for k in range(1, n + 1)],
        "Customer Name": names,
        "Segment": rng.choice(seg_names, size=n, p=seg_p),
        "GeographyKey": gkeys,
        "EmployeeKey": reps,
        "First Order Date": None,
    })
    # customer "size" drives order frequency and order size
    df["_size"] = df["Segment"].map({"Small business": 1.0, "Mid-market": 2.6, "Enterprise": 6.0}) * rng.lognormal(0, 0.5, n)
    return df


def build_date():
    d = pd.date_range(START, END_CAL, freq="D")
    iso = d.isocalendar()
    fy_end_year = np.where(d.month >= 7, d.year + 1, d.year)
    fmonth = ((d.month - 7) % 12) + 1
    df = pd.DataFrame({
        "DateKey": d.strftime("%Y%m%d").astype(int),
        "Date": d.date,
        "Year": d.year,
        "Quarter": "Q" + d.quarter.astype(str),
        "Year Quarter": d.year.astype(str) + " Q" + d.quarter.astype(str),
        "Month Number": d.month,
        "Month": d.strftime("%B"),
        "Month Short": d.strftime("%b"),
        "Year Month": d.strftime("%Y-%m"),
        "Year Month Number": d.year * 100 + d.month,
        "Day of Month": d.day,
        "Day of Week Number": d.dayofweek + 1,
        "Day of Week": d.strftime("%A"),
        "Is Weekend": d.dayofweek >= 5,
        "ISO Year": iso["year"].values,
        "ISO Week": iso["week"].values,
        "Week Start Date": (d - pd.to_timedelta(d.dayofweek, unit="D")).date,
        "Fiscal Year": ["FY" + str(y) for y in fy_end_year],
        "Fiscal Quarter": ["FQ" + str((m - 1) // 3 + 1) for m in fmonth],
        "Fiscal Month Number": fmonth,
    })
    return df


def build_sales(geo, products, customers, scale=1.0):
    """Order lines with seasonality, growth, weekday pattern and deliberate 'heavy' columns."""
    rng = _rng(10)
    days = pd.date_range(START, END_SALES, freq="D")
    base_orders_per_day = 100 * scale
    years_from_start = (days - START).days / 365.25
    growth = 1.09 ** years_from_start
    weekday = np.array([1.15, 1.1, 1.05, 1.05, 1.0, 0.45, 0.3])[days.dayofweek]
    season = np.array([0.85, 0.85, 0.95, 1.0, 1.1, 1.15, 1.1, 1.05, 1.0, 0.95, 0.95, 1.05])[days.month - 1]
    n_orders_day = rng.poisson(base_orders_per_day * growth * weekday * season)
    n_orders = int(n_orders_day.sum())
    order_day = np.repeat(np.arange(len(days)), n_orders_day)

    cust_p = customers["_size"].values / customers["_size"].sum()
    cust_idx = rng.choice(len(customers), size=n_orders, p=cust_p)
    lines_per_order = 1 + rng.binomial(5, 0.35, n_orders)
    n_lines = int(lines_per_order.sum())
    line_order = np.repeat(np.arange(n_orders), lines_per_order)
    line_no = np.concatenate([np.arange(1, k + 1) for k in lines_per_order])

    # order-level attributes
    o_dates = days[order_day]
    secs = rng.integers(7 * 3600, 19 * 3600, n_orders)
    o_dt = o_dates + pd.to_timedelta(secs, unit="s")
    year_seq = pd.Series(o_dates.year).groupby(o_dates.year).cumcount().values + 1
    order_no = np.char.add(np.char.add("SO-", o_dates.year.astype(str).values.astype("U4")),
                           np.char.add("-", np.char.zfill(year_seq.astype(str), 6)))
    c = customers.iloc[cust_idx]
    region = geo.set_index("GeographyKey").loc[c["GeographyKey"].values, "Region"].values
    ship_lag = rng.integers(1, 6, n_orders)
    deliv_lag = ship_lag + np.where(region == "EMEA", rng.integers(1, 5, n_orders),
                                    np.where(region == "Americas", rng.integers(2, 8, n_orders), rng.integers(3, 11, n_orders)))

    # line-level product choice with category seasonality
    cats = list(CATEGORIES)
    prod_cat = products["Category"].values
    month_of_line = o_dates.month.values[line_order]
    season_mat = np.array([CATEGORIES[cg][3] for cg in cats])  # cats x 12
    cat_w = season_mat[:, month_of_line - 1].T * np.array([1.0, 0.6, 0.9, 1.2, 0.5])
    cat_w = cat_w / cat_w.sum(axis=1, keepdims=True)
    u = rng.random(n_lines)[:, None]
    cat_choice = (u > np.cumsum(cat_w, axis=1)).sum(axis=1)
    prod_choice = np.empty(n_lines, dtype=int)
    for ci, cg in enumerate(cats):
        mask = cat_choice == ci
        pidx = np.where(prod_cat == cg)[0]
        pw = 1 / np.sqrt(products["List Price"].values[pidx])
        prod_choice[mask] = rng.choice(pidx, size=mask.sum(), p=pw / pw.sum())
    p = products.iloc[prod_choice]

    seg = c["Segment"].values[line_order]
    disc_base = pd.Series(seg).map({s[0]: s[2] for s in SEGMENTS}).values
    disc = np.clip(disc_base + rng.choice([0, 0, 0, 0.05, 0.1], n_lines), 0, 0.3)
    qty = 1 + rng.poisson(np.clip(c["_size"].values[line_order], 1, 12))
    unit_price = np.round(p["List Price"].values * rng.uniform(0.97, 1.03, n_lines), 4)
    net = qty * unit_price * (1 - disc)                       # deliberately NOT rounded (VertiPaq lab)
    cost = np.round(qty * p["Unit Cost"].values, 2)

    # deliberately heavy columns
    hexs = rng.integers(0, 16, size=(n_lines, 32)).astype(np.uint8)
    hexchars = np.array(list("0123456789abcdef"))[hexs]
    guid = ["".join(r[:8]) + "-" + "".join(r[8:12]) + "-4" + "".join(r[13:16]) + "-a" + "".join(r[17:20]) + "-" + "".join(r[20:32])
            for r in hexchars]
    has_comment = rng.random(n_lines) < 0.15
    tmpl = rng.integers(0, len(COMMENTS), n_lines)
    refs = rng.integers(10000, 999999, n_lines)
    comment = np.where(has_comment, [COMMENTS[t].format(r) for t, r in zip(tmpl, refs)], "")
    o_dt_line = o_dt[line_order]
    last_upd = o_dt_line + pd.to_timedelta(rng.integers(0, 30 * 86400, n_lines), unit="s")

    df = pd.DataFrame({
        "Sales Order Number": order_no[line_order],
        "Sales Order Line": line_no,
        "OrderDateKey": o_dates.strftime("%Y%m%d").astype(int).values[line_order],
        "ShipDateKey": (o_dates + pd.to_timedelta(ship_lag, unit="D")).strftime("%Y%m%d").astype(int).values[line_order],
        "DeliveryDateKey": (o_dates + pd.to_timedelta(deliv_lag, unit="D")).strftime("%Y%m%d").astype(int).values[line_order],
        "CustomerKey": c["CustomerKey"].values[line_order],
        "ProductKey": p["ProductKey"].values,
        "GeographyKey": c["GeographyKey"].values[line_order],
        "EmployeeKey": c["EmployeeKey"].values[line_order],
        "Quantity": qty,
        "Unit Price": unit_price,
        "Discount Pct": np.round(disc, 2),
        "Net Amount": net,
        "Cost Amount": cost,
        "Order Date Time": o_dt_line.strftime("%Y-%m-%d %H:%M:%S"),
        "Order Line GUID": guid,
        "Comment": comment,
        "Last Updated": last_upd.strftime("%Y-%m-%d %H:%M:%S"),
    })
    return df


def build_budget(sales, products, geo):
    """Budget at month × category × region grain (deliberately coarser than sales)."""
    rng = _rng(20)
    s = sales[["OrderDateKey", "ProductKey", "GeographyKey", "Net Amount"]].copy()
    s["Month"] = pd.to_datetime(s["OrderDateKey"].astype(str), format="%Y%m%d").dt.to_period("M")
    s["Category"] = products.set_index("ProductKey").loc[s["ProductKey"], "Category"].values
    s["Region"] = geo.set_index("GeographyKey").loc[s["GeographyKey"], "Region"].values
    act = s.groupby(["Month", "Category", "Region"])["Net Amount"].sum()
    rows = []
    for m in pd.period_range("2022-01", "2026-12", freq="M"):
        for cat in CATEGORIES:
            for reg in ["EMEA", "Americas", "APAC"]:
                prev = act.get((m - 12, cat, reg))
                cur = act.get((m, cat, reg))
                if prev is not None:
                    base = prev * 1.08
                elif cur is not None:
                    base = cur
                else:
                    base = act.get((m - 24, cat, reg), 0) * 1.17
                amount = round(base * rng.uniform(0.92, 1.12), -2)
                first = m.to_timestamp()
                rows.append((first.date(), int(first.strftime("%Y%m%d")), cat, reg, amount))
    return pd.DataFrame(rows, columns=["Budget Month", "DateKey", "Category", "Region", "Budget Amount"])


def build_flat(sales, products, customers, geo, emp, year=2025):
    """Denormalized extract for the 'flat → star schema' demo (one year)."""
    s = sales[sales["OrderDateKey"] // 10000 == year]
    f = (s.merge(products.drop(columns=["Unit Cost"]), on="ProductKey")
          .merge(customers[["CustomerKey", "Customer Code", "Customer Name", "Segment"]], on="CustomerKey")
          .merge(geo.drop(columns=["Weight"]), on="GeographyKey")
          .merge(emp[["EmployeeKey", "Employee Name"]], on="EmployeeKey"))
    f["Order Date"] = pd.to_datetime(f["OrderDateKey"].astype(str), format="%Y%m%d").dt.date
    f["Ship Date"] = pd.to_datetime(f["ShipDateKey"].astype(str), format="%Y%m%d").dt.date
    f["Delivery Date"] = pd.to_datetime(f["DeliveryDateKey"].astype(str), format="%Y%m%d").dt.date
    cols = ["Sales Order Number", "Sales Order Line", "Order Date", "Ship Date", "Delivery Date",
            "Customer Code", "Customer Name", "Segment", "City", "Country", "Region",
            "Product Code", "Product Name", "Subcategory", "Category", "Brand", "Color",
            "Employee Name", "Quantity", "Unit Price", "Discount Pct", "Net Amount", "Cost Amount"]
    return f.sort_values(["Sales Order Number", "Sales Order Line"])[cols]


def build_all(scale=1.0):
    geo = build_geography()
    products = build_products()
    emp, reps = build_employees(geo)
    customers = build_customers(geo, reps)
    dates = build_date()
    sales = build_sales(geo, products, customers, scale)
    budget = build_budget(sales, products, geo)
    first_order = sales.groupby("CustomerKey")["OrderDateKey"].min()
    customers["First Order Date"] = pd.to_datetime(
        customers["CustomerKey"].map(first_order).astype("Int64").astype(str), format="%Y%m%d", errors="coerce").dt.date
    customers = customers.drop(columns=["_size", "GeographyKey", "EmployeeKey"])
    return {
        "D_Date": dates,
        "D_Geography": geo.drop(columns=["Weight"]),
        "D_Product": products,
        "D_Customer": customers,
        "D_Employee": emp,
        "F_Sales": sales,
        "F_Budget": budget,
    }, (sales, products, customers, geo, emp)


def write_csv_pack(out_dir, scale=1.0):
    os.makedirs(out_dir, exist_ok=True)
    tables, (sales, products, customers, geo, emp) = build_all(scale)
    for name, df in tables.items():
        if name == "F_Sales":
            years = df["OrderDateKey"] // 10000
            for y in sorted(years.unique()):
                df[years == y].to_csv(os.path.join(out_dir, f"F_Sales_{y}.csv"), index=False, encoding="utf-8")
        else:
            df.to_csv(os.path.join(out_dir, f"{name}.csv"), index=False, encoding="utf-8")
    flat = build_flat(sales, products, customers, geo, emp)
    flat.to_csv(os.path.join(out_dir, "Sales_Flat_2025.csv"), index=False, encoding="utf-8")
    return tables


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="../data")
    ap.add_argument("--scale", type=float, default=1.0)
    a = ap.parse_args()
    t = write_csv_pack(a.out, a.scale)
    for k, v in t.items():
        print(f"{k:12s} {len(v):>10,} rows")
