section .text
global leap_year_old
leap_year_old:
	
	xor eax, eax
	test edi, 3					; if n % 4 != 0, return 0
	jne .end

	imul edi, edi, -1030792151	; multiply by modular inverse of 25
	
	mov eax, 1	
	ror	edi, 2					; rotate by 2 to effectively multiply by 1/100
	cmp	edi, 42949672			; compare to floor((2**32-1)/100)
	ja .end						; n % 100 != 0, so return true
	
	ror edi, 2					; rotate by 2 again to effectively multiply by 1/400
	xor eax, eax
	cmp edi, 10737418			; compare to floor((2**32-1)/400)
	setbe al					; return num % 400 == 0
.end:
	ret
