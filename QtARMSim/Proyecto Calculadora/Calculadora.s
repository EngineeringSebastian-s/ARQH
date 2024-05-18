	.data

	@ --------------
	@ Inicialización
	@ --------------
num1:	.word 0
num2: 	.word 0
ope:	.word 0
sym:	.word 32
res:	.word 0
point:  .word 32
dec1:	.word 32
dec2:	.word 32
dec3:	.word 32
dec4:	.word 32
str_f: 	.asciz "%d %c %d = %c%d%c%c%c%c"
ind_div: .asciz "n/0 = ? "
ind_pow: .asciz "0^0 = ? "


	.text

	@ --------------
	@ Programa Invocador
	@ --------------

main:
    	bl write
    	cmp r2,#'+'
    	beq sum
    	cmp r2,#'-'
    	beq subtract
    	cmp r2,#'*'
    	beq multiply
    	cmp r2,#'/'
    	beq divide
	cmp r2,#'^'
    	beq potencia
	cmp r2,#'%'
    	beq modulo

    	b stop

stop:	wfi

	@ --------------
	@ Subrutinas
	@ --------------

sum:
    	add r3, r0, r1     @ Suma los operandos
	ldr r4,=res
	str r3,[r4]
   	b print_result

subtract:
	sub r3, r0, r1     @ Resta el segundo operando al primero
	ldr r4,=res
	str r3,[r4]
	b print_result

multiply:
    	mov r3,r0
    	mul r3, r1     @ Multiplica los operandos
	ldr r4,=res
	str r3,[r4]
    	b print_result

potencia:
	@Potencia cero^cero
	cmp r1,#0
	bne not_ind_pow
	cmp r0,#0
	ldr r2,=ind_pow
	beq print_ind
	ldr r4,=res
	mov r3, #1
	str r3,[r4]
	bl print_result
not_ind_pow:
	

	mov r4,#0 @ Inicializar Iterador
	mov r5,r1 @ Rango final del Iterador
	@Invertir potencias negativas
	cmp r1,#0
	bge not_invert_pow
	mov r2,#0
	sub r2,r2,#1
	mul r5,r5,r2
not_invert_pow:
	mov r3,#1
loop_pow:
	mul r3,r3,r0
	add r4,r4,#1 @Incrementa en Uno
	cmp r4,r5 @ Comparar Inicio y Final
	bne loop_pow
	
	cmp r1,#0
	bge print_pow
	mov r0,#1
	mov r1,r3
	mov r2,#'/'
	bl write
	b divide
print_pow:
	ldr r4,=res
	str r3,[r4]
    	b print_result

modulo:
	@División entre cero
	cmp r1,#0
	ldr r2,=ind_div
	beq print_ind

	@Invertir (Dado que cuando la división no es exacta solo toma el signo de dividendo)
	cmp r1,#0
	bgt not_invert_mod
	mov r2,#0
	sub r2,r2,#1
	mul r0,r0,r2
	mul r1,r1,r2
not_invert_mod:
	bl sdivide @ Implementar sdivide con r0,r1, dejando r0 como resultado y r1 como residuo
	ldr r3,=res
	str r1,[r3]
	
	@ symbol
	cmp r1,#0
	bge not_sym
	cmp r0,#0
	bne not_sym
	ldr r4,=sym
	mov r5, #'-'
	str r5,[r4]
not_sym:
	b print_result

divide:
	@División entre cero
	cmp r1,#0
	ldr r2,=ind_div
	beq print_ind
	
	@Invertir (Dado que cuando la división no es exacta solo toma el signo de dividendo)
	cmp r1,#0
	bgt not_invert_div
	mov r2,#0
	sub r2,r2,#1
	mul r0,r0,r2
	mul r1,r1,r2
not_invert_div:
	bl sdivide @ Implementar sdivide con r0,r1, dejando r0 como resultado y r1 como residuo
	ldr r3,=res
	str r0,[r3]
	

	@ symbol
	cmp r1,#0
	bge not_add_sym
	cmp r0,#0
	bne not_add_sym
	ldr r4,=sym
	mov r5, #'-'
	str r5,[r4]
not_add_sym: 

	@ Calcular Decimales

	mov r4,#1 @ Inicializar Iterador
	mov r5,#5 @ Rango final del Iterador
loop_dec:
	@ Valor Absoluto
	cmp r1,#0
	bge not_abs
	mov r2,#0
	sub r2,r2,#1
	mul r1,r1,r2
not_abs:
	@ Preparación del Residuo
	mov r6,#10 @ Inicilizar base numerica
	mul r1, r6 @ Multiplica el Residuo por la base numerica
    	mov r0,r1 @ Guarda el residuo*base n en r0 para sdivide, como nuevo dividendo
	
	@ Carga de Divisor
	ldr r3,=num2	@ Referencia en Memoria para el divisor
	ldr r1,[r3] @ Carga el mismo divisor previamente guardado

	@Invertir (Dado que cuando la división no es exacta solo toma el signo de dividendo)
	cmp r1,#0
	bgt not_invert_lp
	mul r1,r1,r2
