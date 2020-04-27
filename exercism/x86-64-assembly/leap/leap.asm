section .text
global leap_year
; Key ideas:
;
; - If 4 isn't a divisor, n is not a leap year.
; - If 4 is a divisor but 25 isn't, then 100 isn't a divisor,
;		so n IS a leap year.
; - If 25 is a divisor, then 400 is a divisor (so, n is a leap
;		year) iff 16 is also a divisor.
; - Divisibility by 4 and 16 can be quickly tested by and'ing
;		against 0b0011 and 0b1111 respectively.
; - Divisibility by 25 can be tested without `idiv` using the
;		multiplicative inverse mod 2**32
leap_year:
	xor eax, eax
	test edi, 3					; if ~(4|n), return 0
	jne .end

	mov eax, 1	
	imul ecx, edi, -1030792151	; multiply by modular inverse of 25
	cmp	ecx, 171798688			; compare to floor((2**32-1)/25)
	ja .end						; if ~(25|n), return 1

	xor eax, eax
	test edi, 15				; 25|n ^ 16|n => 400|n
	sete al						; return 400|n
.end:
	ret


; branchless approach: same as above, except compute all of:
;
; dl: n % 4 == 0
; cl: n % 25 == 0
; al: n % 16 == 0
;
; ... then return (dl && !cl) || (cl && al)
leap_year_branchless:
	xor edx, edx
	test edi, 3
	sete dl						; dl = n % 4 == 0
	
	xor ecx, ecx	
	imul esi, edi, -1030792151	; multiply by modular inverse of 25
	cmp	esi, 171798688			; compare to floor((2**32-1)/25)
	setbe cl					; cl = n % 25 == 0
	
	xor eax, eax
	test edi, 15
	sete al						; al = n % 16 == 0

	test cl, cl
	cmove eax, edx
	ret

