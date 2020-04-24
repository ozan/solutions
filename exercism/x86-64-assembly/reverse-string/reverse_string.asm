section .text
global reverse
reverse:
	mov rsi, rdi
.find_end:
	cmp byte [rsi], 0	; until we reach a null byte...
	je .loop
	inc rsi				; increment the source pointer
	jmp .find_end
.loop:
	mov al, [rsi - 1]   ; read from end
	mov bl, [rdi]		; read from start
	mov [rsi - 1], bl	; write back to end
	mov [rdi], al		; write back to start
	inc rdi
	dec rsi
	cmp rdi, rsi
	jl .loop	
    ret
