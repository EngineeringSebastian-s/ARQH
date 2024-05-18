        .data      @ Comienzo de la zona de datos 
word1:	.word 15   @ Numero en decimal
word2:	.word 0x15 @ Numero en hexadecimal
word3:	.word 015  @ Numero en octal
word4:	.word 0b11 @ Numero en binario

	.text
stop:	wfi
