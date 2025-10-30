def requires_auth(func):
    def wrapper(user_authenticated):
        if not user_authenticated:
            print("Access denied! Please log in first")
            return
        print("Access granted.")
        return func(user_authenticated)
    return wrapper

@requires_auth
def view_dashboard(user_authenticated):
    print("Welcome to your dashboard")

view_dashboard(False)
view_dashboard(True)