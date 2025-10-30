import json
import os

FILE_NAME = "profiles.json"

def load_profiles():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []
def save_profiles(profiles):
    with open(FILE_NAME, "w") as f:
        json.dump(profiles, f, indent=4)
def main():
    profiles = load_profiles()

    print("=== Add New Profile ===")
    name = input("Enter you name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")

    new_profile = {"name": name, "age": age, "city": city}
    profiles.append(new_profile)

    save_profiles(profiles)
    print("✅ Profile saved successfully!")

    print("\n=== All Saved Profiles ===")
    print(profiles)
if __name__ == "__main__":
    main()