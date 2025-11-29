import csv

input_file = "./reports/duplicate/output.csv"
output_file = "./reports/duplicate/static_no_whitespace.csv"

# with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
#     prev_line = None
#     for line in f_in:
#         if line != prev_line:   # only write if not same as previous
#             f_out.write(line)
#         prev_line = line



cleaned_rows = []
with open(input_file, newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 4:
            continue  # skip broken rows

        # all fields after gender
        after_gender = row[4:]

        # keep only if something exists after gender
        if any(cell.strip() for cell in after_gender):
            cleaned_rows.append(row)

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(cleaned_rows)