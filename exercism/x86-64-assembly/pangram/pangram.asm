section .text
global is_pangram
is_pangram:
	; rdi: source string
	xor rax, rax
.loop:
	movzx rcx, byte [rdi]			; read next char
	cmp rcx, 'a'					; if upper case, make lower
	jae .set_bit
	add rcx, 32						; in ascii, X + 32 = x
.set_bit:
	sub rcx, 'a'
	bts rax, rcx					; set the corresponding bit in our bit set
	inc rdi
	cmp byte [rdi], 0
	jne .loop
.end:
	and rax, 0x0000000003ffffff
	cmp rax, 0x0000000003ffffff
	sete al
	movzx rax, al
    ret
