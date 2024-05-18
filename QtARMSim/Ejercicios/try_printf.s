	.data
str: .asciz "Operando: %d %c %d = %d"

	.text
main:
    mov r0, #5           @ Primer operando
    mov r1, #'+'         @ Operador (en este caso, suma)
    mov r2, #3           @ Segundo operando
    mov r5, #8           @ Almacena el resultado en r3

    sub sp, sp, #16      @ Reserva espacio para cuatro palabras (4 * 4 bytes = 16 bytes) en la pila
    str r5, [sp, #8]     @ Almacena el resultado dos words adelante del stack pointer
    str r2, [sp, #4]     @ Almacena el segundo termino una word adelante del stack pointer
    str r1, [sp]         @ Almacena el operador en la word del stack pointer
    mov r3, r0		 @ Almacena el primer termino una word antes del stack pointer

    mov r0, #0           @ Columna para PrintF
    mov r1, #0           @ Fila para PrintF
    ldr r2, =str         @ Carga la dirección de la cadena de formato en r2
    bl printf            @ Llama a printf para imprimir la cadena formateada

    add sp, sp, #16      @ Restaura el puntero de pila después de usarla

stop: wfi
