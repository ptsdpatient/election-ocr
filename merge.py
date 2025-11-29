import pandas as pd


input_file = "./reports/duplicate/static_no_whitespace.csv"
output_file = "./reports/duplicate/merged.csv"

# Load CSV
df = pd.read_csv(input_file)

# Helper function to define grouping key
def get_key(row):
    if pd.notna(row["Name"]) and str(row["Name"]).strip() != "":
        return (row["Date"], row["Name"])
    else:
        return (row["Date"], row["Age"], row["Gender"])

# Apply key column
df["merge_key"] = df.apply(get_key, axis=1)

# Group by key and merge
def combine_rows(group):
    # Fill missing values with available ones across rows
    return group.ffill().bfill().iloc[0]

merged = df.groupby("merge_key", as_index=False).apply(combine_rows)

# Drop helper column
merged = merged.drop(columns=["merge_key"])

# Save output
merged.to_csv(output_file, index=False)
