        .data      @ Comienzo de la zona de datos

byte:	.byte 0xff
	.balign 4
str2:	.asciz "abcde" 
byte2:	.byte 0xff

	.text
main:	mov r0,#1 @ Columna de Print
	mov r1, #1 @ Fila de Print
	ldr r2, .ascii "abcde"
	bl printString

stop:	wfi
