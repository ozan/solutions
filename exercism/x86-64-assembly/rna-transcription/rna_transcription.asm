default rel

section .rodata
mapping: db "U G   C            A"

section .text
global to_rna
to_rna:
	; rdi: dna strand string
	; rsi: output buffer
 	lea rax, [mapping]
	xor edx, edx
.loop:
	cmp byte [rdi + rdx], 0
	je .end
	movzx rcx, byte [rdi + rdx]	; get dna char
	mov cl, [rax + rcx - 'A']   ; get translated rna char
	mov [rsi + rdx], cl			; write back rna char
	inc rdx
	jmp .loop
.end:
    ret

