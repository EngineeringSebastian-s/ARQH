	.text
main:	mov r0,#0 @ total inicializado en Cero
	mov r1,#10 @ Inicialización de N en Diez
loop:	mov r2,r1 @ Copia N a R2
	mul r2,r1 @ Almacena N al Cuadrado en R2
	mul r2,r1 @ Almacena N al Cubo en R2
	add r0,r0,r2 @ Suma R0 y el cubo de N
	sub r1,r1,#1 @ decrementa N en 1
	bne loop @ salta a "loop" si n!=0
stop: 	wfi
	.end
