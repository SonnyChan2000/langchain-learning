text = "  The quick brown fox jumps over the lazy dog.  "

print(text.strip())
print(text.lower())
print(text.strip().split())
print(text.lower().count("the"))
print(text.strip().replace(" ", "_"))
print(",".join(text.strip().split()))