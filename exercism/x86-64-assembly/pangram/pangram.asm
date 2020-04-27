section .text
global is_pangram
is_pangram:
	; rdi: source string
	xor edx, edx
.loop:
	movzx rcx, byte [rdi]			; read next char
	bts rcx, 5						; force lower case (in ascii, 'a' + 32 -> 'A')
	sub rcx, 'a'
	bts edx, ecx					; set the corresponding bit in our bit set
	inc rdi
	cmp byte [rdi], 0
	jne .loop
	xor eax, eax
	and edx, 0x03ffffff
	cmp edx, 0x03ffffff
	sete al
    ret
