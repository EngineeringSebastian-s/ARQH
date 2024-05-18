	.equ Monday, 1
	.equ Tuesday, 2

	.text
	day .req r7
main:	mov r0, #Monday
	mov r1, #Tuesday
	mov day, #3
	.unreq day
stop:	wfi
	.end
