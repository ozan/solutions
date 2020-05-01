section .text
global square
square:
	xor eax, eax
	dec edi
	bts rax, rdi					; Generally, we just set the n-1th bit
	xor ecx, ecx
	test rdi, 0xffffffffffffffc0	; But if the 7th or higher bit of n-1 is set,
	cmova rax, rcx					; n is not in range (0, 64] so return 0 instead.
    ret

global total
total:
	mov rax, -1
    ret
