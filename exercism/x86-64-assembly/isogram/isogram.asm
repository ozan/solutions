section .text
global is_isogram
is_isogram:
	xor eax, eax
	xor edx, edx 			; Use a 32-bit bitset
.loop:
	movzx ecx, byte [rdi]
	or ecx, 32 				; Downcase.
	test ecx, 64  			; If the 7th bit is not set,
	cmove ecx, eax			; target the 0th bit of the bitset,
	and dl, 0xfe 			; which we just ignore.
	bts edx, ecx			; Set the nth bit, mod 64.
	jb .end					; If it was already set, return false.
	inc rdi
	cmp byte [rdi-1], 0
	jne .loop
.end:
	setnb al
    ret
