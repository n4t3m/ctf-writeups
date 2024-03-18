import hashlib

with open("/Users/natem135/Downloads/rockyou.txt", "rb") as file:
    for line in file:
        word = line.strip()
        try:
            email = f"{word.decode()}@1753ctf.com"
            email_hash = hashlib.md5(email.encode()).hexdigest()
            #print(f"{email} {email_hash}")
            if email_hash == "2471b1362bace767fdc0bb9c7e4df686":
                print(f"Found email: {email}")
                break
        except:
            pass