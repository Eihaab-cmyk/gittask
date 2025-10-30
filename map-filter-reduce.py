from functools import reduce

students = [
    {"name": "Ali", "scores": [85, 90, 78]},
    {"name": "Sara", "scores": [92, 88, 95]},
    {"name": "Bilal", "scores": [40, 35, 50]},
    {"name": "Ayesha", "scores": [75, 80, 72]}
]

averages = list(map(lambda s: {"name": s["name"], "avg": sum(s["scores"]) / len(s["scores"])}, students))
print("Average Scores:", averages)

passed_students = list(filter(lambda s: s["avg"] >= 60, averages))
print("\n Passed Students:", passed_students)

class_average = reduce(lambda acc, s: acc + s["avg"], passed_students, 0) / len(passed_students)
print(f"\nClass Average (of passed students): {class_average:.2f}")