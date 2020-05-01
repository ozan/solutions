section .text
global is_pangram
is_pangram:
	; rdi: source string
	xor edx, edx
.loop:
	movzx ecx, byte [rdi]	; read next char
	or ecx, 32				; force lower case (in ascii, 'a' + 32 -> 'A')
	sub ecx, 'a'
	bts edx, ecx			; set the corresponding bit in our bit set
	inc rdi
	cmp byte [rdi], 0
	jne .loop
	xor eax, eax
	and edx, 0x03ffffff
	cmp edx, 0x03ffffff		; it's a pangram if low order 26 bits are set
	sete al
    ret
