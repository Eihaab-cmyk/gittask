def smart_calculator(*args, operation="+", **kwargs):
    if not args:
        return "No numbers provided"
    result = None
    if operation == "+":
        result = sum(args)
    elif operation == "-":
        result = args[0]
        for num in args[1:]:
            result = result-num
    elif operation == "*":
        result = 1
        for num in args:
            result *= num
    elif operation == "/":
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Error: Division by zero"
            result /= num
    else:
        return f"Unknown operation: {operation}"
    
    if "round_to" in kwargs:
        result = round(result, kwargs["round_to"])

    if kwargs.get("verbose", False):
        print(f"Operation: {operation}")
        print(f"Numbers: {args}")
        print(f"Result: {result}")
    
    return result

def main():
    print("🧮 Welcome to Smart Calculator!")
    print("Supported operations: +, -, *, /")
    print("Type 'exit' to quit.\n")

    while True:
        numbers_input = input("Enter numbers separated by spaces: ")
        if numbers_input.lower() == "exit":
            print("Goodbye 👋")
            break

        try:
            numbers = [float(n) for n in numbers_input.split()]
        except ValueError:
            print("❌ Please enter valid numbers.")
            continue

        operation = input("Enter operation ((+)/(-)/(*)/(/)): ").lower()
        round_to = input("Round result to how many decimals? (Press Enter to skip): ")
        verbose_input = input("Show detailed output? (y/n): ").lower()

        kwargs = {}
        if round_to.isdigit():
            kwargs["round_to"] = int(round_to)
        if verbose_input == "y":
            kwargs["verbose"] = True

        result = smart_calculator(*numbers, operation=operation, **kwargs)
        print(f"✅ Result: {result}\n")


if __name__ == "__main__":
    main()