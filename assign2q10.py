# Find lines containing a keyword in a text file

def find_lines_containing(filename, keyword):
    results = []
    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if keyword.lower() in line.lower():
                results.append((i, line.strip()))
    return results

# Test the function
matches = find_lines_containing("sample-file.txt", "lorem")

if not matches:
    print("No matching lines were found.")
else:
    print(f"Number of matching lines: {len(matches)}")
    print("First 3 matching lines:")
    for line_number, line_text in matches[:3]:
        print(f"{line_number}: {line_text}")