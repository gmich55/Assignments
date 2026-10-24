password = input("Enter a password: ")

special_chars = "!@#$%^&"

hl = False
hu = False
hd = False
hs = False

for ch in password:
    if ch.islower():
        hl = True
    elif ch.isupper():
        hu = True
    elif ch.isdigit():
        hd = True
    elif ch in special_chars:
        hs = True

if len(password) >= 8 and hl and hu and hd and hs:
    print("Strong password!")
else:
    print("Weak password. It needs:")
    if len(password) < 8:
        print("  - at least 8 characters")
    if not hl:
        print("  - a lowercase letter")
    if not hu:
        print("  - an uppercase letter")
    if not hd:
        print("  - a digit")
    if not hs:
        print("  - a special character (!@#$%^&)")