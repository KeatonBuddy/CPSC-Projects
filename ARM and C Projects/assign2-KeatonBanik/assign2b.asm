	//Author: Keaton Banik
	//Description: Assembly Code with macros for Assignment 2.
	//Prints out a User Inputed Number of Random numbers between 0-9 and calculates and prints the frequency and sum/size of the numbers generated


	//String Formats
fmt:			.string "Enter a number between 5-20: " 			// Format String for Initial Prompt
input0:			.string "%d" 							// Format String for scanf input
word:			.string "\n The input numbers are: \n" 				// Format String for output displaying
rannum:			.string "%d " 							// Format String for to output random generated numbers
lowTxt:			.string "User Input is too low, Please Try again \n" 		// Format String to output Error message of a user input too low
highTxt:		.string "User Input is too high, Please Try again \n" 		// Format String to output Error message of a suer input too high
sizeTxt:		.string "The size of the document is: %d \n" 			// Format String to output Size of documented
lowFreqTxt:		.string "The Lowest frequency in the document is: %d % \n"	// Format String to output lowest frequency
highFreqTxt:		.string "The Highest frequency in the document is: %d % \n" 	// Format String to output highest Frequency

//defining macros
	define(base, x0)
	define(argument1, x1)
	define(userinput, x19)
	define(counter, x20)
	define(seed, x21)
	define(maxrand, x22)
	define(randnum, x23)
	define(lowfreq, x24)	
	define(highfreq,x25)
	define(size, x26)
	define(freq,x28)


	
	//Main Declaration
	.balign 4 //Forces Alignment
	.global main

main:

	stp	x29,x30, [sp, -16]!	//Saves State
	mov	x29, sp 		//Saves State to x29

	ldr	base, =fmt		// Loades Format String for Initial Prompt
	bl 	printf			// Prints Intial Prompt

	ldr 	base, =input0 		// Loads Format String for user input
	ldr	argument1, =input 	// Loads integer Value for user input
	bl	scanf 			// Scans for user input
	ldr	argument1, =input	//Loads user input into x1
	ldr 	userinput, [x1]		// Loads value x1 points to in x19
	mov 	x20, 5 			//sets x20 value to 5 (min user input)
	mov 	x21, 20 		// sets x21 value to 20 (max user input)

	cmp 	userinput,x20 	//compares User Input value to lower bound
	b.lt 	lowTest 	//If user input is less than Lower Bound -> lowTest, else continue
	cmp 	userinput, x21 	//compares User Input value to upper bound
	b.gt	highTest	//If user input is greater than upper bound -> hightest, else continue


	//Intializes Registers
	mov 	counter, 0	//Sets x20 to 1, counter for loop
	mov	seed, 0		//stores random seed
	mov 	maxrand, 0 	// used to store max for random numbers
	mov 	randnum, 0 	// Stores Random number (0-9)
	mov 	lowfreq, 10 	//Stores lowest frequency, set to 10 as all initial values will be less than 10
	mov 	highfreq, 0 	//Stores highest frequency, set to 0 as initial values will be greater than or equal to 0
	mov 	size, 0 	//Stores sum of all occurances
	mov	x27, 100	//Stores the number 100 for frequency calculation
	mov	freq, 0		//Stores frequency

	ldr 	base, =word 	//Loads format string for list of numbers title
	bl	printf 		//prints format string for list of numbers title


	//initializes time and srand for rand
	mov 	base, 0	// Initialized x0 to 0 for time and srand
	bl 	time	//initializes time
	bl 	srand	//initializes srand


	b test// Pre test

//loop body
loop:
	
	mov     base, 0		//Initializes x0 to 0 for rand
	bl      rand		//initializes rand numb to x0


	//Modulus stored in x23 (random number)
	mov     seed, base 			//random number saved in x21
	mov     maxrand, 10 			// x22 stores top threshold for random number
	sdiv    randnum, seed, maxrand 		// divides random number/top threshold, stores in x23
	mul     randnum, randnum, maxrand 	// multiply quotient * top threshold, store in x23
	sub     randnum, seed, randnum 		//subtract random number by above answer, save in x23
	mov     argument1, randnum      	// Moves modulus number to x1 argument for print argument


	//Prints random number
	ldr     base, =rannum 	//loads format string to random number list
	bl      printf 		// prints random number
	//argument 1 is x1 (random number)


	//Check if Lowest and Highest Frequency
	cmp	randnum,lowfreq  	// compares random number to current lowest frequency
	b.lt	lowFreq 		//if random number is lower than lowest frequency -> lowFreq, else continue

	cmp 	randnum, highfreq	//compares random number to current highest frequency
	b.gt	highFreq		//if random number is higher than highest frequency -> highFreq, else continue


	add 	size,size, randnum	//adds random number to sum total
	add	counter,counter, 1	//increments 1 to counter
	

//Test loops
test:
	cmp 	counter, userinput 	// compares current counter to user input
	b.lt 	loop			// if current counter is less than user input -> loop, else continue
	b	next			// continues to next



//sets lowest frequency
lowFreq:
	mov 	lowfreq, randnum	//sets current lowest frequency to random number
	cmp	randnum, highfreq 	// compares random number to current highest frequency
	b.gt	highFreq 		// if random number is higher than highest frequency -> highfreq, else continue
	add 	size,size,randnum 	// adds random number to sum total
	add	counter,counter, 1	// increments 1 to counter
	b 	test 			// loops test case

	
//sets highest frequency
highFreq:
	mov 	highfreq, randnum 	// sets current highest frequency to random number
	add	size,size, randnum 	// adds random number to sum total
	add	counter,counter,1 	//increments 1 to counter
	b	test 			//loops test case


	
//prints error message and ends program
lowTest:
	ldr	base, =lowTxt 	// loads format string for user input too low
	bl 	printf		//prints string for user input too low

	//ends program, Restores state of Frame pointer and Link register
	ldp     x29,x30,[sp],16
	ret



//prints error message and ends program
highTest:
	ldr     base, =highTxt 	// loads format string for user input too high
	bl 	printf 		// prints string for user input too high

	//ends program, Restores state of Frame pointer and Link register
	ldp     x29,x30,[sp],16
	ret



//calcuates frequency and prints, then ends program
next:

	mul	freq,x27,lowfreq 	//Multiplication for frequency (100 x lowest frequency) stores in x28
	udiv	freq,freq,size 		//divides x28 by size/sum of document, stores back in x28

	ldr	base, =sizeTxt	//Loads format string for document sum/size
	mov 	argument1, size	//sets x1 first argument to size/sum of document
	bl 	printf		//prints format string of document size/string

	ldr	base,=lowFreqTxt	//Loads format string for lowest frequency
	mov	argument1,freq		//sets x1 first argument to lowest frequency
	bl	printf			//prints format string of lowest frequency

	mul 	freq, x27, highfreq	//Multiplication for frequency (100 x highest frequency) stores in x28
	udiv	freq,freq, size		//divides x28 by size/sum of document, stores back in x28

	ldr	base, =highFreqTxt	// Loads format string for highest frequency
	mov	argument1, freq		//sets x1 first argument to highest frequency
	bl 	printf			//prints format string of highest frequency


	//ends program, Restores state of Frame pointer and Link register
	ldp	x29,x30,[sp],16
	ret

//ends program, restores state of frame pointer and link register
end:
	ldp	x29,x30,[sp],16
	ret


	//Data for input integer
	.data
input:  .int	0
	
