        .data
str:	.asciz "%d dividido entre %d es igual a: %d" 

	.text
	mov r0, #50
	mov r4, r0
	mov r1, #2
	mov r5, r1
	mov r0, #25     @ Divide 50 entre 2
	sub sp, sp, #8
	str r0, [sp, #4]
	str r5, [sp]
	mov r3, r4
	mov r0, #0
	mov r1, #0
	ldr r2, =str
	bl  printf	@ Imprime dividendo, divisor y resultado
	add sp, sp, #8
stop:	wfi
