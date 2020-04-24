default rel

section .rodata
mapping: db "U G   C            A"

section .text
global to_rna
to_rna:
	; rdi: dna strand string
	; rsi: output buffer
 	lea rax, [mapping]
.loop:
	cmp byte [rdi], 0
	je .end
	movzx rbx, byte [rdi]		; get dna char
	mov cl, [rax + rbx - 'A']   ; get translated rna char
	mov [rsi], cl				; write back rna char
	inc rdi
	inc rsi
	jmp .loop
.end:
    ret

