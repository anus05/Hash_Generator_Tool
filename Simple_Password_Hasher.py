import hashlib

print("Enter the text:")
data = input()

print("\nChoose Hash Algorithm:")
print("1. MD5")
print("2. SHA-1")
print("3. SHA-256")
print("4. SHA-512")

choice = input("Enter your choice (1-4): ")

match choice:
    case "1":
        hash_obj = hashlib.md5(data.encode())
    case "2":
        hash_obj = hashlib.sha1(data.encode())
    case "3":
        hash_obj = hashlib.sha256(data.encode())
    case "4":
        hash_obj = hashlib.sha512(data.encode())
    case _:
        print("Invalid choice!")
        exit()

result = hash_obj.hexdigest()
print("\nGenerated Hash:", result)