data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mean = sum(data) / len(data)

mad = sum([abs(x - mean) for x in data]) / len(data)

variance = sum([((x - mean) ** 2) for x in data]) / len(data)

std = variance ** 0.5

print(f"mean: {mean}")
print(f"mad: {mad}")
print(f"variance: {variance}")
print(f"std: {std}")

