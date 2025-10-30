import inspect

def function_info(func):
    print(f"🔍 Function Name: {func.__name__}")
    print(f"📘 Docstring: {inspect.getdoc(func) or 'No docstring'}")
    print(f"📍 Arguments: {inspect.signature(func)}")
    print(f"📄 Source Code:\n{inspect.getsource(func)}")

def greet(name, age):
    return f"Hello {name}, you are {age} years old"
def add(a,b):
    return a+b

print("Available functions: greet, add")
choice = input("Which function do you want to inspect? ").strip()

if choice == "greet":
    function_info(greet)
elif choice == "add":
    function_info(add)
else:
    print("❌ Function not found!")