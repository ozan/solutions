default rel

section .rodata
prefix:	db	"One for "
you:	db	"you"
suffix: db	", one for me.", 0

section .text
global two_fer
two_fer:
	; rdi: name
	; rsi: output buffer
	mov rax, rdi		; save reference to name
	mov rdi, rsi		; set up movsb destination in rdi
	lea	rsi, [prefix]	; copy prefix
	mov rcx, 8
	rep movsb
	mov rsi, rax
	cmp rax, 0			; if name is given, use it
	jne .use_name
	lea rsi, [you]		; by default, use "you"
	mov rcx, 3
	rep movsb
	jmp .end	
.use_name:
	movsb
	cmp byte [rsi], 0
	jne .use_name	
.end:
	lea rsi, [suffix]
	mov rcx, 14
	rep movsb
    ret
