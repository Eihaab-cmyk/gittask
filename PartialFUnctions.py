from functools import partial

def apply_discount(price, discount):
    return price - (price * discount / 100)

student_discount = partial(apply_discount, discount=15)
member_discount = partial(apply_discount, discount=10)
vip_discount = partial(apply_discount, discount=25)

price = float(input("Enter the original price: "))
print("\nSelect Discount Type:")
print("1. Student (15%)")
print("2. Member (10%)")
print("3. VIP (25%)")
choice = input("Enter choice (1/2/3): ")

if choice == '1':
    final_price = student_discount(price)
elif choice == "2":
    final_price = member_discount(price)
elif choice == "3":
    final_price = vip_discount(price)
else:
    final_price = price
    print("No discount applied!")

print(f"\n💰 Final Price after discount: {final_price}")