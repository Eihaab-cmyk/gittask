employees = [
    {"name": "Ali", "salary": 60000, "dept": "IT"},
    {"name": "Emily", "salary": 90000, "dept": "IT"},
    {"name": "Sara", "salary": 75000, "dept": "HR"},
    {"name": "John", "salary": 50000, "dept": "Finance"},
    {"name": "David", "salary": 45000, "dept": "Finance"}
]

high_earners = list(filter(lambda emp: emp["salary"] > 60000, employees))

sorted_emps = sorted(high_earners, key=lambda emp: emp["salary"])

result = list(map(lambda emp: (emp["name"], emp["salary"]), sorted_emps))
print(result)