not_invert_lp:
	
	@ División
    	bl sdivide @ Implementa sdivide con r0,r1, dando r0 como resultado y r1 como residuo
	
	@ Configuración Dirección en Memoria dinamica
	ldr r3,=point @ Referencia en memoria para Decimales
	mov r6,#4 @ Bytes de Desplazamiento
	mov r7,r4 @ Copias Iterador
	mul r7,r6 @ Numero de Iteración * 4 bits, para acceder al decimal correspondiente de la Iteración

	@ Carga de Resultado
	add r0, r0, #48 @ En ascii los caracteres de numeros empiezan en 48
	str r0,[r3,r7] @ Guarda el Decimal en Memoria  

	add r4,r4,#1 @Incrementa en Uno
	cmp r4,r5 @ Comparar Inicio y Final
	bne loop_dec
	
	@ Colocar el Punto de Decimal
	ldr r3,=point
	mov r4,#46
	str r4, [r3]
	
	@ Redondear
		
	@ Carga Decimal
	ldr r2,=dec3
	ldr r0,[r2]

	@Carga Decimal Extra
	ldr r3,=dec4
	ldr r1,[r3]
	
	cmp r1,#53
	blt not_round @Compara si el decimal extra calculado es menor que 5 en ascii
	
	@ Cambia el Decimal
	add r0,r0,#1
	str r0,[r2]

not_round:
	mov r0,#16 @ Inicializar Iterador (4*(Cantidad de Decimales a evaluar+1))
	mov r1,#0 @ Rango final del Iterador
	ldr r2,=point @ Tomar referente de desplazamiento el punto
loop_cant_dec:
	ldr r3,[r2,r0]
	cmp r3,#48 @ Verificar si no es un cero (48 en ASCCI corresponde al cero)
	bne end_dec
	
	mov r4,#32 @ Inicializar Espacio en ASCII
	str r4,	[r2,r0] @ Modificar cero a la derecha como un espacio

	sub r0,r0,#4 @Decrementa en Uno
	cmp r0,r1 @ Comparar Inicio y Final
	bne loop_cant_dec
	str r4,[r2]
end_dec:
	b print_result
	
print_ind:
	mov r0, #0           @ Columna para PrintString
    	mov r1, #0           @ Fila para PrintString
	bl printString
	bl read
	b stop


print_result:
	@ Carga de Memoria
	bl read
    	sub sp, sp, #32       @ Reserva espacio (Cada formato es una palabra, pero r3 envia el primer parametro) para Nueve palabras menos una (8*4 bytes = 28 bytes) en la pila
	str r7, [sp, #28]     @ Almacena el tercer resultado decimal en la quinta words adelante del stack pointer, mediante str
	str r6, [sp, #24]     @ Almacena el segundo resultado decimal en la quinta words adelante del stack pointer, mediante str
   	str r5, [sp, #20]     @ Almacena el primer resultado decimal en la cuarta words adelante del stack pointer, mediante str
	ldr r5,=point
	ldr r5,[r5] 	      @ Carga el valor del puntero ( 32 Espacio o 46 Punto)
	str r5, [sp, #16]     @ Almacena el primer resultado decimal en la cuarta words adelante del stack pointer, mediante str
	str r4, [sp, #12]     @ Almacena el resultado en la tercera words adelante del stack pointer, mediante str
    	str r3, [sp, #8]      @ Almacena el signo del resultado (Para cuando sea cero con parte decimal negativa) en la segunda word adelante del stack pointer, mediante str
    	str r1, [sp, #4]      @ Almacena el segundo termino en la primer word del stack pointer, mediante str
    	str r2, [sp]          @ Almacena el operador en la word del stack pointer, mediante str
    	mov r3, r0	      @ Almacena el primer termino una word antes del stack pointer, mediante str
    	mov r0, #0           @ Columna para PrintF
    	mov r1, #0           @ Fila para PrintF
    	ldr r2, =str_f         @ Carga la dirección de la cadena de formato en r2
    	bl printf            @ Llama a printf para imprimir la cadena formateada

    	add sp, sp, #28      @ Restaura el puntero de pila después de usarla
	bl read
    	b stop


read:
	ldr r7,=num1
	ldr r0,[r7]
	ldr r7,=num2
	ldr r1,[r7]
	ldr r7,=ope
	ldr r2,[r7]
	ldr r7,=sym
	ldr r3, [r7]
	ldr r7,=res
	ldr r4, [r7]
	ldr r7,=dec1
	ldr r5,[r7]
	ldr r7,=dec2
	ldr r6,[r7]
	ldr r7,=dec3
	ldr r7,[r7]
	bx lr

write:
	ldr r4, =num1
	ldr r5, =num2
        ldr r6, =ope
	str r0, [r4]
	str r1, [r5]
	str r2, [r6]
	bx lr
	.end
