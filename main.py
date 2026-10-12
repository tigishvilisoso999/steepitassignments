first_name = input("შეიყვანეთ სახელი: ").strip().lower()
last_name = input("შეიყვანეთ გვარი: ").strip().lower()

print("აირჩიეთ ელფოსტის დომენი:")
print("1. gmail.com")
print("2. itstep.ge")
print("3. yahoo.com")

choice = input("შეიყვანეთ არჩევანი (1, 2 ან 3): ")

domains = {
    "1": "gmail.com",
    "2": "itstep.ge",
    "3": "yahoo.com"
}

if choice in domains:
    username = first_name[0] + last_name
    email = f"{username}@{domains[choice]}"
    print(f"თქვენი ელფოსტაა: {email}")
else:
    print("არასწორი არჩევანი!")