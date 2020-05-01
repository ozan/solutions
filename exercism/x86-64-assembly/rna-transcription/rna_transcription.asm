default rel

section .rodata
mapping:
	db 0	
	times 64 db ' '
	db "U G   C            A"
	times 165 db ' '

section .text
global to_rna
to_rna:
	; rdi: dna strand string
	; rsi: output buffer
 	lea rax, [mapping]
	xor edx, edx
.loop:
	movzx ecx, byte [rdi + rdx]	; get dna char
	mov cl, [rax + rcx]   ; get translated rna char
	mov [rsi + rdx], cl			; write back rna char
	inc rdx
	cmp byte [rdi + rdx], 0
	jne .loop
    ret

