words = input()
keyword = input()
words = "".join([w for w in words if w.isalpha()])

print(1 if keyword in words else 0)