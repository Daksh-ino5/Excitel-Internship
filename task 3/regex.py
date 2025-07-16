import os

# Get the path of the current script
current_dir = os.path.dirname(__file__)

# Build the full path to regex.txt
file_path = os.path.join(current_dir, "regex.txt")

# Read all lines from the file
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Keep alternate lines (even indices: 0, 2, 4, ...)
filtered_lines = [line for i, line in enumerate(lines) if i % 2 == 0]

# Write the cleaned lines to a new file (or overwrite same file)
output_path = os.path.join(current_dir, "rules.txt")
with open(output_path, "w", encoding="utf-8") as file:
    file.writelines(filtered_lines)

print("✅ Alternate lines removed and saved to regex_cleaned.txt")
