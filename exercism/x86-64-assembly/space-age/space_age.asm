default rel

section .text
global age
age:
	cvtsi2ss xmm0, rsi
	lea rdx, [earth_seconds]
	divss xmm0, [rdx + 4 * rdi]
    ret

section .rodata
earth_seconds:
	dd 7600543.8
	dd 19414149.1
	dd 31557600.0
	dd 59354032.7
	dd 374355659.1
	dd 929292362.9
	dd 2651370019.3
	dd 5200418560.0
