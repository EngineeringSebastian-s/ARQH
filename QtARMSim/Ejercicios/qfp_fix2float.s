.data
str_f: .asciz "%f\n" @ Define el formato de impresión para una cadena seguida de un salto de línea

.text
main:
    mov r0, #100         @ Valor de punto fijo (por ejemplo, 100)
    mov r1, #8           @ Número de bits fraccionarios (por ejemplo, 8)
    bl qfp_fix2float     @ Convierte el valor de punto fijo a punto flotante
    mov r3,r0
    mov r0,#0
    mov r1,#0
    ldr r2,=str_f
    bl printf          @ Imprime el valor de Pi en formato flotante
