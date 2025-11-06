from stats import word_count, count_char, sort_on
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]
word_count(path)
counts = count_char(path)
items = [{"char": c, "num": n} for c, n in counts.items()]
items.sort(reverse=True, key=sort_on)
for i in items:
    print(f"{i['char']}: {i['num']}")