from stats import word_count, count_char, sort_on

word_count()
counts = count_char()
items = [{"char": c, "num": n} for c, n in counts.items()]
items.sort(reverse=True, key=sort_on)
for i in items:
    print(f"{i['char']}: {i['num']}")