# Find near-duplicate lines in a text file

import string

def normalize(line):
    # Normalize a line
    return ''.join(ch for ch in line.lower() if ch not in string.whitespace and ch not in string.punctuation)

def find_near_duplicates(filename):
    groups = {}

    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            original_line = line.rstrip('\n').rstrip()  # remove trailing spaces
            key = normalize(original_line)

            if key == "":
                continue  # skip empty lines

            groups.setdefault(key, []).append((line_number, original_line))

    duplicate_sets = [v for v in groups.values() if len(v) > 1]

    print(f"Number of near-duplicate sets: {len(duplicate_sets)}\n")

    for i, dup_set in enumerate(duplicate_sets[:2], start=1):
        print(f"Set {i}:")
        for line_number, text in dup_set:
            print(f"{line_number}: {text}")
        print()

find_near_duplicates("sample-file.txt")