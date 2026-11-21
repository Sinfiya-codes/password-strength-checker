password = input("Enter your password: ")

length = len(password)

uppercase = any(ch.isupper() for ch in password)
lowercase = any(ch.islower() for ch in password)
digit = any(ch.isdigit() for ch in password)
special = any(not ch.isalnum() for ch in password)

score = 0

if length >= 8:
    score += 1

if uppercase:
    score += 1

if lowercase:
    score += 1

if digit:
    score += 1

if special:
    score += 1

print("\n--- Password Strength Report ---")

print("Length:", length)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Number:", digit)
print("Special Character:", special)

if score <= 2:
    print("\nPassword Strength: WEAK")
    print("Improve your password by adding more characters.")

elif score <= 4:
    print("\nPassword Strength: MEDIUM")
    print("Add more security features.")

else:
    print("\nPassword Strength: STRONG")
    print("Your password is secure!")
