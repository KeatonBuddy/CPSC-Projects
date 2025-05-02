// Author: Abdelghani
// Desc: exmaple shopwing the use of 2 global initialized variables and one global non initialized variable
// Computing y = x power n. x and n are assumed to be greater than 0
	inputStr: .string "%d %d"
	outputStr: .string "%d to the %d is %d \n"

	define(x_r, x9)
	define(n_r, x10)
	define(y_r, x11)
	define(i_r, x12)
	define(temp_r, x13)

	.balign 4	
	.global main
main: //void main()
	stp 	x29,	x30,	[sp, -16]!
	mov 	x29,	sp

	bl 	getInput
	bl 	power
	bl 	printY
	
	ldp 	x29,	x30, 	[sp], 16
	ret //End of main

power: 	//void power(). Leaf function, no need for a frame record.
	//Computing x to the n
    	ldr     temp_r,     =varX      		//Load regsiter x13 with the address of varX
        ldr     x_r,      [temp_r]            	//Store 1st number entered by user in register x9
        ldr     temp_r,    =varN           	//Load register x13 with the address of varN
        ldr     n_r,      [temp_r]            	//Store 2nd number entered by user in register x10
        mov     y_r,      1               	//Initializing y

	mov 	i_r, 	n_r
	b ltest
loop:	mul 	y_r,	y_r,	x_r
	sub	i_r,	i_r,	1
ltest:  cmp	i_r, 	0
	b.gt	loop

	ldr 	temp_r, =varY
	str 	y_r,	[temp_r]
	ret //End of power subroutine 

getInput: //void getInput()  
	stp 	x29,	x30,	[sp, -16]!
	mov 	x29,	sp

	//Getting user input using the C function scanf
        ldr     x0,     =inputStr       //Load register x0 with the address of string inputStr
        ldr     x1,     =varX           //Load regsiter x1 with the address of varX
        ldr     x2,     =varN           //Load register x2 with the address of varN
        bl      scanf                   //Call function scanf

	ldp 	x29,	x30, 	[sp], 16
	ret //End of getInput subroutine

printY: //void printY() 
	stp 	x29,	x30,	[sp, -16]!
	mov 	x29,	sp

	//Printing result using the C function printf
	ldr 	x0,	=outputStr 	//Load register x0 with the address of string outputStr
   	ldr     temp_r, =varX
        ldr     x1,     [temp_r]	
	ldr	temp_r,	=varN
	ldr 	x2, 	[temp_r]
	ldr     temp_r, =varY
        ldr     x3,     [temp_r]
	bl	printf

	ldp 	x29,	x30, 	[sp], 16
	ret //End of printY subroutine
	
	.data //Global Initialized Variables
varX: 	.dword	1 //scanf will store first number entered by user in this memory location
varN: 	.dword	1 //scanf will store 2nd number entered by user in this memory location

	.bss //Global Zero Initialized Variables
varY:	.skip 	8 // size = 8 bytes


