section .text
global reverse
reverse:
	mov rsi, rdi
.find_end:
	inc rsi					; increment the source pointer
	cmp byte [rsi-1], 0 	; until we reach a null byte
	jne .find_end
	sub rsi, 2
.loop:
	movzx eax, byte [rsi]   ; read from end
	movzx ecx, byte [rdi]	; read from start
	mov [rsi], cl			; write back to end
	mov [rdi], al			; write back to start
	inc rdi
	dec rsi
	cmp rdi, rsi
	jl .loop	
    ret
