section .text
global square_of_sum
; Square of sum of first n integers, ie (n(n + 1)/2)**2
square_of_sum:
	lea eax, [edi + 1]
	mul edi
	shr eax, 1
    mul eax
	ret

global sum_of_squares
; nth square pyramidal number, ie n(n + 1)(2n + 1)/6
sum_of_squares:
	lea eax, [edi + 1]
	mul edi
	lea edi, [2*edi + 1]
	mul edi
	mov edi, 0xAAAAAAAB		; To avoid div by 6,
	imul rax, rdi			; multiply by (2**33 + 1)/3.
	shr rax, 34				; Answer is in high order 30 bits.
    ret

global difference_of_squares
; Effectively, square_of_sum(n) - sum_of_squares(n)
; but calculated using the simpler expression:
;
; 	n(n + 1)(n - 1)(3n + 2)/12
;
; to avoid a few extra instructions + function call overhead.
difference_of_squares:
	lea eax, [edi + 1]
	lea ecx, [edi - 1]
	mul edi
	mul ecx
	lea edi, [2*edi + edi + 2]
	mul edi
	mov edi, 0xAAAAAAAB		; To avoid div by 12,
	imul rax, rdi			; multiply by (2**33 + 1)/3.
	shr rax, 35				; Answer is in high order 29 bits.
    ret
