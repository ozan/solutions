section .text
global distance
distance:
	xor eax, eax
	xor r9, r9
.loop:	
	movzx edx, byte [rdi + r9]
	movzx ecx, byte [rsi + r9]
	inc r9
	xor r8, r8
	cmp edx, ecx
	setne r8b				; If chars are not equal,
	add eax, r8d			; increment count.
	or edx, ecx				; If both are zero, return count.
	jz .end
	test edx, ecx			; If neither is zero, loop again.
	jne .loop
	mov eax, -1
.end:	
    ret
