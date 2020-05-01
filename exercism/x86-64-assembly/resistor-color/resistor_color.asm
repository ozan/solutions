default rel

section .text
global color_code
; Strategy: Since no color has >= 8 characters, store them
; aligned to 64 bits, with null padding. As we iterate,
; we can then locate colors at `start + i * 8`. In order
; to compare these to the string at [rdi], we must clean
; it up first, since the 8 bytes starting at [rdi] could
; include non-null bytes after the terminating null byte.
; These subsequent bytes can be found and zero'ed out
; using a trick adapted from chapter 6 of Hacker's Delight
; where given the magic number M = 0x7f7f7f7f7f7f7f7f,
; the expression:
;
; 	y = ~(((x & M) + M) | x | M)
;
; ... will have a single set bit corresponding to the
; locating of the first null byte. We can then decrement
; to create a mask.
color_code:

	mov rdx, [rdi]				; Read the parameter x
	mov r9, 0x7f7f7f7f7f7f7f7f	; Load our magic number M.
	mov r10, rdx				; y = x
	and r10, r9					; 	  x & M
 	add r10, r9					;     (x & M) + M
	or r10, rdx					;     ((x & M) + M) | x
	or r10, r9					;     ((x & M) + M) | x | M
	not r10						; r10's single bit indicates first null in x.
	dec r10						; We want only the LOW ORDER bytes.
	and rdx, r10				; So zero out trailing (high order) bytes.

	xor eax, eax
	lea r8, [black]
.loop:							; Iterate over colors until...
	mov rcx, [r8 + 8*rax]
	test rcx, rcx  				; ... end of array...
	je .fail					
	inc rax
	cmp rcx, rdx				; ... or exact match.
	jne .loop
	dec rax
	ret
.fail:
	mov eax, -1
    ret


global colors
colors:
	lea rax, [all_colors]
    ret


section .rodata
black: db "black", 0, 0, 0
brown: db "brown", 0, 0, 0
red: db "red", 0, 0, 0, 0, 0
orange: db "orange", 0, 0
yellow: db "yellow", 0, 0
green: db "green", 0, 0, 0
blue: db "blue", 0, 0, 0, 0
violet: db "violet", 0, 0
grey: db "grey", 0, 0, 0, 0
white: db "white", 0, 0, 0
	dq 0

all_colors:
	dq black
	dq brown
	dq red
	dq orange
	dq yellow
	dq green
	dq blue
	dq violet
	dq grey
	dq white
	dq 0
