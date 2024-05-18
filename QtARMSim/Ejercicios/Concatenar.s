.data
point: .word 46
dec1: .word 48
dec2: .word 48
result: .asciz ""
format: .asciz "%s\n"  @ Formato para imprimir un entero seguido de un salto de línea

.text
main:
    
    ldr r0,=point
    ldr r0,[r0]
    ldr r1,=dec1
    ldr r1,[r1]
    ldr r2,=dec2
    ldr r2,[r2]

    mov r4, #52        @ Inicializa r4 como 0

    lsl r4, r4, #8    @ Desplaza r4 8 bits a la izquierda
    orr r4, r4, r2    @ Combina r0 con r4 usando OR
    lsl r4, r4, #8    @ Desplaza r4 8 bits a la izquierda
    orr r4, r4, r1    @ Combina r1 con r4 usando OR
    lsl r4, r4, #8    @ Desplaza r4 8 bits a la izquierda
    orr r4, r4, r0    @ Combina r2 con r4 usando OR
    lsl r4, r4, #8    @ Desplaza r4 8 bits a la izquierda
    
    

    ldr r5, =result   @ Carga la dirección de memoria result en r5
    str r4, [r5]      @ Almacena el resultado concatenado en la dirección de memoria cargada en r5

    mov r0, #0        @ Columna para printf
    mov r1, #0        @ Fila para printf
    ldr r2, =format   @ Carga la dirección de memoria del formato en r2
    ldr r3, =result   @ Carga la dirección de memoria del resultado en r3
    ldr r3, [r3]      @ Carga el valor almacenado en la dirección de memoria del resultado
    bl printf         @ Imprime el valor concatenado usando printf

    b stop            @ Retorna

stop: wfi
