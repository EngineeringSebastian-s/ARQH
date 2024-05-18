	.text
 main: 	mov r0, #2 @r0 <- 2
	mov r1, #3 @r1 <- 3
	add r2,r0,r1 @ r2 <- r0+r1
stop: wfi
	.end
