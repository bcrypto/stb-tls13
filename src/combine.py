import os
import re

# Folder containing the split .md files
input_folder = "."
output_file = "../draft-stb-tls13.md"

# Non-section markdown that must never be merged into the draft
IGNORE_FILES = {
    "RFC_REVIEW_REPORT.md",
    "99RFC_STYLE_GUIDE.md",
    "99RFC_STYLE_GUIDE_CHANGES.md",
}

# Collect all .md files
files = [f for f in os.listdir(input_folder) if f.endswith(".md")]

# Use only files that start with digits; skip review/report extras
numbered_files = []

for f in files:
    if f in IGNORE_FILES:
        continue
    if re.match(r"^\d+", f):
        numbered_files.append(f)

# Sort numbered files by their full leading number (00, 01, ..., 91, ...)
def sort_key(fname):
    match = re.match(r"^(\d+)", fname)
    return int(match.group(1)) if match else 999999

numbered_files.sort(key=sort_key)

print("Merging in order:")
for f in numbered_files:
    print("  ", f)

with open(output_file, "w", encoding="utf-8") as fout:
    for fname in numbered_files:
        path = os.path.join(input_folder, fname)
        with open(path, "r", encoding="utf-8") as fin:
            content = fin.read().strip()
        fout.write(content + "\n\n")

print(f"Done! Merged into {output_file}")
