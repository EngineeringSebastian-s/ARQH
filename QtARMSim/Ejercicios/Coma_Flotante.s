 	.data

	@ --------------
	@ Inicialización
	@ --------------
num: .float 3.1416 @ Inicializa el número en formato IEEE 754 de 32 bits
str_f: 	.asciz "%d / %d = %f"

	.text

	@ --------------
	@ Programa Invocador
	@ --------------
	
main:	
	
   	ldr r0, =num 
    	ldr r1, [r0]
	mov r2, #7
    	sub sp, sp, #8       @ Reserva espacio para dos palabras (2*4 bytes = 8 bytes) en la pila
    	str r1, [sp, #4]      @ Almacena el segundo termino en la primer word del stack pointer, mediante str
    	str r2, [sp]          @ Almacena el operador en la word del stack pointer, mediante str
    	mov r3, #22      @ Almacena el primer termino una word antes del stack pointer, mediante str
    	mov r0, #0           @ Columna para PrintF
    	mov r1, #0
	orr r2,r2,r1
    	ldr r2, =str_fYO M
    	bl printf
    	add sp, sp, #8

stop: wfi
