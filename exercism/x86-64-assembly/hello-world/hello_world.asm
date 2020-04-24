default rel

section .rodata
msg: db "Hello, World!", 0

section .text
global hello
hello:
    lea rax, [msg]
    ret
