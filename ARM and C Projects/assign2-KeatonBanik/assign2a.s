	//Author: Keaton Banik
	//Description: Assembly Code without macros for Assignment 2.
	//Prints out a User Inputed Number of Random numbers between 0-9 and calculates and prints the frequency and sum/size of the numbers generated


//String Formats
fmt:		.string "Enter a number between 5-20: " 			// Format String for Initial Prompt
input0:		.string "%d" 							// Format String for scanf input
word:		.string "\n The input numbers are: \n" 				// Format String for output displaying 
rannum:		.string "%d " 							// Format String for to output random generated numbers
lowTxt:		.string "User Input is too low, Please Try again \n" 		// Format String to output Error message of a user input too low
highTxt:	.string "User Input is too high, Please Try again \n" 		// Format String to output Error message of a suer input too high
sizeTxt:	.string "The size of the document is: %d \n" 			// Format String to output Size of documented
lowFreqTxt:	.string "The Lowest frequency in the document is: %d % \n"	// Format String to output lowest frequency
highFreqTxt:	.string "The Highest frequency in the document is: %d % \n" 	// Format String to output highest Frequency



	//Main Declaration
	.balign 4 //Forces Alignment
	.global main

main:	stp	x29,x30, [sp, -16]!	//Saves State
	mov	x29, sp 		//Saves State to x29
	
	ldr	x0, =fmt		// Loades Format String for Initial Prompt
	bl 	printf			// Prints Intial Prompt
	
	ldr 	x0, =input0 		// Loads Format String for user input
	ldr	x1, =input 		// Loads integer Value for user input
	bl	scanf 			// Scans for user input
	ldr	x1, =input 		//Loads user input into x1
	ldr 	x19, [x1] 		// Loads value x1 points to in x19
	mov 	x20, 5 			//sets x20 value to 5 (min user input)
	mov 	x21, 20 		// sets x21 value to 20 (max user input)

	cmp 	x19,x20 	//compares User Input value to lower bound
	b.lt 	lowTest 	//If user input is less than Lower Bound -> lowTest, else continue
	cmp 	x19, x21 	//compares User Input value to upper bound
	b.gt	highTest	//If user input is greater than upper bound -> hightest, else continue
	

	//Intializes Registers
	mov 	x20, 1 	//Sets x20 to 1, counter for loop
	mov	x21, 0 	//Use for random number
	mov 	x22, 0 	// used to store max for random numbers
	mov 	x23, 0 	// Stores Random number (0-9)
	mov 	x24, 10 //Stores lowest frequency, set to 10 as all initial values will be less than 10
	mov 	x25, 0 	//Stores highest frequency, set to 0 as initial values will be greater than or equal to 0
	mov 	x26, 0 	//Stores sum of all occurances
	mov	x27, 100//Stores the number 100 for frequency calculation
	mov	x28, 0	//Stores frequency 

	ldr 	x0, =word 	//Loads format string for list of numbers title
	bl	printf 		//prints format string for list of numbers title


	//initializes time and srand for rand
	mov 	x0, 0 	// Initialized x0 to 0 for time and srand
	bl 	time	//initializes time
	bl 	srand	//initializes srand


	//test loop
test:	cmp	x20, x19 	// loop comparison, compares user input value to counter
	b.gt	next 		//if counter is greater than user input value -> next, else continue
	mov     x0, 0 		//Initializes x0 to 0 for rand
	bl      rand		//initializes rand numb to x0


	//Modulus stored in x23 (random number)
	mov     x21, x0 //random number saved in x21
	mov     x22, 10 // x22 stores top threshold for random number
	sdiv    x23, x21, x22 // divides random number/top threshold, stores in x23
	mul     x23, x23, x22 // multiply quotient * top threshold, store in x23
	sub     x23, x21, x23 //subtract random number by above answer, save in x23
	mov     x1, x23      // Moves modulus number to x1 argument for print argument


	//Prints random number
	ldr     x0, =rannum 	//loads format string to random number list
	bl      printf 		// prints random number
	//argument 1 is x1 (random number)

	
	//Check if Lowest and Highest Frequency
	cmp	x23, x24 	// compares random number to current lowest frequency
	b.lt	lowFreq 	//if random number is lower than lowest frequency -> lowFreq, else continue

	cmp 	x23, x25	//compares random number to current highest frequency
	b.gt	highFreq	//if random number is higher than highest frequency -> highFreq, else continue

	
	add 	x26, x26, x23	//adds random number to sum total
	add	x20, x20, 1	//increments 1 to counter
	b 	test 		//loops test case

	
//sets lowest frequency
lowFreq:
	mov 	x24, x23	//sets current lowest frequency to random number
	cmp	x23, x25 	// compares random number to current highest frequency
	b.gt	highFreq 	// if random number is higher than highest frequency -> highfreq, else continue
	add 	x26,x26,x23 	// adds random number to sum total
	add	x20, x20, 1	// increments 1 to counter
	b 	test 		// loops test case

//sets highest frequency
highFreq:
	mov 	x25, x23 	// sets current highest frequency to random number
	add	x26, x26, x23 	// adds random number to sum total
	add	x20,x20,1 	//increments 1 to counter
	b	test 		//loops test case

//prints error message and ends program
lowTest:
	ldr	x0, =lowTxt 	// loads format string for user input too low
	bl 	printf		//prints string for user input too low
	//ends program, Restores state of Frame pointer and Link register
	ldp     x29,x30,[sp],16
	ret
	

	
//prints error message and ends program
highTest:
	ldr     x0, =highTxt 	// loads format string for user input too high
	bl 	printf 		// prints string for user input too high
	//ends program, Restores state of Frame pointer and Link register
	ldp     x29,x30,[sp],16
	ret


	
//calcuates frequency and prints, then ends program
next:
	
	mul	x28,x27,x24 	//Multiplication for frequency (100 x lowest frequency) stores in x28 
	udiv	x28,x28,x26 	//divides x28 by size/sum of document, stores back in x28

	ldr	x0, =sizeTxt	//Loads format string for document sum/size
	mov 	x1, x26		//sets x1 first argument to size/sum of document
	bl 	printf		//prints format string of document size/string

	ldr	x0,=lowFreqTxt	//Loads format string for lowest frequency
	mov	x1,x28		//sets x1 first argument to lowest frequency
	bl	printf		//prints format string of lowest frequency
	
	mul 	x28, x27, x25	//Multiplication for frequency (100 x highest frequency) stores in x28
	udiv	x28, x28, x26	//divides x28 by size/sum of document, stores back in x28

	ldr	x0, =highFreqTxt// Loads format string for highest frequency
	mov	x1, x28		//sets x1 first argument to highest frequency
	bl 	printf		//prints format string of highest frequency
	

	//ends program, Restores state of Frame pointer and Link register
	ldp	x29,x30,[sp],16
	ret

//ends program, restores state of frame pointer and link register
end:

	ldp	x29,x30,[sp],16
	ret


	.data
//data for integer user input
input:	 .int	0
