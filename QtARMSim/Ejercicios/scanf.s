	.data
input_message: .asciz "Ingrese un número entero: "
output_message: .asciz "El número ingresado es: %d\n"
number: .word 0

	.text
main:
    @ Solicitar al usuario que ingrese un número entero
    ldr r0, =input_message
    bl printf

    @ Leer el número entero ingresado por el usuario
    ldr r0, =number
    bl scanf

    @ Mostrar el número ingresado en pantalla
    ldr r0, =output_message
    ldr r1, =number
    ldr r1, [r1]   @ Cargar el valor del número desde su dirección en la memoria
    bl printf

    @ Finalizar el programa
    mov r0, #0
    bx lr
